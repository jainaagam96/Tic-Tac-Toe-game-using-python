import os
clear = lambda: os.system('cls')
print("                                 LETS    PLAY    TIC   TAC   TOE                         \n")
print("Note: 1,2,3,4,5,6,7,8,9 are position no.\n")
while True:
    List=[1,2,3,4,5,6,7,8,9]
    def check(p):
        if List[0]==p and List[1]==p and List[2]==p:
            return True
        if List[3]==p and List[4]==p and List[5]==p:
            return True
        if List[6]==p and List[7]==p and List[8]==p:
            return True
        if List[0]==p and List[3]==p and List[6]==p:
            return True
        if List[1]==p and List[4]==p and List[7]==p:
            return True
        if List[2]==p and List[5]==p and List[8]==p:
            return True
        if List[0]==p and List[4]==p and List[8]==p:
            return True
        if List[2]==p and List[4]==p and List[6]==p:
            return True       
    def display():
        print(" --- --- ---")
        print("|   |   |   |")
        print(f"| {List[0]} | {List[1]} | {List[2]} |")
        print("|   |   |   |")
        print(" --- --- ---")
        print("|   |   |   |")
        print(f"| {List[3]} | {List[4]} | {List[5]} |")
        print("|   |   |   |")
        print(" --- --- ---")
        print("|   |   |   |")
        print(f"| {List[6]} | {List[7]} | {List[8]} |")
        print("|   |   |   |")
        print(" --- --- ---")
        print()
    display()
    j=0
    count=0
    print("enter 'x' to choose 'x' for player 1 or 'o' to choose 'o' for player 1") 
    while True:
        player1=input()
        if player1=='x' or player1=='o':
            break
        else:
            print("invalid input!!!")        
    player2=''
    if player1 == 'x':
        player2='o'
    else:
        player2='x'
    print("HERE WE GO")
    print(f"1st player chooses {player1} and 2nd player chooses  {player2}")
    while List[8]==9:
        List[j]=' '
        j+=1    
    player=1
    print()
    count1=0
    while True:
        player_number=1
        print(f"player {player}'s turn....")
        print("enter position no. to input your character\n")
        pos=int(input())
        if pos not in range(1,10):
            print("invalid input!!!")
            continue
        if List[pos-1]=='x' or List[pos-1]=='o' :
            print("invalid input")
            continue
        else:
            if player%2!=0:
                List[pos-1]=player1
                count+=1
                player_number=1
                player+=1
                print()
                clear()
                display()
            else:
                List[pos-1]=player2
                count+=1
                player_number=2
                player-=1
                print()
                clear()
                display()
        if count>=5:
            if player_number==1:
                if check(player1)==True:
                    count1+=1
                    print(f">>>>>>>>congratulations!!! player {player_number} won")
                    break
            else:
                if check(player2)==True:
                    count1+=1
                    print(f">>>>>>>>congratulations!!!  player {player_number} won")
                    break
        if count==9:
            break
    if count1==0:
        print("Oh!!! Game is Draw\n")
    print("if you want to play again enter 'y' else enter 'n'")
    choice=input()
    if choice=='y':
        continue
    else:
        break
