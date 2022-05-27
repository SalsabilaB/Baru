from math import sqrt

N = 510143758735509025530880200653196460532653147
primes = []

def isPrime(x):
	global primes
	if x in primes:
		return True
	
	for divisor in primes:
		if divisor > sqrt(x):
            # kalau divisor > sqrt (x) maka kelebihan angkanya
			break
	
		if x % divisor == 0:
			# X is non-prime
			return False
	
	primes.append(x)
	return True
	
def factorize(x):
	primeFactors = []
	divisor = 2
	while x > 1:
		if isPrime(divisor):
			if x % divisor == 0:
				x = x / divisor
				primeFactors.append(divisor)
			else:
				divisor += 1
		else:
			divisor += 1	
	return primeFactors
	
factors = factorize(N)

print(factors)