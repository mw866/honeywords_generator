#!/usr/bin/env python3
import sys
import random
import string

ALPHABET = string.ascii_uppercase + string.ascii_lowercase

def generate(filename, n):
	realpasswds = []
	with open(filename) as f:
		for line in f:
			realpasswds.append(line.strip())

	sweetwordsets = []
	for realpasswd in realpasswds:
		sweetwordset = []
		# categorize characters into 3 types: char, digit and special char
		for i in range(n):
			charBlock = []
			digitBlock = []
			specialBlock = []
			for char in realpasswd:
				if char in ALPHABET:
					charBlock.append(char)
				elif char in string.digits:
					digitBlock.append(char)
				else:
					specialBlock.append(char)
			# shuffle each block
			random.shuffle(charBlock)
			random.shuffle(digitBlock)
			random.shuffle(specialBlock)
			
			# shuffle the position of each block
			stringBlocks = [charBlock, digitBlock, specialBlock]
			random.shuffle(stringBlocks)
			sweetword = ''.join(stringBlocks[0] + stringBlocks[1] + stringBlocks[2])

			if sweetword == realpasswd or sweetword in sweetwordset:
				# if sweetword is repeated, randomly generate a new one
				if random.choice([True, False]):
					charSet = ALPHABET + string.digits
				else:
					charSet = ALPHABET + string.digits + '!@#$%^&*()'
				sweetword = ''.join(random.choice(charSet) for _ in range(len(realpasswd)))
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
	sweetwordsets = generate(filename, n)
	write_file(sweetwordsets, outFilename)


if __name__ == '__main__':
	main()
