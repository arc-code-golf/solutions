def p(e):o=e.index(min(e,key=set))+1;f={a*1j+r:e for a,e in enumerate(e[::o])for r,e in enumerate(e[::o])};return[[[e or[f[s:=a//o*1j+r//o],*[f[n+s-e]for e in f if(f[e]==f[n])*2>abs(s-e)]][-1]for r,e in enumerate(e)]for a,e in enumerate(e)]for n in f if all(f.get(n+1j**a)for a,e in enumerate(e))][-1]
# ----------------------------------------------------------------
# compression: frozen
# huffman: 754d4902012014bd4acb466419b9485a841f415101b83bc28ee6de38
