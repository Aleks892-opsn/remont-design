# Собирает основное портфолио: три темы, блок «О себе» в виде переписки
import gen, av
for k, th in gen.THEMES.items():
    open(f'{k}.html', 'w').write(gen.page(k, th, about=av.AB['a3']))
print('ok')
