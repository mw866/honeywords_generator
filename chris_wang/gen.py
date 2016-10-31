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


def read_infile(filename):
    infile_list = [ ]
    lines = open(filename,"r").readlines()
    for line in lines:
        infile_list.extend( line.split() )
    return infile_list

 #[chris] To prove the original noise generator by using disctionaries link: https://wiki.skullsecurity.org/Passwords

def make_password(real_list, train_list): # make a random password like those in given password list
    for real_pw in real_list:
        if real in real_list:
            sweet = random.choice(train_list)
        else:
            sweet = make_password_like_ari(real_list)
    return sweet_list

def generate_sweet( n, real_list, train_list):
    ans = [ ]
    for t in range( n ):
        pw = make_password(real_list, train_list)
        ans.append( pw )
    return ans

def main():
    n = int(sys.argv[1])     # get number of passwords desired
    real_filename = sys.argv[1]    
    sweet_filename = sys.argv[2] 
    train_filename = sys.argv[3] 

    real_list = read_infile(real_filename)
    train_list = read_infile(train_filename)
    sweet_list = generate_sweet(n, real_list, train_list)     # generate passwords
    random.shuffle(sweet_list)     # shuffle their order

    printing_wanted = True     # print if desired
    if printing_wanted:
        for sweet in sweet_list:
            print (sweet)

main()

def make_password_like_ari(pw_list):
    """ 
    make a random password like those in given password list
    """
    if random.random() < tn:
        return tough_nut()
    # start by choosing a random password from the list
    # save its length as k; we'll generate a new password of length k
    k = len(random.choice(pw_list))
    # create list of all passwords of length k; we'll only use those in model
    L = [ pw for pw in pw_list if len(pw) == k ]
    nL = len(L)
    # start answer with the first char of that random password
    # row = index of random password being used 
    row = random.randrange(nL)
    ans = L[row][:1]                  # copy first char of L[row] 
    j = 1                             # j = len(ans) invariant
    while j < k:                      # build up ans char by char
        p = random.random()           # randomly decide what to do next, based on p
        # here p1 = prob of action 1
        #      p2 = prob of action 2
        #      p3 = prob of action 3
        #      p1 + p2 + p3 = 1.00
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
        return make_password(pw_list)
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
