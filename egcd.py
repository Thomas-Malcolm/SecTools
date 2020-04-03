#!/usr/bin/python

import sys

def help():
	print("usage: egcd.py [a] [b]")
	exit()

def egcd(x,y):
	# ax + by = gcd(x,y)
	a, a_last = 0, 1
	b, b_last = 1, 0	
	r, r_last = y, x

	while r != 0:
		q = r_last // r
		
		r_new = r_last - q*r
		r_last = r
		r = r_new

		a_new = a_last - q*a
		a_last = a
		a = a_new

		b_new = b_last - q*b
		b_last = b
		b = b_new

	print("GCD  : {}*{} + {}*{} = {}".format(a_last, x, b_last, y, r_last))
	print("ZERO : {}*{} + {}*{} = {}".format(a, x, b, y, r))

def main():

	if len(sys.argv) != 3:
		help()

	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except:
		help()

	egcd(a, b)

if __name__ == "__main__":
	main()
