def p(r):
 for n in range(100):
  e=[f for f in range(100)if r[f//10][f%10]<5in r[f//10][:f%10]and 5in r[f//10][f%10:]and f<50];i=[f for f in range(100)if r[f//10][f%10]==n]
  if[e[0]-n for n in e]==[i[0]-n for n in i]:
   for f in e:r[f//10][f%10]=n
   for f in i:r[f//10][f%10]=0
 for n in range(100):
  e=[f for f in range(100)if r[f//10][f%10]<5in r[f//10][:f%10]and 5in r[f//10][f%10:]and f>50];i=[f for f in range(100)if r[f//10][f%10]==n]
  if[e[0]-n for n in e]==[i[0]-n for n in i]:
   for f in e:r[f//10][f%10]=n
   for f in i:r[f//10][f%10]=0
 return r
# ----------------------------------------------------------------
# compression: frozen
# huffman: cd500b0680600c06a0530ca29016825e17991fd196c1cad4fdab2005020986ef6d
