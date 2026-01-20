def	f(r,n,e,l,d):
	if	len(r)>n+1>1>r[e][n]%3:r[e][n]=3;return	f(r,n+d,e,l,d)
	if	r[e][n]%3:return	f([[*n]for	n	in	zip(*r)],e,n-d,l-1,1)or	f([[*n]for	n	in	zip(*r)],e,n-d,l-1,-1)if	l	else(3>r[e][n])*r
def	p(r):(n,e),(l,d)=[(n,e)for	n	in	range(len(r))for	e	in	range(len(r))if	r[e][n]%2];return	f([[*n]for	n	in	r],n,e,2,1)or	f(r,n,e,2,-1)if	l>n	else[[*n]for	n	in	zip(*p([[*n]for	n	in	zip(*r)]))]
# ----------------------------------------------------------------
# compression: frozen
# huffman: 8d50cd0a40700c3ff31e6a632adc8817d1bf52464aa3e1e2e905a4509c98df77
