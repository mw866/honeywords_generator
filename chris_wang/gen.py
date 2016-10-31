##############################################################################
#### PARAMETERS CONTROLLING PASSWORD GENERATION (aside from password files)

tn = 0.08            # probability that a generated password is a ``tough nut''
                     # (password of length 40 of random chars)
                     # otherwise following parameters apply

# probabilities p1, p2, p3 add up to 1 (heuristically chosen)
p1 = 0.10            # chance of a "random" char at this position (see code)
p2 = 0.40            # chance of a markov-order-1 char at this position (see code)
p3 = 0.50            # choice of continuing copying from same word

q = 0.03             # add 3% noise words to list of passwords

# syntax parameters for a password
nL = 0               # password must have at least nL letters
nD = 0               # password must have at least nD digit
nS = 0               # password must have at least nS special (non-letter non-digit)

#### END OF PARAMETERS CONTROLLING PASSWORD GENERATION
##############################################################################

import random
import sys
import string

def make_password_like_ari(real, train_list):
    #make a random password like those in given password list
    if random.random() < tn:
        return tough_nut()
    # start by choosing a random password from the list
    # save its length as k; we'll generate a new password of length k
    #k = len(real)
    # create list of all passwords of length k; we'll only use those in model
    L = [ pw for pw in train_list if len(pw) == len(real) ]
    nL = len(L)
    # start answer with the first char of that random password
 
    row = random.randrange(nL)    # index of random password being used 
    ans = L[row][:1]                  # copy first char of L[row] 
    j = 1                             # j = len(ans) invariant
    while j < len(real):              # build up ans char by char
        p = random.random()           # randomly decide what to do next, based on p
        #  p1 = prob of action 1, p2 = prob of action 2, p3 = prob of action 3
        #  p1 + p2 + p3 = 1.00
        if p<p1:
            action = "action_1"
        elif p<p1+p2:
            action = "action_2"
        else:
            action = "action_3"
        if action == "action_1":
            # add same char that some random word of length k has in this position
            row = random.randrange(nL)
            ans = ans + L[row][j]
            j = j + 1
        elif action == "action_2":
            # take char in this position of random word with same previous char
            LL = [ i for i in range(nL) if L[i][j-1]==ans[-1] ]
            row = random.choice(LL)
            ans = ans + L[row][j]
            j = j + 1
        elif action == "action_3":
            # stick with same row, and copy another character
            ans = ans + L[row][j]
            j = j + 1
    if (nL > 0 or nD > 0 or nS > 0) and not syntax(ans): 
        return make_password_like_ari(real, train_list)
    return ans

def tough_nut():
    """
    Return a ``tough nut'' password
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    nchars = len(chars)
    w = [ ]
    k = 40
    for j in range(k):
        w.append(chars[random.randrange(nchars)])
    w = ''.join(w)
    return w

def syntax(p):
    """
    Return True if password p contains at least nL letters, nD digits, and nS specials (others)
    """
    global nL, nD, nS
    L = 0
    D = 0
    S = 0
    for c in p:
        if c in string.ascii_letters:
            L += 1
        elif c in string.digits:
            D += 1
        else:
            S += 1
    if L >= nL and D >= nD and S >= nS:
        return True
    return False
#===End From the origianl gen.py by Ari and Ron===

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
    #random.shuffle(sweet_list)     # shuffle their order

    print("Real Password\t\tSweet Passwords")
    for real, sweet_list in sweet_dict.items():
        print real, '\t\t', sweet_list
    #<TODO> Export to outputfile
main()

