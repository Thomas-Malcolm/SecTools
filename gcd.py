#!/usr/bin/python

import sys

def help():
	print("usage: gcd [a] [b]")
	exit()

def gcd(a, b):

	if b == 0:
		return a

	return gcd(b, a % b)

def main():

	if len(sys.argv) != 3:
		help()

	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except:
		help()

	gcd_val = gcd(a, b)

	print("gcd({},{}) = {}".format(a, b, gcd_val))

if __name__ == "__main__":
	main()