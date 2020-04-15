#!/usr/bin/python3

import numpy
import sys

a = [2, 3, 5]
n = [5, 11, 17]

def help():
	print("usage: ch_rem.py [a1] [n1] [a2] [n2] ...")
	exit()

def mod_inv(x,y):
	# ax + my = 1 = gcd(x, y)
	# ax = 1 (mod y)

	a, a_last = 0, 1
	r, r_last = y, x

	while r != 0:
		q = r_last // r
		
		r_new = r_last - q*r
		r_last = r
		r = r_new

		a_new = a_last - q*a
		a_last = a
		a = a_new

	return y + a_last

def chn_remainder(a, n):
	# x = a_1 (mod n_1), x = a_2 (mod n_2), ...
	# x = a (mod) N
	# a = (N_1 * a_1 * a_1_inverse) + (N_2 * a_2 * a_2_inverse) + ... (mod N)

	final = 0

	N = int(numpy.product(n))

	for i,x in enumerate(a):
		N_i = N / n[i]

		a_inv = mod_inv(N_i, x)

		final += N_i * x * a_inv
	
	return int(final % N), N

def main():

	if len(sys.argv) < 3 or len(sys.argv[1:]) % 2 != 0:
		help()

	a = []
	n = []
	arr = sys.argv[1:]

	try:
		for i,x in enumerate(sys.argv[1:]):
			a.append(int(x)) if (i % 2 == 0) else n.append(int(x))
	except:
		help()

	if len(a) != len(n):
		help()

	result, N = chn_remainder(a, n)
	print("REM : x = {} (mod {})".format(result, N))

main()