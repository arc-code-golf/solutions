def p(i):r=[[i[n+f//3][u+f%3]for f in range(9)]for n in range(len(i)-2)for u in range(len(i[n])-2)if([i[n+f//3][u+f%3]for f in range(9)]==[i[n+f//3][u+f%3]for f in range(9)][::-1])*len({i[n+f//3][u+f%3]for f in range(9)})>2];[[i[n+f//3][u+f%3]for f in range(9)for i[n+f//3][u+f%3]in[e[f]]]for e in r for n in range(len(i)-2)for u in range(len(i[n])-2)if([i[n+f//3][u+f%3]for f in range(9)]==[(i[n+f//3][u+f%3]>0)*e[f]for f in range(9)][::-1])*len({i[n+f//3][u+f%3]for f in range(9)})>1];return i
# ----------------------------------------------------------------
# compression: frozen
# huffman: b550890680000cfd95205a4917a8d48fcc106d19594981f4ef2988a050c0bbd95a
