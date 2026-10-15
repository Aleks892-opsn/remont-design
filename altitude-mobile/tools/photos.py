# Фото для сайта: стираем чужие логотипы, слегка чистим и сохраняем в webp
import cv2, numpy as np
U = '/root/.claude/uploads/582e4954-cf52-5e21-b49c-abeb6edfe1a3/'
OUT = 'stroy4/photos/'
# (файл, имя, [(x0,y0,x1,y1,режим)])  режим: on_white — цветной логотип на белом; light — светлый текст на тёмном
P = [
 ('3273d52e', 'economy',  []),
 ('96ca56a9', 'comfort',  []),
 ('be853b07', 'business', []),
 ('0727cc41', 'jet',      []),
 ('581a5533', 'cabin',    []),
 ('6d1dd513', 'window',   []),
 ('40c27b32', 'wing',     [(520, 382, 640, 409, 'text')]),
 ('c000aadd', 'lounge',   [(960, 355, 1040, 385, 'on_white')]),
 ('77843ab5', 'first',    [(626, 365, 742, 392, 'text'), (1026, 312, 1075, 368, 'text')]),
 ('73107e50', 'abroad',   [((398, 151), (662, 226), (662, 272), (398, 225), 'col'), ((1080, 243), (1143, 243), (1128, 313), (1023, 313), 'col')]),
 ('2ad66a16', 'ticket',   [(578, 212, 676, 242, 'light')]),
 ('56e80125', 'baggage',  [(396, 388, 596, 425, 'text'), (268, 338, 318, 375, 'text'), (607, 358, 648, 383, 'text')]),
 ('8c2e4644', 'relax',    [((1022, 199), (1029, 174), (1147, 137), (1154, 161), 'navy'), (874, 214, 921, 237, 'navy')]),
]
def fill(im, mask, src_ok=None):
    # заливка дыры плавным фоном вокруг (нормализованное размытие) — без пятен
    src = ((~mask) if src_ok is None else ((~mask) & src_ok)).astype(np.float32)[..., None]; f = im.astype(np.float32)
    out = f.copy()
    for sg, th in ((4, .25), (9, .2), (20, .1), (40, .02)):
        num = cv2.GaussianBlur(f * src, (0, 0), sg); den = cv2.GaussianBlur(src[..., 0], (0, 0), sg)[..., None]
        ok = (den > th) & mask[..., None] & (out == f).all(axis=2, keepdims=True)
        out = np.where(ok, num / np.maximum(den, 1e-3), out)
    noise = np.random.normal(0, 1.2, im.shape).astype(np.float32)
    out = np.where(mask[..., None], out + noise, f)
    return np.clip(out, 0, 255).astype(np.uint8)
def clean(im, boxes):
    if not boxes: return im
    f = im.astype(np.int16); B, G, R = f[..., 0], f[..., 1], f[..., 2]
    V = f.max(axis=2); S = V - f.min(axis=2)
    white = ((V > 200) & (S < 40)).astype(np.uint8)
    nearw = cv2.dilate(white, np.ones((15, 15), np.uint8)) > 0
    mask = np.zeros(im.shape[:2], bool)
    for bx in boxes:
        mode = bx[-1]; box = np.zeros_like(mask)
        if isinstance(bx[0], tuple):   # наклонная надпись — многоугольник
            poly = np.zeros(mask.shape, np.uint8); cv2.fillPoly(poly, [np.array(bx[:-1], np.int32)], 1); box = poly > 0
        else:
            x0, y0, x1, y1 = bx[:4]; box[y0:y1, x0:x1] = True
        if mode == 'on_white':
            m = box & (~((V > 200) & (S < 40))) & ((B - R > 18) | (R - B > 60)) & nearw
        elif mode == 'text':
            bg = np.percentile(V[box], 85)
            m = box & (((bg - V) > 22) | (B - R > 25) | (R - B > 60))
        elif mode == 'col':
            m = box & (((B - R > 25) & (V < 185)) | (R - B > 50) | (B - R > 70))
        elif mode == 'all':
            m = box
        elif mode == 'dark':
            m = box & (V < 110)
        elif mode == 'sat':
            m = box & (S > 55)
        elif mode == 'navy':
            m = box & (V < 160) & (B - R > 15)
        else:
            m = box & (V > 150)
        mask |= m
    mask = cv2.dilate(mask.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
    wsrc = ((V > 190) & (S < 45)) if any(b[-1] == 'col' for b in boxes) else None
    return fill(im, mask, wsrc)
BLUR = {'baggage': (0, 0, 700, 560, 2.2), 'relax': (745, 0, 1408, 560, 1.4)}
import os; os.makedirs(OUT, exist_ok=True)
for key, name, boxes in P:
    im = cv2.imread(U + key + '-image.jpg')
    im = clean(im, boxes)
    if name in BLUR:
        x0, y0, x1, y1, sg = BLUR[name]; im[y0:y1, x0:x1] = cv2.GaussianBlur(im, (0, 0), sg)[y0:y1, x0:x1]
    im = cv2.fastNlMeansDenoisingColored(im, None, 2, 2, 7, 21)
    bl = cv2.GaussianBlur(im, (0, 0), 1.0); im = cv2.addWeighted(im, 1.25, bl, -0.25, 0)
    cv2.imwrite(OUT + name + '.webp', im, [cv2.IMWRITE_WEBP_QUALITY, 82])
    cv2.imwrite('photos/chk_' + name + '.jpg', im, [cv2.IMWRITE_JPEG_QUALITY, 80])
print('ok')
