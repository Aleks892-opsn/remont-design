import re, os, shutil, sys
def collect(src, dst):
    seen=set(); todo=['index.html']
    while todo:
        f=todo.pop()
        if f in seen: continue
        seen.add(f)
        p=os.path.join(src,f)
        if not os.path.isfile(p): continue
        os.makedirs(os.path.dirname(os.path.join(dst,f)) or dst, exist_ok=True)
        shutil.copy(p, os.path.join(dst,f))
        if f.endswith(('.html','.css','.js')):
            t=open(p,encoding='utf-8',errors='ignore').read()
            refs=re.findall(r'''(?:src|href|srcset|poster|data-src)\s*=\s*["']([^"'#?]+)''',t)+re.findall(r'''url\(\s*["']?([^"')?#]+)''',t)+re.findall(r'''["']((?:img|assets|hero|photos|images)/[^"'?#\s]+)["']''',t)
            for r in refs:
                for part in r.split(','):
                    part=part.strip().split(' ')[0]
                    if not part or part.startswith(('http','data:','//','mailto:','tel:','#')): continue
                    q=os.path.normpath(os.path.join(os.path.dirname(f),part))
                    if not q.startswith('..'): todo.append(q)
    return seen
for k,d in [('protektor','protektor'),('altitude','altitude-site'),('forte','opora-site')]:
    out=f'sites/{k}'; shutil.rmtree(out,ignore_errors=True)
    s=collect('/home/user/-/'+d,out)
    print(k,len([x for x in s if os.path.isfile(os.path.join('/home/user/-/'+d,x))]))
