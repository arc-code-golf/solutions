import re
def p(n):u={0:(0,i:=max(n:=re.sub(', ','',f'{n,*zip(*n)}'),key=n.count))}|{len(max(re.findall(f'{l}+',n)))*(((r:=len(re.findall(f'{l}{l}([^]){l}]+){l}|$',n+n[::-1])[0]))>0)+1)+r>>1:(1+r>>1,l)for l in{*n}-{*'([^])',i}};return[[int([u[max(abs(l),abs(r))][1],i][u[max(abs(l),abs(r))][0]>min(abs(l),abs(r))])for l in range(-max(u),max(u)+1)]for r in range(-max(u),max(u)+1)]
# ----------------------------------------------------------------
# compression: frozen
# huffman: 7d4e074a402118be8a40e00e6563e845c4e06d24fb0b4ba8ccbba7eded966fae
