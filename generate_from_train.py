
import random
import sys
import string
import gen_1


def read_infile(filename):
    infile_list = [ ]
    lines = open(filename,"r",errors='ignore').readlines()
    for line in lines:
        infile_list.extend( line.split() )
    return infile_list

def generate_sweet_dict( n, real_list, train_list):
    sweet_dict = {}
    for real in real_list:
        sweet_list = []
        if real in train_list: #pick from the train list
            i = 1
            while i <= n:
                sweet = random.choice(train_list)
                if sweet != real:
                    sweet_list.append(sweet)
                    i = i + 1
            sweet_dict[real]=sweet_list           
        else: #generate from emtply train
            sweet_list = gen_1.generate([real], n)[0]
            sweet_dict[real] = sweet_list
    return sweet_dict

def write_file(sweet_dict, sweet_filename):
    with open(sweet_filename, 'w') as f:
        for real, sweet_list in sweet_dict.items():
            f.write(','.join(sweet_list))
            f.write('\n')

def generate(n ,real_filename, sweet_filename, train_filename):
    real_list = read_infile(real_filename)
    train_list = read_infile(train_filename)
    sweet_dict = generate_sweet_dict(n, real_list, train_list)     # generate passwords

    #random.shuffle(sweet_dict)     # shuffle their order

    print("Real Password\t\tSweet Passwords")
    for real, sweet_list in sweet_dict.items():
        print(real, '\t\t', sweet_list)
    
    write_file(sweet_dict, sweet_filename)
