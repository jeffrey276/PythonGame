import random
import turtle as t

class Explorer:
    sword = 0
    diam = 0
    pos = 0
    def __init__(self, Name, HP):
        self.name = Name
        self.hp = HP

#==========================================================================================


def biomeDraw(fillColor):       # Turtle function to draw an individual biome
        t.fillcolor(fillColor)
        t.begin_fill()
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.end_fill()
        t.forward(70)

def playerDraw():           # Turtle function to draw the player 
        t.fillcolor("red")
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        
def drawBoard():            # Turtle function to draw the entire board
        t.penup()
        t.forward(-300)
        t.pendown()
        for i in range(4):        ##This is when a catastrophe happens, biome gets deleted
            biomeDraw("blue")
            biomeDraw("red")
        t.home()
    
#==========================================================================================
def convert_2_to_10(binary_as_list):
    return int("".join(map(str, binary_as_list)),2)

def read_string_list_from_file(the_file):
    fileRef = open(the_file,"r")
    List=[]
    for line in fileRef:
        string = line[0:len(line)-1]
        List.append(string)
    fileRef.close()
    return List


def create_lists_board(listStrings):
    i = 0
    List = []
    for s in listStrings:
            h = s.find("-")
            h2 = s.find("-",h+1)
            Diam = int(s[0:h]) #This is the number of diamonds#
            Sword = int(s[h+1:h2]) #This is the material of sword#
            Enemy = int(s[h2+1:len(s)]) #This is the number of enemy#
            List.append([i,Diam,Sword,Enemy])
            i+=1
    return List


def show_board(mssg,Locallist,player_pos=None,PythonShine=None):
    print "\nShowing board... " + mssg 
    print "\n The board at this point contains..."

    fmat = "{0:6} {1:6} {2:6} {3:1}" ##format
    print fmat.format("Biome#", "Diam", "Sword", "Enemy")
    
    for l in Locallist:
            i = l[0]
            Diam = l[1]
            Sword = l[2]
            Enemy = l[3]
            Output = fmat.format(str(i),str(Diam),str(Sword),str(Enemy))
            if PythonShine == i:
                Output += " <===PythonShine"
            if player_pos == i:
                Output += " <---Player"
            print Output
            i+=1


def show_player(mssg,player):
    print "\nShowing Player... " + mssg
    print "\nThe player " + player.name
    print "currently has: " + str(player.hp) + " life points"
    if player.sword == 0:
        print "has no sword"
    else:
        print "has a sword of material: " + str(player.sword)
    print "has " + str(player.diam) + " diamonds"
    print "is in the position: " + str(player.pos)
    if player.hp > 0:
        print "So... he is... Very alive!!!"
    else:
        print "So... he is... Dead... oh no!!!"

def List2Str(list_or_iterator):
    return "[" + ", ".join( str(x) for x in list_or_iterator) + "]"


#=============================================================================
print " Welcome to the Survival and Surprises CMPT 120 Games!"
print "======================================================\n"
totalgames = 0
win = 0
board = ""
play = ""


while board.lower() != 'y' and board.lower() != 'n':
    board = raw_input("\nDo you want to draw the board? (y/n): ")
    if board == 'y':
            print
            drawBoard()
while play.lower() != 'y' and play.lower() != 'n':
    play = raw_input("\nDo you want to play? (y/n): ")
