def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

n = 0
fib_sum = 0
s = 0
while s < 4 * (10 ** 6):
	s = fib(n+1)
	if s % 2 == 0:
		fib_sum	+= s
	n+=1

print fib_sum