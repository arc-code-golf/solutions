def	p(r):
	e,s=max((len({*str(n:=[e[m:m+3]for	e	in	r[e:e+3]])}),n)for	e	in	range(len(r))for	m	in	range(len(r[-1])))
	for	n	in	range(len(r[-1])):
		for	e	in	range(len(r)-n*3):
			for	m	in	range(len(r[-1])-n*3):
				for	p	in	range(len(r[-1])):
					for	p	in	range(n*3*all(r[e+p][m+o]==s[p//n][o//n]or	r[e+p][m+o]==r[-1][-1]!=s[p//n][o//n]==max({*s[1]}-{r[-1][-1]})for	p	in	range(n*3)for	o	in	range(n*3))):
						for	o	in	range(n*3):r[e+p][m+o]=s[p//n][o//n]
					s=*zip(*s[::-1]),
	return	r
# ----------------------------------------------------------------
# compression: frozen
# huffman: 755035428021189de1166ea43da19c04b13129c156ee2e60fd39c0f01a2e
