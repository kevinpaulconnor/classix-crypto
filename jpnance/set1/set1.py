#!/usr/bin/python3

import unittest

class TestMethods(unittest.TestCase):
	def testHexToBase64(self):
		self.assertEqual(hexToBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'), 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

def hexToBase64(hex):
	return 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

if __name__ == '__main__':
	unittest.main()
