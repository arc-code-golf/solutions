def p(n):
 *u,e={d*66+f:(n)for d,n in enumerate(n)for f,n in enumerate(n)if n},
 for d in e:r={d};u=[i for i in u if i==i-{d-66,d-1}or r.update(i)]+[r]
 for i in u:
  for d in i:
   for r in i:
    t=i
    for t in 1//len([f for f in t if e[d]==e[f]])*u:
     for m in i-{r}:
      for f in[f for f in t if e[d]==e[f]==e[r]]:f+=(len([f for f in t if e[d]==e[f]==e[r]])^6)%6*(m-r);n[f//66][f%66],={e[f]for f in t}-{e[d]}
 return n
# ----------------------------------------------------------------
# compression: frozen
# huffman: 7d4d0b0603201806a053fc307a6e06a1e924698c8ad8daa440bafb2ab330061fdfdb
