import random
import numpy
l=[ "-","-","-",
   "-","-","-",
    "-","-","-" ]
winner = None
gameRunning = True
currentPlayer=None

def display(l):
    print("-------------") 
    print(f"| {l[0]} | {l[1]} | {l[2]} |" ) 
    print("-------------") 
    print(f"| {l[3]} | {l[4]} | {l[5]} |" )  
    print("-------------")
    print(f"| {l[6]} | {l[7]} | {l[8]} |" )   
    print("-------------") 

def intake():
    opt=input('Choose one "X" or "O" : ')
    while (opt not in "xXoO") or opt=="":
        opt=input('Choose one "X" or "O" : ')
    return opt.upper()

def count(e1,e2,e3,key):
    count=0
    if e1==key:count+=1
    if e2==key:count+=1
    if e3==key:count+=1
    return count

def findEmpty(x,y,z):
    if x=="-":
        return 1
    if y=="-":
        return 2
    if z=="-":
        return 3

def hardcom(l:list,p:str):

    if p=="X":
        p2="O"
    else:
        p2="X"
    
    nothing_happens=True
    # our win'
    while True:
        if count(l[0],l[1],l[2],p) >1 and ("-" in (l[0],l[1],l[2])):
            l[findEmpty(l[0],l[1],l[2])-1]=p
            nothing_happens=False
            break
        if count(l[3],l[4],l[5],p) >1 and ("-" in (l[3],l[4],l[5])):
            l[findEmpty(l[3],l[4],l[5])+2]=p
            nothing_happens=False
            break

        if count(l[6],l[7],l[8],p) >1 and ("-" in (l[6],l[7],l[8])):
            l[findEmpty(l[6],l[7],l[8])+5]=p
            nothing_happens=False
            break

        #columns
        if count(l[0],l[3],l[6],p) >1 and ("-" in (l[0],l[3],l[6])):
            if findEmpty(l[0],l[3],l[6])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[3],l[6])==2:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[3],l[6])==3:
                l[6]=p
                nothing_happens=False
                break
        if count(l[1],l[4],l[7],p) >1 and ("-" in (l[1],l[4],l[7])):
            if findEmpty(l[1],l[4],l[7])==1:
                l[1]=p
                nothing_happens=False
                break
            if findEmpty(l[1],l[4],l[7])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[1],l[4],l[7])==3:
                l[7]=p
                nothing_happens=False
                break
        if count(l[2],l[5],l[8],p) >1 and ("-" in (l[2],l[5],l[8])):
            if findEmpty(l[2],l[5],l[8])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[2],l[5],l[8])==2:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[2],l[5],l[8])==3:
                l[6]=p
                nothing_happens=False
                break

        #diagonals
        if count(l[0],l[4],l[8],p) >1 and ("-" in (l[0],l[4],l[8])):
            if findEmpty(l[0],l[4],l[8])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[4],l[8])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[4],l[8])==3:
                l[8]=p
                nothing_happens=False
                break
        if count(l[3],l[4],l[6],p) >1 and ("-" in (l[3],l[4],l[6])):
            if findEmpty(l[3],l[4],l[6])==1:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[3],l[4],l[6])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[3],l[4],l[6])==3:
                l[6]=p
                nothing_happens=False
                break
        break
    #opposing other win    
    while True:
        #rows
        if count(l[0],l[1],l[2],p2) >1 and ("-" in (l[0],l[1],l[2])):
            l[findEmpty(l[0],l[1],l[2])-1]=p
            nothing_happens=False
            break
        if count(l[3],l[4],l[5],p2) >1 and ("-" in (l[3],l[4],l[5])):
            l[findEmpty(l[3],l[4],l[5])+2]=p
            nothing_happens=False
            break
        if count(l[6],l[7],l[8],p2) >1 and ("-" in (l[6],l[7],l[8])):
            l[findEmpty(l[6],l[7],l[8])+5]=p
            nothing_happens=False
            break

        #columns
        if count(l[0],l[3],l[6],p2) >1 and ("-" in (l[0],l[3],l[6])):
            if findEmpty(l[0],l[3],l[6])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[3],l[6])==2:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[3],l[6])==3:
                l[6]=p
                nothing_happens=False
                break
        if count(l[1],l[4],l[7],p2) >1 and ("-" in (l[1],l[4],l[7])):
            if findEmpty(l[1],l[4],l[7])==1:
                l[1]=p
                nothing_happens=False
                break
            if findEmpty(l[1],l[4],l[7])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[1],l[4],l[7])==3:
                l[7]=p
                nothing_happens=False
                break
        if count(l[2],l[5],l[8],p2) >1 and ("-" in (l[2],l[5],l[8])):
            if findEmpty(l[2],l[5],l[8])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[2],l[5],l[8])==2:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[2],l[5],l[8])==3:
                l[6]=p
                nothing_happens=False
                break

        #diagonals
        if count(l[0],l[4],l[8],p2) >1 and ("-" in (l[0],l[4],l[8])):
            if findEmpty(l[0],l[4],l[8])==1:
                l[0]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[4],l[8])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[0],l[4],l[8])==3:
                l[8]=p
                nothing_happens=False
                break
        if count(l[3],l[4],l[6],p2) >1 and ("-" in (l[3],l[4],l[6])):
            if findEmpty(l[3],l[4],l[6])==1:
                l[3]=p
                nothing_happens=False
                break
            if findEmpty(l[3],l[4],l[6])==2:
                l[4]=p
                nothing_happens=False
                break
            if findEmpty(l[3],l[4],l[6])==3:
                l[6]=p
                nothing_happens=False
                break
        break
    

    if nothing_happens==True:complay(l,p)

