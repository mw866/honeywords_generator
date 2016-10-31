#!/usr/bin/env python3
import sys
import random
import string

ALPHABET = string.ascii_uppercase + string.ascii_lowercase


def load_file(filename):
	passwds = []
	with open(filename) as f:
		for line in f:
			passwds.append(line.strip())
	return passwds


def generate(realpasswds, top100passwds, n):
	sweetwordsets = []
	for realpasswd in realpasswds:
		sweetwordset = []
		for i in range(n):
			# nothing's done yet
			sweetword = ''
			sweetwordset.append(sweetword)
		sweetwordsets.append(sweetwordset)
	return sweetwordsets


def write_file(sweetwordsets, outFilename):
	with open(outFilename, 'w') as f:
		for sweetwordset in sweetwordsets:
			f.write(','.join(sweetwordset))
			f.write('\n')




def main():
	n = int(sys.argv[1])
	filename = sys.argv[2]
	outFilename = sys.argv[3]

	realpasswds = load_file(filename)
	top100passwds = load_file('top100.txt')

	sweetwordsets = generate(realpasswds, top100passwds, n)
	write_file(sweetwordsets, outFilename)


if __name__ == '__main__':
	main()


