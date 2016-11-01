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


def generate(realpasswds, n):
	''' (List[str], int) -> List[List[str]]
	Usage: To call generate() for one single realpasswd, use
	       sweetword = generate([realpasswd], 1)[0][0]
	       sweetword is the permutation of realpasswd
	'''
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
			
			while sweetword == realpasswd or sweetword in sweetwordset:
#				# if sweetword is repeated, with some probability just generate a random password
#				if random.random() < 0.1:
#					charSet = ALPHABET + string.digits
#					sweetword = ''.join(random.choice(charSet) for _ in range(len(realpasswd)))
#					break
				# recursively call generate() until the sweetword is not in the set and not equal to realpassword
				sweetword = generate([realpasswd], 1)[0][0]
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
	sweetwordsets = generate(realpasswds, n)
	write_file(sweetwordsets, outFilename)


if __name__ == '__main__':
	main()
