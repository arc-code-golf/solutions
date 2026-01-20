def p(i):n,m=range,15;f=sum(i,p:=[]);i=[[]];[(i:=[i+[(r,p)]for i in i for r in n(3*m)if f[r]<1],p:=[])for r in n(3*m)if p==(p:=p+[n for n in n(r,150,m)if f[n]&(r<m)])>[]];return max([*zip(*[((any(n+min(i)-r in i for r,i in i if r%m<5+n%m)+f[n]%5)%3for n in n(150))]*m)]for i in i)
# ----------------------------------------------------------------
# compression: frozen
# huffman: 650fc542c050e8577699c2c2de65f52388bda71cc027b65fbfb489ee
