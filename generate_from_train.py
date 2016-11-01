
import random
import sys
import string
import generate_from_empty

def make_password_like_howard(real):
    return generate_from_empty.generate(real)


def read_infile(filename):
    infile_list = [ ]
    lines = open(filename,"r").readlines()
    for line in lines:
        infile_list.extend( line.split() )
    return infile_list

 #[chris] To prove the original noise generator by using disctionaries link: https://wiki.skullsecurity.org/Passwords

def make_sweet(real, train_list): # make a random password like those in given password list
    if real in train_list:
        sweet = random.choice(train_list)
    else:
        sweet = make_password_like_ari(real, train_list)
    return sweet

def generate_sweet_dict( n, real_list, train_list):
    sweet_dict = {}
    for real in real_list:
        sweet_list = []
        for t in range( n ):
            sweet = make_sweet(real, train_list)
            sweet_list.append( sweet )
        sweet_dict[real]=sweet_list

    return sweet_dict

def main():
    if len(sys.argv) < 5 :
        print('Arguments: [number of sweets per real] [input-real filename] [output-sweet filename] [train_filename]')
    n = int(sys.argv[1])     # get number of passwords desired
    real_filename = sys.argv[2]    
    sweet_filename = sys.argv[3] 
    train_filename = sys.argv[4] 

    real_list = read_infile(real_filename)
    train_list = read_infile(train_filename)
    sweet_dict = generate_sweet_dict(n, real_list, train_list)     # generate passwords
    #random.shuffle(sweet_dict)     # shuffle their order

    print("Real Password\t\tSweet Passwords")
    for real, sweet_list in sweet_dict.items():
        print real, '\t\t', sweet_list
    #<TODO> Export to outputfile
main()

