import unittest

def ValidaPrimo(a):
	k = 1
	divisor = 0
	while k <= a:
		if a % k == 0:
			divisor += 1
		k += 1

	if divisor > 2:
		return False
	return True

def fatora(n):
	#solucao do abnaldo
	fatores = []
	i = 2
	while n > 1:
		if  n % i == 0:
			fatores.append(i)
			n = n/i
		else:
			i += 1
	return fatores

class test(unittest.TestCase):
	def testFunc(self):
		self.assertEqual([2,2],fatora(5))	
	

if __name__ == "__main__":
	unittest.main()

