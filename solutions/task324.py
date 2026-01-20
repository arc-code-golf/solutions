def	p(u):
	i=sum(u,[]);o=i.count;f=i[o(i[0])<4];m,t={},{()}
	for(r,n)in	enumerate(u):
		for(e,a)in	enumerate(n):
			if	o(a)<4:m[f	in	n	and	f	in	i[e::len(n)]]=a;t|={r+e,(r-e,)}
	for(r,n)in	enumerate(u):
		for(e,a)in	enumerate(n):
			if{r+e,(r-e,)}&t:n[e]=m[f	in	n	and	f	in	i[e::len(n)]]
	return	u
# ----------------------------------------------------------------
# compression: frozen
# huffman: a54d4b228021105e4f07a10860553a4942981834915aa5bb231b5660f7bdbf
