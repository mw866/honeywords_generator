
import sys
import generate_from_train

def main():
	print('Scenario 2. T is the set of the 100 most common RockYou passwords.')
	#print('Usage: [number of sweets per real] [input-real filename] [output-sweet filename] ')
	n = int(sys.argv[1])     # get number of passwords desired
	real_filename = sys.argv[2]    
	sweet_filename = sys.argv[3] 
	train_filename = 'top100.txt'  
	generate_from_train.generate(n ,real_filename, sweet_filename, train_filename)

main()	