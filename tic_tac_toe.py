positionArray = [1,2,3,4,5,6,7,8,9]  # initial array
current = 'X'
win = 0
 # setting board display
def setBoard():    
    print("\t\t|\t\t|\t\t\n\t{}\t|\t{}\t|\t{}\t".format(positionArray[0],positionArray[1],positionArray[2]))
    print("----------------------------------------------------")
    print("\t\t|\t\t|\t\t\n\t{}\t|\t{}\t|\t{}\t".format(positionArray[3],positionArray[4],positionArray[5]))
    print("----------------------------------------------------")
    print("\t\t|\t\t|\t\t\n\t{}\t|\t{}\t|\t{}\t".format(positionArray[6],positionArray[7],positionArray[8]))
    if win == 0:
        getPosition()
    
def initialize():
    global current
    print("Player 1 enter X or O")
    player = input()
    if player.upper() == 'X':
        players = {'O': 'Player 2', 'X': 'Player 1'}
        current = 'X'
    else:
        players = {'O': 'Player 1' , 'X' : 'Player 2'}
        current = 'O'
    print("O for {} \nX for {}".format(players['O'],players['X'])) 
    setBoard()

    

def getPosition():
    print("Enter the position you want to place your text. Ex - 1,2... 9 ")
    pos = int(input())
    if(pos > 9 or pos < 1):
        print("Please enter a number between 1 to 9")
    else:
        checkWin(pos)

def checkWin(pos):
    global current
    global positionArray
    global win
    

    if positionArray[pos-1] == 'X' or positionArray[pos-1] == 'O':
        print("Position already taken. Please select some other position")
        setBoard()
    else:
        positionArray[pos-1] = current
        checkDraw =  [num for num in positionArray if num == 'X' or num == 'O']
        
        if positionArray[0] == current and positionArray[1] == current and positionArray[2] == current or positionArray[3] == current and positionArray[4] == current and positionArray[5] == current or positionArray[6] == current and positionArray[7] == current and positionArray[8] == current or positionArray[0] == current and positionArray[3] == current and positionArray[6] == current or positionArray[1] == current and positionArray[4] == current and positionArray[7] == current or positionArray[2] == current and positionArray[5] == current and positionArray[8] == current  or positionArray[0] == current and positionArray[4] == current and positionArray[8] == current or positionArray[2] == current and positionArray[4] == current and positionArray[6] == current:
            print("Player {} wins. Congratulations to the winner !!!".format(current))
            win = 1
            setBoard()
        elif len(checkDraw) == len(positionArray):
            print("Sorry! we have no winner for this match")
            win = 1
            setBoard()
        else:    
            if current == 'X':
              current = 'O'
            else:
              current = 'X'
            setBoard()    

            
   
    
initialize()        