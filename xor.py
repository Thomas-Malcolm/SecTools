#!/usr/bin/python

from itertools import izip, cycle
import sys

def help():
	print("usage: xor.py [key] [message]")
	print("use plaintext ascii strings")
	exit()

def main():

	if len(sys.argv) != 3:
		help()

	key = sys.argv[1]
	msg = sys.argv[2]

	decoded = ''.join(chr(ord(let) ^ ord(k)) for (let,k) in izip(msg, cycle(key)))

	print("Decoded (space after ':')")
	print("As str: {}".format(decoded.encode('utf8')))
	print("As hex: {}".format(decoded.encode('hex')))
	print("As b64: {}".format(decoded.encode('base64')))


if __name__ == "__main__":
	main()
