#_*_ coding: utf-8 _*_

import unittest

def multiply(x,y):
	return reduce(lambda a, b: a + x, range(y), 0)
	'''result = 0
	for i in range(y):
		result += x
	return result'''

class MultiplicationTest(unittest.TestCase):
	def test_simple(self):
		self.assertEqual(6, multiply(3,2))
		#self.assertEqual(9, multiply(3,3))


if __name__ == '__main__':
	unittest.main()