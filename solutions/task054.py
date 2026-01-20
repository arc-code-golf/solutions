def p(r):
 p=[i*1for i in r]
 for i in range(28):
  for o in range(28):
   if r[i][o+1]==r[i][o-1]!=r[i][o]!=r[i+1][o]==r[i-1][o]!={r[i][o+1],r[i+1][o+1]}!={r[i+1][o]}:
    for e in range(28):
     for t in range(28):
      if r[i][o]==r[e][t]:
       for n in range(-1,2):
        for d in range(-1,2):
         f=1
         if r[i+n*f][o+d*f]!=r[i+1][o+2]:
          p[e+n*f][t+d*f]=r[i+n][o+d];f+=1
          if r[i][o]!=r[i+n*f][o+d*f]!=r[i+1][o+2]:
           while r[e+n*f][t+d*f]!=r[i+1][o+2]:p[e+n*f][t+d*f]=r[i+n][o+d];f+=1
    for n in range(-2,3):
     for d in range(-2,3):p[i+n][o+d]=r[i+1][o+2]
 return p
# ----------------------------------------------------------------
# compression: frozen
# huffman: 8d503d22002014de3bc5b351359405749234a022a8240cb83b7a28025b7dffe5
