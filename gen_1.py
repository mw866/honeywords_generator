#!/usr/bin/env python3
'''
Strategy for generate_from_empty.py:
- loop through the input real passwords
- seperate them into 3 categories: char, digit, special
- with some randomness, lower/upper case the character
- with some randomness, substitute the digit with random digit
- shuffle each block
- shuffle block position
- if sweetword exists in the generated set or equal to real password,
  run the same procedure again
'''

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
					#if random.random() < 0.2:
					#	char = char.lower()
					#elif random.random() < 0.1:
					#	char = char.upper()
					charBlock.append(char)
				elif char in string.digits:
					# with some probabilities to change char to random digit
					#if random.random() < 0.8:
						#digitBlock.append(char)
					#else:
			
					digitBlock.append(random.choice(list('0123456789')))
				else:
					specialBlock.append(char)

			#make digit block randomly 1234
			if random.random() < 0.7:
				nineties = ['19']
				nineties.append(random.choice(list('0123456789')))
				nineties.append(random.choice(list('0123456789')))
			
				twenties = ['20']
				twenties.append(random.choice(list('01')))
				twenties.append(random.choice(list('0123456789')))

				digitBlock = random.choice([['1234'],['666'], ['1'], ['2'], ['123'],['69'], ['321'], ['000'], nineties, twenties])

			#totally strip digits 15% of the time, but less so when the real password doesn't have digits
			if digitBlock and random.random() < 0.15:
				digitBlock = ['']
			elif not digitBlock and random.random() < 0.05:
				digitBlock = ['']


			#lowercase entire password
			if charBlock and random.random() < 0.2:
				charBlock = [char.lower() for char in charBlock]

			#flip capitalization of first letter
			if charBlock and random.random() < 0.5:
				charBlock = [char.lower() for char in charBlock]
				charBlock[0] = charBlock[0].upper()

			#Randomly shuffle the special characters
			random.shuffle(specialBlock)
			
			# shuffle the position of each block with given probability
			stringBlocks = [charBlock, digitBlock, specialBlock]
			#if random.random() < 0.7:
			#	random.shuffle(stringBlocks)
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
