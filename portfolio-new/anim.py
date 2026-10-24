# Демо: одна страница, пять наборов анимаций
import gen, av
NAMES = {'rise': 'Подъём', 'blur': 'Проявление из размытия', 'wipe': 'Шторка', 'flip': 'Переворот', 'scale': 'Масштаб'}
for i, m in enumerate(NAMES, 1):
    open(f'an{i}.html', 'w').write(gen.page('v1', gen.THEMES['v1'], about=av.AB['a3']).replace('<body>', f'<body data-anim="{m}">', 1))
print('ok')
