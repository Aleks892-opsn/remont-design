import cv2, numpy as np
from PIL import Image
src='/root/.claude/uploads/582e4954-cf52-5e21-b49c-abeb6edfe1a3/e9ac6509-image.jpg'
im=cv2.imread(src)
im=cv2.fastNlMeansDenoisingColored(im,None,3,3,7,21)
sr=cv2.dnn_superres.DnnSuperResImpl_create(); sr.readModel('models/EDSR_x2.pb'); sr.setModel('edsr',2)
up=sr.upsample(im).astype(np.float32)/255.0
bl=cv2.GaussianBlur(up,(0,0),1.2); up=np.clip(up+0.35*(up-bl),0,1)
L=up.max(axis=2)
a=np.clip((L-0.045)/0.80,0,1)          # чёрный → прозрачно, белое → непрозрачно
a=a**0.85
C=np.where(a[...,None]>0.02, up/np.maximum(a[...,None],1e-3), 1.0)
C=np.clip(C,0,1)
# лёгкий холодный оттенок в тенях облаков
C=C*np.array([1.0,0.985,0.96])[None,None,:]  # BGR: чуть больше синего
a8=(a*255).astype(np.uint8)
ys,xs=np.where(a8>10); pad=24
y0,y1,x0,x1=max(ys.min()-pad,0),min(ys.max()+pad,a8.shape[0]),max(xs.min()-pad,0),min(xs.max()+pad,a8.shape[1])
rgba=np.dstack([(C[...,::-1]*255).astype(np.uint8),a8])[y0:y1,x0:x1]
img=Image.fromarray(rgba,'RGBA')
w=1200; img=img.resize((w,round(img.height*w/img.width)),Image.LANCZOS)
img.save('stroy4/hero/cloud-title.webp',quality=86,method=6)
print(img.size)
bg=Image.new('RGBA',img.size,(22,88,240,255)); bg.alpha_composite(img); bg.convert('RGB').save('sshot4/cloud_title_check.jpg',quality=88)
