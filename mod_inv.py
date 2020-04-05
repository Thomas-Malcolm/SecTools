#!/usr/bin/python

import sys

def help():
	print("usage: mod_inv.py [g] [m]")
	print("       g * d = 1 (mod m)")
	exit()

def mod_inv(g, m):
	# ag + bm = 1 = gcd(g, m)
	# ag = 1 (mod m)

	a, a_last = 0, 1
	r, r_last = m, g

	while r != 0:
		q = r_last // r
		
		r_new = r_last - q*r
		r_last = r
		r = r_new

		a_new = a_last - q*a
		a_last = a
		a = a_new

	inv = a_last % m

	print("INVERSE: {}".format(inv))
	print("{} * {} = 1 (mod {})".format(g, inv, m))

def main():

	if len(sys.argv) != 3:
		help()

	try:
		a = int(sys.argv[1])
		b = int(sys.argv[2])
	except:
		help()

	mod_inv(a, b)

if __name__ == "__main__":
	main()
