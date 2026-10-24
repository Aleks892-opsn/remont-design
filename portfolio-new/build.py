# Собирает основное портфолио: три темы, «О себе» перепиской, компьютерная раскладка «Крупно»
import gen, av, dv
for k, th in gen.THEMES.items():
    a = dict(av.AB['a3'])
    a['css'] += dv.D['d1'][1]
    a['js'] += dv.D['d1'][2]
    open(f'{k}.html', 'w').write(gen.page(k, th, about=a))
print('ok')
