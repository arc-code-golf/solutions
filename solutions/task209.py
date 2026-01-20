def p(e):
 f=e
 for i in f*4:f=[[*i]for i in zip(*f[~4:])if{*i}-{0,4}];e=[[*i]for i in zip(*e[(4in e[-1])-2::-1])]
 for(i,a)in enumerate(e):
  if[0for(t,a)in enumerate(e)for(r,a)in enumerate(i*a)for(n,a)in enumerate(i*all(e in[0,((f+20*[[]])[(n-t)//i]+20*[4])[(o-r)//i]]for(n,e)in enumerate(e)for(o,e)in enumerate(e))*f)for(o,a)in enumerate(i*a)for e[n+t][o+r]in[f[n//i][o//i]]]:return e
# ----------------------------------------------------------------
# compression: frozen
# huffman: 6d4e3d02012014de9da2b122a0299ce46980170f8a640167a760a0a5eafb5f
