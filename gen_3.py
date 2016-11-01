
import sys
import generate_from_train

def main():
	print('Scenario 3. T is the set of the full RockYou passwords.')
	print('Usage: [number of sweets per real] [input-real filename] [output-sweet filename] ')
	n = int(sys.argv[1])     # get number of passwords desired
	real_filename = sys.argv[2]    
	sweet_filename = sys.argv[3] 
	train_filename = 'full.txt'  
	generate_from_train.generate(n ,real_filename, sweet_filename, train_filename)

main()	