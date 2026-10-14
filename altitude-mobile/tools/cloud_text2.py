# Облачная надпись «Выше ожиданий» в две строки: вырезка с чёрного фона, x2, белее
import cv2, numpy as np
from PIL import Image
src = '/root/.claude/uploads/582e4954-cf52-5e21-b49c-abeb6edfe1a3/61b5b1ca-image.jpg'
im = cv2.imread(src)[180:410, 160:1660]           # только полоса с текстом
im = cv2.fastNlMeansDenoisingColored(im, None, 3, 3, 7, 21)
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('models/EDSR_x2.pb'); sr.setModel('edsr', 2)
up = sr.upsample(im).astype(np.float32) / 255.0
bl = cv2.GaussianBlur(up, (0, 0), 1.2); up = np.clip(up + 0.3 * (up - bl), 0, 1)
L = up.max(axis=2)
a = np.clip((L - 0.05) / 0.62, 0, 1) ** 0.8          # плотнее и белее
C = np.clip(up / np.maximum(a[..., None], 1e-3), 0, 1)
C = 1 - (1 - C) * 0.45                                # тени в складках слабее — облака белее
C = C * np.array([1.0, 0.99, 0.975])[None, None, :]   # BGR: еле заметный холодный оттенок
rgba = np.dstack([(C[..., ::-1] * 255).astype(np.uint8), (a * 255).astype(np.uint8)])
gap = (703 - 160) * 2                                 # середина просвета между словами
def crop(x):
    al = x[..., 3]; ys, xs = np.where(al > 8); p = 16
    return x[max(ys.min() - p, 0):ys.max() + p, max(xs.min() - p, 0):xs.max() + p]
w1, w2 = crop(rgba[:, :gap]), crop(rgba[:, gap:])
lead = int(w2.shape[0] * -0.02)                       # строки почти вплотную
W = max(w1.shape[1], w2.shape[1]); H = w1.shape[0] + lead + w2.shape[0]
out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
out.alpha_composite(Image.fromarray(w1, 'RGBA'), ((W - w1.shape[1]) // 2, 0))
out.alpha_composite(Image.fromarray(w2, 'RGBA'), ((W - w2.shape[1]) // 2, w1.shape[0] + lead))
out.save('stroy4/hero/cloud-title.webp', quality=86, method=6)
print(out.size)
bg = Image.new('RGBA', out.size, (22, 88, 240, 255)); bg.alpha_composite(out); bg.convert('RGB').save('sshot4/cloud_title_check.jpg', quality=88)
