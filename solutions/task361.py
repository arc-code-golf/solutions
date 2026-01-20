def p(r):n=[r+r for r in r+r];return[[[n[l][i]|n[r-a+i][r+a+e+~l]|n[r+r+e+~l][a+a+e+~i]|n[r+a+e+~i][a-r+l]for i in range(10)]for l in range(10)]for e in range(10)for a in range(10)for r in range(10)if all(all(r[a:a+e])for r in n[r:r+e])][-1]
# ----------------------------------------------------------------
# compression: frozen
# huffman: 658c010680501044aff201654501944eb2164b5b626d1905a4b3a792240ce3795e
