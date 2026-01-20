def p(f):
 a=f
 for n in range(len(f)):
  for r in range(len(f[0])):
   if a[n][r]==1:z={(r,n)}
 for n in f:z={(r+l,e+n)for l,n in z for r in range(-1,2)for e in range(-1,2)if e+n in range(len(f))!=r+l in range(len(f[0]))!=0<f[e+n][r+l]}
 for n in(1,1,-1)*4:
  f=[z for*z,in zip(*f[::n])]
  for e in range(-13,13):
   for r in range(-13,13):
    if all(e+n in range(len(f))!=r+l in range(len(f[0]))!=a[n][l]in(1,3,f[e+n][r+l])for l,n in z):
     for l,n in z:f[e+n][r+l]=a[n][l]
 return f
# ----------------------------------------------------------------
# compression: frozen
# huffman: 95503b0201300cdd9d22b6fea098d0935407684015c50277a701c5647dff64
