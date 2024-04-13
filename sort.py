def f(nst):
	if (len(nst)<3): 
		if (len(nst)==2):
			if (nst[1]>nst[0]):
				nst[0],nst[1]=nst[1],nst[0]
				return nst
		if (len(nst)==1 or len(nst)==0):
			return nst
	k = jun(nst)
	n = [[i for i in nst if i > k],[i for i in nst if i <= k]]
	if (n[0]==[] or n[1]==[]):
		return n[0]+n[1]
	return f(n[0])+f(n[1])
#You can sort the list by typing

def GO(ng=50,lmax=1,number = [1,114514]):
	for i in range(ng):
		k = random.randint(number[0],number[1])
		s = rand(k,lmax)
		#k = 9**(i+1) + 1
		#s = [10000] + [1]*(9**(i+1))
		print(f"The{i+1}:")
		print(f"10^{k-1}")

		op0 = time.time()
		o = f(s)
		end0 = time.time()
		#print(o)
		print(f"f spend {end0-op0}")
#You can Timing
