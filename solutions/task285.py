def p(e):
 for g in range(8):
  e[::-1]=zip(*e)
  for g in range(len(e)):
   for f in range(len(e)):
    for i,h in(r:=[(g,f)]):*e[i],=e[i];e[i][f+f-h-1]=e[g][f-1];r+=[(p+i,h+n)for p in range(-1,2)for n in range(-1,2)if 0<e[g][f-1]!=(2*(2*e)[p+i])[h+n]==e[g][f]>0==e[p+i][f+f-h-n-1]]
 return e
# ----------------------------------------------------------------
# compression: frozen
# huffman: 6d4d4556802110de738a71479a0de245109b3210b13dbd0346d37c79
