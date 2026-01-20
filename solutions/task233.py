def p(n):
 for i,o in sorted([[-e.count(2),e]for f in range(len(n)-2)for d in range(len(n[0])-2)if all(e:=[n[f+i][d+e]for i in range(3)for e in range(3)])and{*e}!={2}!=[2for i in range(3)for e in range(3)for n[f+i][d+e]in[0]]]):
  for i in range(4):[[2for i in range(3)for e in range(3)for n[f+i][d+e]in[o[i*3+e]]]for f in range(len(n)-2)for d in range(len(n[0])-2)if all(n[f+i][d+e]==2!=o[i*3+e]or o[i*3+e]-n[f+i][d+e]==2in n[f+i]for i in range(3)for e in range(3))];n=[n[::-1]for*n,in zip(*n)if 2in n]
 return n
# ----------------------------------------------------------------
# compression: frozen
# huffman: a550c54280000cbdf315e3461ae009e54be64c864e71b4cdbfc3cc6e9a578b
