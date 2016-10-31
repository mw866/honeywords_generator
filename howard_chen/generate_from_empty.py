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
					# with some probabilities to change char to lower/upper
					if random.random() < 0.2:
						char = char.lower()
					elif random.random() < 0.1:
						char = char.upper()
					charBlock.append(char)
				elif char in string.digits:
					# with some probabilities to change char to random digit
					if random.random() < 0.8:
						digitBlock.append(char)
					else:
						digitBlock.append(random.choice(list('0123456789')))
				else:
					specialBlock.append(char)
				
			# shuffle each block
			if random.random() < 0.1:
				random.shuffle(charBlock)
			# if p set too low for digitBlock shuffling, it's likely to produce repeated sweetword
			if random.random() < 0.85:
				random.shuffle(digitBlock)
			random.shuffle(specialBlock)
			
			# shuffle the position of each block with given probability
			stringBlocks = [charBlock, digitBlock, specialBlock]
			if random.random() < 0.7:
				random.shuffle(stringBlocks)
			sweetword = ''.join(stringBlocks[0] + stringBlocks[1] + stringBlocks[2])
			
			if sweetword == realpasswd or sweetword in sweetwordset:
				# if sweetword is repeated, randomly generate a new one
				if random.random() < 0.85:
					charSet = ALPHABET + string.digits
				else:
					charSet = ALPHABET + string.digits + '!@#$%&*'
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
