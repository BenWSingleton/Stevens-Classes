#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens Honor System

# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("I lost...WAIT! That can't be right. You won, how did you win, I always win?")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("I win ... AGAIN")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles  
    while True:
        try:
            num_piles=int(input("How many piles do you want to play with?"))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            break
    piles=[0]*num_piles
    for n in range(len(piles)):
        while True:
            try:
                print("How many in pile ", n, "?")
                piles[n]=int(input())
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                break
        
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    for n in range(num_piles):
        print("piles ", n, " = ", piles[n])


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    while True:
        try:
            user_Choice = int(input("Which pile?"))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            if piles[user_Choice]==0:
                print("Already empty. Try again.")
            else:
                if 0<= user_Choice <len(piles):
                    break
                else:
                    print("Out of range. Try again.")
    return user_Choice
                              


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    while True:
        try:
            user_Remove=int(input("How many?"))
        except ValueError:
            print("Not an integer! Try again.")
        else:
            if 1<= user_Remove <=piles[pnum]:
                break
            else:
                print("Out of range. Try again.")
    return user_Remove


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 
    nim_sum=piles[0]
    for n in range(1,num_piles):
        nim_sum=nim_sum^piles[n]
    return nim_sum

    
def opt_play():
    """ Return (p,n) where p is the pile number and n is the amountt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    pile=0
    num=0
    nim_sum=game_nim_sum()
    pile_sum=0
    #pile_sums=[0]*num_piles
    for i in range(num_piles):
        pile_sum=nim_sum^piles[i]
        if pile_sum<piles[i]:
            pile=i
            num=abs(piles[i]-pile_sum)
            return (pile,num)
    for i in range(num_piles):
        if piles[i]>0:
            pile=i
            return (pile,1)
        

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    (pile,num)=opt_play()
    pileToTakeFrom=pile
    amount=num
    piles[pileToTakeFrom] -= amount
    #piles[pile]=abs(piles[pile]-num)
    print("My turn ... prepare to be dazzled!!!")
    print("I remove ", num, " from pile ", pile)
    


#   start playing automatically
if __name__ == "__main__" : play_nim()
