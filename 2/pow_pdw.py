import time 

def pow_it(x, n):
	'''
	iterate raising x to the n
	x : base
	n : exponent 
	'''

	print 'Raising {0} to the {1}'.format(x,n)
	start = time.time()
	a = 1
	i = n
	if n == 0:
		return 1
	else:
		while i > 0:
			a *= x
			i -= 1
	stop = time.time()
	run_time = stop - start
	print 'Raised {0} to the {1} in {2}'.format(x,n,run_time)
	return a

def pow_re(x,n,top=True):
	'''
	recursively raising x to the n
	x : base
	n : exponent
	top : default true for explicit calls, default false for recursive subcalls
	'''
  
	if top:
		print 'Raising {0} to the {1}'.format(x,n)
		start = time.time()

	a = x

	if n == 0:
		return 1
	else:
		a *= pow_re(a, n-1, False)
		if top:
			stop = time.time()
			run_time = stop - start
			print 'Raised {0} to the {1} in {2}'.format(x,n,run_time)
		return a
