# Вертикальные кадры для маленьких фото: вырезаем нужную часть и увеличиваем x2 (EDSR)
import cv2, sys, importlib.util
spec = importlib.util.spec_from_file_location('ph', 'tools/photos_lib.py'); ph = importlib.util.module_from_spec(spec); spec.loader.exec_module(ph)
key, name, ratio, cx = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
boxes = [b for k, n, b in ph.P if k == key][0]
im = ph.clean(cv2.imread(ph.U + key + '-image.jpg'), boxes)
im = cv2.fastNlMeansDenoisingColored(im, None, 2, 2, 7, 21)
h = im.shape[0]; w = round(h * ratio); c = int(im.shape[1] * cx); x0 = max(0, min(im.shape[1] - w, c - w // 2))
crop = im[:, x0:x0 + w]
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('models/EDSR_x2.pb'); sr.setModel('edsr', 2)
up = sr.upsample(crop); bl = cv2.GaussianBlur(up, (0, 0), 1.2); up = cv2.addWeighted(up, 1.3, bl, -0.3, 0)
cv2.imwrite('stroy4/photos/' + name + '.webp', up, [cv2.IMWRITE_WEBP_QUALITY, 82]); print(name, up.shape)
