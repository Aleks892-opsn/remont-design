# Новые фото (вторая генерация): убираем надписи и логотипы, без уменьшения, лёгкая резкость
import cv2, numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('ph', 'tools/photos_lib.py'); ph = importlib.util.module_from_spec(spec); spec.loader.exec_module(ph)
U = ph.U; OUT = 'stroy4/photos/'
# (файл, имя, надписи под заливку, области под размытие (x0,y0,x1,y1,sigma))
P = [
 ('0981ce98', 'economy',  [], [(183, 368, 232, 418, 4)], [(614, 430, 722, 488), (858, 424, 948, 460), (1000, 424, 1054, 450), (448, 424, 508, 468), (648, 690, 752, 724)]),
 ('a3f128f3', 'comfort',  [], []),
 ('1b8ab074', 'business', [], [(138, 392, 242, 562, 4), (596, 496, 654, 518, 3)]),
 ('b20ce8cc', 'jet',      [(803, 378, 872, 407, 'dark'), (866, 344, 893, 362, 'all')], []),
 ('e574e3e1', 'window',   [], []),
 ('2e3188e9', 'cabin',    [(128, 226, 178, 254, 'dark'), (845, 186, 916, 224, 'dark'), (743, 228, 797, 272, 'dark')], []),
 ('ac0c87f3', 'wing',     [], []),
 ('1043e86b', 'lounge',   [], []),
 ('b2456079', 'first',    [(273, 508, 304, 542, 'text')], [(0, 326, 118, 350, 4), (372, 340, 478, 362, 4), (828, 368, 1002, 418, 2.5)]),
 ('9cf40083', 'bizseat',  [], []),
 ('4b12b6f1', 'jetcarpet', [], []),
 ('26824a54', 'fleet',    [], []),
]
def flat(im, x0, y0, x1, y1):
    reg = im[y0:y1, x0:x1].reshape(-1, 3).astype(np.float32)
    col = np.percentile(reg, 75, axis=0)                     # светлый тон карточки
    m = np.zeros(im.shape[:2], np.float32); m[y0 + 3:y1 - 3, x0 + 3:x1 - 3] = 1
    m = cv2.GaussianBlur(m, (0, 0), 2.5)[..., None]
    shade = cv2.GaussianBlur(im, (0, 0), 25).astype(np.float32)   # сохраняем общий свет
    tone = col * (shade / max(shade[y0:y1, x0:x1].mean(), 1)) 
    out = im.astype(np.float32) * (1 - m) + np.clip(tone + np.random.normal(0, 1.5, im.shape), 0, 255) * m
    return out.astype(np.uint8)
for item in P:
    key, name, boxes, blurs = item[:4]; flats = item[4] if len(item) > 4 else []
    im = cv2.imread(U + key + '-image.jpg')
    # по просьбе: без закраски и размытия — фото как есть
    cv2.imwrite(OUT + name + '.webp', im, [cv2.IMWRITE_WEBP_QUALITY, 90])
    cv2.imwrite('photos/n_' + name + '.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 85])
print('ok')