Data = []
while play.lower() == 'y':
    totalgames +=1
    PythonShine = -1
    txt = raw_input("\nType the name of board file including '.txt' or type d for default: ")
    if txt == "d":
        listStrings = read_string_list_from_file("biomesData1.txt")
    else:
        listStrings = read_string_list_from_file(txt)
    Data = create_lists_board(listStrings)
    show_board("just created",Data)
    while PythonShine < 0 or PythonShine > len(Data)-1:
        PythonShine = input("\nWhich position shall PythonShine be (0.."+str(len(Data)-1)+"), ")
    if PythonShine == 0:
        PythonShine = 1


    #Codes for make the character
    Name = ""
    print "\nData for player"
    while Name == "":
        Name = raw_input("\nName? ")
    print
    playerDraw()
    HP = raw_input("Initial life points (10..50)? ")
    while HP.isalpha() or int(HP) < 10 or int(HP) > 50:
        if HP.isalpha():
            print "What you typed is not an integer, please retype"
        else:
            print "What you typed in out of range, please retype"
        HP = raw_input("Initial life points (10..50)? ")
    Player = Explorer(Name,int(HP))


    #Codes for game init
    Catastrophes = False
    Surprise = False
    Check = raw_input("\nMaximum turns this game? (1..10) ")
    while Check.isalpha() or int(Check) < 1 or int(Check) > 10:
        if Check.isalpha():
            print "\nWhat you typed is not an integer, please retype"
        else:
            print "\nWhat you typed in out of range, please retype"
        Check = raw_input("Maximum turns this game? (1..10) ")
    Max = int(Check)
    
    Check = raw_input("\nAllow that catastrophes happen? (y/n): ")
    while Check.lower() != 'y' and Check.lower() != 'n':
        Check = raw_input("\nPlease type y or n: ")
    if Check == 'y':
        Catastrophes = True    
    Check = raw_input("\nAllow that surprises happen? (y/n): ")
    while Check.lower() != 'y' and Check.lower() != 'n':
        Check = raw_input("\nPlease type y or n: ")
    if Check == 'y':
        Surprise = True


    #Codes for game play

    Catas = 0
    Surp = 0
    turn = 1
    while Player.hp > 0 and turn <= Max and Player.pos != PythonShine:
        show_board("about to do turn num:"+str(turn),Data,Player.pos)
        show_player("about to do turn num:"+str(turn),Player)
        Choice = ""
        while Choice.lower() != 'd' and Choice.lower() != 'u':
            Choice = raw_input("\nRoll die, or user types next pos? (d/u): ")
        if Choice == 'd':
            Dice = random.randint(1,6)
            print "\n the die was... "+str(Dice)
            print " the previous position was... "+str(Player.pos)
            Player.pos += Dice
            if Player.pos > len(Data)-1:
                Player.pos-=len(Data)
            print " and the next position is... "+str(Player.pos)+"\n"
        else:
            while Choice.isalpha() or int(Choice) > len(Data)-1 or int(Choice) < 0:
                Choice = raw_input(" which biome should the player go? (0.."+str(len(Data)-1)+"): ")
            Player.pos = int(Choice)
            print ""
            
        if Player.pos == PythonShine:
            print "Amazing! the player is in PythonShine and won the game!"
            Player.hp = 9999
            Player.diam = 9999
        else:
            biome = Data[Player.pos]
            if biome[0] == 0:
                print "\nIn biome #0 no action takes place..."
            else:
                if biome[1]/3 > 0:
                    print "\nyey!!... the player collected "+str(biome[1]/3)+" diamonds"
                else:
                    print "\n well, there is no diamonds in biome "+str(biome[0])
                Player.diam+=biome[1]/3
                if Player.diam>9999:
                    Player.diam=9999
                biome[1]-=biome[1]/3
                if biome[2] > Player.sword:
                    print "Yey!!... the player exchanged to a better sword"
                    Player.sword,biome[2] = biome[2],Player.sword
                    print "The player's new sword is of type: "+str(Player.sword)
                if Player.sword < biome[3]:
                    if Player.hp == 1:
                        i = 1
                    else:
                        i = random.randint(1,Player.hp)
                    Player.hp -= i
                    print "Oh No! the player lost the fight and lost "+str(i)+" life points"
                elif Player.sword == biome[3]:
                    if Player.hp == 1:
                        i = 1
                    else:
                        i = random.randint(1,Player.hp/2)
                    Player.hp -= i
                    print "Oh well... the player tied the fight and lost "+str(i)+" life points"
                else:
                    if Player.hp == 1:
                        i = 1
                    else:
                        i = random.randint(1,Player.hp)
                    Player.hp += i
                    if Player.hp>9999:
                        Player.hp=9999
                    print "Great! the player won the fight and won "+str(i)+" life points"
                if Player.hp < 0:
                    Player.hp = 0
                print "The Player now has "+str(Player.hp)+" life points"

            #Catastrophes
            if Player.hp > 0 and Catastrophes:
                i = random.randint(1,len(Data)*5)
                if i < len(Data):
                    Catas+=1
                    print "\nOh oh! A catastrohe occured in biome # "+str(i)
                    print "and the board shrunk"
                    if PythonShine > i:
                        PythonShine -= 1
                    if Player.pos == i:
                        print "and the player was there!! and died!"
                        Player.hp = 0
                    elif Player.pos > i:
                        Player.pos-=1
                        Data.pop(i)
                        index = len(Data)-1
                        while index >= i:
                            biome = Data[index]
                            biome[0] -= 1
                            index -= 1
                        print "but the player was not there, yet the player's position changed"
                        print "and now is "+str(Player.pos)
                    else:
                        Data.pop(i)
                        index = len(Data)-1
                        while index >= i:
                            biome = Data[index]
                            biome[0] -= 1
                            index -= 1
                        print "but the player was not there, so the player is safe"
            #Surprise
            if Player.hp >0 and Surprise:
                i = random.randint(1,len(Data)*5)
                if i < len(Data):
                    Surp += 1
                    print "\n Oooooh! A surprise is happening up to biome # "+str(i)
                    print " the board will have more diamonds for the next turn!"
                    while i > 1:
                        Biome1 = Data[i-1]
                        Biome2 = Data[i]
                        Biome1[1] += Biome2[1]
                        i-=1
        
        turn += 1
    #End part
    print "\n RESULTS END OF GAME"
    print "\nThe game number " + str(totalgames) + " just took place"
    if Player.hp <= 0:
        print "The game ended because the player died"
    elif turn >= Max:
        print "The game ended because the max number of turns were played"
    else:
        print "The game ended because the player is in PythonShine and won the game!"
        win += 1
    show_board("end of game",Data,Player.pos)
    show_player("end of game",Player)
    if Player.pos == PythonShine and Player.hp > 0:
        print "and he reached PythonShine, so he won!!!"
    if Catas > 0:
        print "\n"+str(Catas)+" catastrophes took place, eliminating a biome each"
    play = ""
    if Surp > 0:
        print "\n"+str(Surp)+" surprises took place, adding diamonds to the board"
    play = raw_input("\nDo you want to play again? (y/n): ")
    while play.lower() != 'y' and play.lower() != 'n':
        print "\nPlease type y or n!"
        play = raw_input("Do you want to play again? (y/n): ")

#Codes of showing results
if totalgames > 0:
    print "\n RESULTS END OF ALL GAMES..........."
    print "\n The user played " + str(totalgames) + " games in total"
    print " of those, the player won "+str(win)
    print " To conclude, the program will do a conversion from binary to decimal!"
    print " taking as source the diamonds list in the list game board"
    DiamondsList = []
    BinaryList = []
    for i in Data:
        DiamondsList.append(i[2])
        if i[2]%2 == 0:
            BinaryList.append(0)
        else:
            BinaryList.append(1)
    print "\n  List with diamonds: " + List2Str(DiamondsList)
    print "  Corresponding Binary: " + List2Str(BinaryList)
    print "  which converted to decimal is: " + str(convert_2_to_10(BinaryList))
print "\n\n\nBye...."
