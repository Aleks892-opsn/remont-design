# Вертикальный фон 9:16 из фото крыла: та же чистка надписи, затем увеличение x2
import cv2, sys
sys.path.insert(0, 'tools')
import importlib.util
spec = importlib.util.spec_from_file_location('ph', 'tools/photos_lib.py'); ph = importlib.util.module_from_spec(spec); spec.loader.exec_module(ph)
im = cv2.imread(ph.U + '40c27b32-image.jpg')
im = ph.clean(im, [(520, 382, 640, 409, 'text')])
h = im.shape[0]; w = round(h * 9 / 16); cx = int(im.shape[1] * 0.42)
crop = im[:, cx - w // 2: cx + w // 2]
sr = cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('models/EDSR_x2.pb'); sr.setModel('edsr', 2)
up = sr.upsample(crop)
cv2.imwrite('stroy4/photos/wing-bg.webp', up, [cv2.IMWRITE_WEBP_QUALITY, 78]); print(up.shape)