def play(l,p:str):

    while True:
        inp=input("Enter the position 1-9 : ")
        while inp not in ["1","2","3","4","5","6","7","8","9"] or inp=="":    
            inp=input("Enter the position 1-9 : ")
        if l[int(inp)-1]!="-":
            print("Already filled")
            continue
        else: break
    if p=="X":
        l[int(inp)-1]="X"
    if p=="O":
        l[int(inp)-1]="O"

def complay(l,p:str):
    pos=random.randint(1,9)
    while l[pos-1]!="-":
        pos=random.randint(1,9)
    if l[pos-1]=="-":
        l[pos-1]=p
    
def check_horizontal(l):
    global winner
    if l[0]==l[1]==l[2] and l[1]!="-":
        winner = l[0]
        return True
    if l[3]==l[4]==l[5] and l[4]!="-":
        winner = l[4]
        return True
    if l[6]==l[7]==l[8] and l[7]!="-":
        winner = l[7]
        return True
    
def check_vertical(l):
    global winner
    if l[0]==l[3]==l[6] and l[3]!="-":
        winner = l[3]
        return True
    if l[1]==l[4]==l[7] and l[4]!="-":
        winner = l[4]
        return True
    if l[2]==l[5]==l[8] and l[5]!="-":
        winner = l[5]
        return True
    
def check_diagonal(l):
    global winner 
    if l[0]==l[4]==l[8] and l[0]!="-":
        winner = l[0]
        return True
    if l[2]==l[4]==l[6] and l[2]!="-":
        winner = l[2]
        return True
    
def check_tie(l):
    if "-" not in l:
        print("Match is draw")
        return True
    else: return False

def swich_players():
    global currentPlayer
    if currentPlayer==player_1:
        currentPlayer=player_2
    elif currentPlayer==player_2:
        currentPlayer=player_1 

if __name__== '__main__':
    n=input("2 players or 1 player (2/1) : ")
    while n not in "12" or n=="":
        n=input("2 players or 1 player (2/1) : ")
    if n=="2":
        print("player 1:")
        player_1=intake()
        player_2=None

        if player_1 =="X":
            player_2="O"
        else:
            player_2="X"
        currentPlayer=player_1
        while gameRunning:
            display(l)
            print(f"'{currentPlayer}' to be played")
            play(l,currentPlayer)

            if check_horizontal(l) or check_vertical(l) or check_diagonal(l):
                gameRunning=False
                break
            if check_tie(l):
                gameRunning=False
                break
            swich_players()
        
        display(l)
        print(f"'{winner} is winner!!!'")
    if n=="1":
        hardness=input("choose hardness \n1.easy\n2.mediunm\n3.hard : ")
        while n not in "12" or n=="":
            hardness=input("choose hardness \n1.easy\n2.mediunm\n3.hard : ")
        print("player 1:")
        player_1=intake()
        player_2=None

        if player_1 =="X":
            player_2="O"
        else:
            player_2="X"
        currentPlayer=player_1

        while gameRunning:
            display(l)
            print(f"'{player_1}' to be played")
            play(l,player_1)
            display(l)
            if check_horizontal(l) or check_vertical(l) or check_diagonal(l):
                gameRunning=False
                break
            if check_tie(l):
                gameRunning=False
                break
            print(f"'{player_2}' to be played")
            if hardness=="3":
                hardcom(l,player_2)
            elif hardness == "2":
                temp=numpy.random.randint(1,3,30)
                if random.choice(temp) =="1":
                    complay(l,player_2)
                else:hardcom(l,player_2)
            elif hardness=="1":
                complay(l,player_2)
            if check_horizontal(l) or check_vertical(l) or check_diagonal(l):
                gameRunning=False
                break
            if check_tie(l):
                gameRunning=False
                break

        display(l)
        print(f"'{winner} is winner!!!'")