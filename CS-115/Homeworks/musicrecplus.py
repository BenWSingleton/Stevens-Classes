#Benjamin Singleton
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *
import operator
import collections

#ADD
#DOCSTRINGS

#DATA_FILE="musicrecplus.txt"

debug = False

NAME = ""
ARTIST=[]
DATA_BASE={}

#Works
def menu():
    """Display options to user and gives them certain functions depending on what they enter"""
    if debug: print("[DEUBG: Entering Menu]")
    route=input("Enter a letter to choose an option: \ne - Enter preferences \nr - Get recommendations \np - Show most popular artists \nh - How popular is the most popular \nm - Which user has the most likes \nq - Save and quit\n")
    if route=="e":enter(True) #Works
    elif route=="r":
        if debug: print("[DEBUG: Running getRecommendations() to display recommendations]")
        getRecommendations()
    elif route=="p":
        if debug: print("[DEBUG: Running popular() to display most popular artist(s)]")
        popular() #Works
    elif route=="h":
        if debug: print("[DEBUG: Running howPopular() to display most popular is the most popular artist]")
        howPopular() #Works
    elif route=="m":
        if debug: print("[DEBUG: Running mostLikes() to display the user with the most likes]")
        mostLikes()  #works
    elif route=="q":
        if debug: print("[DEBUG: Running SaveQuit() to save the data in musicrecplus.txt]")
        SaveQuit(NAME, ARTIST, DATA_BASE, "musicrecplus.txt") #Works
    elif route=="t":
        popList()
    else:
        print("Invalid Input")
        menu() #Works

#Works       
def enter(entering):
    """User enters the arists they like which will replace what
    they already have in the database"""
    if debug: print("[DEBUG: Adding new user data]")
    if entering==False:
        ARTIST.clear()
    artist=input("Enter an artist that you like (Enter to finish):")
    if artist != "":
        ARTIST.append(artist)
        enter(True)
    else:
        ARTIST.sort()
        DATA_BASE[NAME]=ARTIST
        menu()

def getRecommendations():
    ''' Gets recommendations for a user (currUser) based
        on the users in userMap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.  '''
    bestUser = findBestUser() #Works
    if bestUser==0:
        print("Sorry no matches")
        menu()
    #print(DATA_BASE[NAME])
    #print(bestUser)
    #print(DATA_BASE[bestUser])
    #print("List1:", DATA_BASE[bestUser])
    #print("List2:", DATA_BASE[NAME])
    recommendations = drop(DATA_BASE[bestUser], DATA_BASE[NAME])
    print(recommendations)
    menu()

#"Works"
def findBestUser():
    ''' Find the user whose tastes are closest to the current
        user.  Return the best user's name (a string) '''
    bestUser=None
    bestScore=0
    users=[]
    #for user in DATA_BASE:
    #    if user!=NAME:
    #        users.append(user)
    for user in DATA_BASE:
        if user!=NAME:
            if user[-1]!="$":
                score=numMatches(DATA_BASE[NAME], DATA_BASE[user])
                #print("score:", score)
                if score > bestScore:
                    #print(bestScore)
                    bestScore=score
                    bestUser=user
                    #print(user)
    bestScore2=0
    bestUser2=None
    if DATA_BASE[bestUser]==DATA_BASE[NAME]:
        for user in DATA_BASE:
            if user!=NAME:
                if user[-1]!="$":
                    if user!=bestUser:
                        score=numMatches(DATA_BASE[NAME], DATA_BASE[user])
                        if score>bestScore2:
                            bestScore2=score
                            bestUser2=user
        bestUser=bestUser2
    return bestUser

#"Works"
def numMatches( list1, list2 ):
    ''' return the number of elements that match between
        two sorted lists '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def drop(list1, list2):
    ''' Return a new list that contains only the elements in
        list2 that were NOT in list1. '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3

def Sort_Tuple(tup):
    """Sorts a list of tuples by their second item"""
    lst = len(tup)  
    for i in range(0, lst):  
        for j in range(0, lst-i-1):  
            if (tup[j][1] < tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp
    return tup 

#Works
def getArtists():
    """Returns a dictionary containing the amount of times that each artist appears"""
    if debug: print("[DEBUG: Starting getArtists()]")
    freq={}
    result={}
    allArtists=[]
    for users in DATA_BASE:
        if users[-1]!="$":
            allArtists+=DATA_BASE[users] #A list of all artists seperated by ', '
    for arts in allArtists:
        if arts in freq:
            freq[arts]+=1
        else:
            freq[arts]=1
    freq_list=[(k,v) for k, v in freq.items()]
    freq_list=Sort_Tuple(freq_list)
    return freq_list

#Works
def popular():
    """Cals up getArtists() to obtain the most popular Artist and displays the amount of likes"""
    if debug: print("[DEBUG: Starting popular()]")
    lst=getArtists()
    if len(lst)==0:
        print("Sorry, no artists found.")
        menu()
    #print(lst)
    maxNum=lst[0][1]
    #print(maxNum)
    mostPops=[]
    #print(mostPops)
    #print(range(len(lst)))
    for arts in range(len(lst)):
        if lst[arts][1]==maxNum:
            mostPops.append(lst[arts][0])
    mostPops.sort()
    print(mostPops)
    menu()

#Work
def howPopular():
    """Returns how popular is the most popular artists or artists as an integer"""
    if debug: print("[DEBUG: Starting howPopular()]")
    lst=getArtists()
    if len(lst)==0:
        print("Sorry, no artists found.")
        menu()
    return print(lst[0][1])
    menu()

#Works
def mostLikes():
    """Prints full name of user who likes the most artists"""
    most=0
    result=[]
    for users in DATA_BASE:
        if users[-1]!="$":
            #if debug: print("[DEBUG: mostLikes() loop]")
            if len(DATA_BASE[users])>most:
                result.clear()
                result.append(users)
                most=len(DATA_BASE[users])
            elif len(DATA_BASE[users])==most:
                result.append(users)
    if result==[]:
        print("Sorry, no user found.")
    else:
        result.sort()
    print(result)
    menu()

#"Works" but bug if two users have the same preferences
def SaveQuit(name, artists, database, text_file):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    database[name]=artists
    file = open("musicrecplus.txt", "w")
    for user in database:
        toSave = str(user) + ":" + ",".join(DATA_BASE[user]) +"\n"
        file.write(toSave)
    file.close()

#Works
if __name__=='__main__':
    """Prompts the user for their name. If they are in the database, sends them to the menu.
    If they aren't in the database, enters their name and prompts them for artists to load
    into the database. Routes user to menu once done entering artists"""
    NAME = input('Enter your name (put a $ symbol after your name if you wish your preferences to remain private):').strip()
    try:
        file=open("musicrecplus.txt", "r")
        users=[]
        #file.write(name)
        for line in file:
            user, artists=line.split(":")
            #print(user)
            artists=artists.split(",")
            arts = []
            for x in artists:
                arts.append(x.strip())
            DATA_BASE[user]= arts
            users.append(user)
        if NAME in DATA_BASE:
            if debug: print("[DEBUG: Using existing user]")
            ARTIST = DATA_BASE[NAME]
            menu()
        else:
            enter(False)     
    except IOError as error:
        print("!!IOError as error!!")
        file=open("musicrecplus.txt", "w")
        file.close()
        enter(False)
