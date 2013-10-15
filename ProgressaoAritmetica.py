import unittest

def calculaProgressao(ar):
listaFinal = []
lisAux = []
r = 1

#ar =  (1,2,3,4,5) 

for x in ar:
	lisAux.append(x)
	lisAux.append(x + 1)
	lisAux.append(x +1+1)
	if ar.sequenciaExiste(lisAux):
		listaFinal.append(lisAux)



class classeTeste(unittest.TestCase):
	def testFunc(self):
		self.assertEqual([[1,2,3],[5,6,7],[1,3,5,7,9],[3,6,9],[1,5,9]],calculaProgressao([1,2,3,5,6,7,9]))

if __name__ == '__main__':
	unittest.main()