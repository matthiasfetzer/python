#!/usr/bin/python

# Tic Tac Toe
# By Matthias Fetzer

fields = []
winner = False
player1Plays = True


# creating a function to print the board
def print_board_game ():
    print (' _________________')
    print ('|  ' + fields[0] + '  |  ' + fields[1] + '  |  ' + fields[2] + '  |  ')
    print (' _________________')
    print ('|  ' + fields[3] + '  |  ' + fields[4] + '  |  ' + fields[5] + '  |  ')
    print (' _________________')
    print ('|  ' + fields[6] + '  |  ' + fields[7] + '  |  ' + fields[8] + '  |  ')
    print (' _________________')

def winner_routine ( playerSign ):
    if playerSign=='X' :
        playerWins='Player 1';
    else :
        playerWins='Player 2';
    print_board_game();
    print("++++++++++++++++++++++++++++++++++++++++++")
    print ("+++ " +playerWins + " is the Winner of the Game +++");
    print("++++++++++++++++++++++++++++++++++++++++++")

# fill fields of board with number from 1 to 9
for field in range (0 , 9) :
    fields.append(str(field + 1))

# start game
while (not winner):
    print_board_game()
    if (player1Plays) : field = int (input("Enter you selection Player 1:")); fields [field-1] = 'X'
    else : field = int (input("Enter you selection Player 2:")); fields [field-1] = 'O'

    print ("your selection is: " + str(field))
    # check horizontal and vertical equality of signs
    for x in range (0,3) :
        y=x*3
        # print (fields[0+x] + fields[1+x] + "equals" +fields[0+x] + fields[2+x])
        if (fields[0+y] == fields[1+y] and fields[0+y] == fields[2+y]) :
            winner_routine(fields[0+y]);winner=True

        if (fields[x] == fields[x+3] and fields[x] == fields[x+6]) :
            winner_routine(fields[x]);winner=True

    # check cross equality of signs
    if (fields[0] == fields[4] and fields[0] == fields[8]) :
        winner_routine(fields[0]);
    if (fields[2] == fields[4] and fields[2] == fields[6]) :
        winner_routine(fields[2]);

    if (player1Plays) : player1Plays=False
    else : player1Plays=True
