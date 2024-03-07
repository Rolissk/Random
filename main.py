import random, sys, vardata 

from ieklusana import login, register

from speles import secretNumber, rockPaperScissors, coinFlip, spinWheel

from naudasShit import cashOut, shopMenu, inventory

def gameMenu():
    print('---------')
    print('Which game would you like to play? Every game costs 5 money to play!')
    print('---------')
    chosenGame = input("""
    If you'd like to play guess the secret number - (s) 
    If you'd like to play rock, paper, scissors - (r)
    If you'd like to play coin flip - (c)
    If you'd like to play spin the wheel - (w)
    Chosen game:""")
    chosenGame = chosenGame.lower()
    if chosenGame =='s':
        secretNumber()
    if chosenGame =='r':
        rockPaperScissors()
    if chosenGame == 'c':
        coinFlip()
    if chosenGame == 'w':
        spinWheel()
    
print ('Welcome to the Arcade! \n Would you like to (l)og in, (r)egister or (q)uit?\n')

ieeja=input('Enter your choice: ')
if ieeja == 'l':
    login()
elif ieeja == 'r':
    register()
elif ieeja == 'q':
    sys.exit()
print('\n----- Hello to the Arcade! -----\n')

#main loops
while True:
    izvele = input("""----------
    What would you like to do?\n
    You can check your balance by typing (b)
    You can pick a game to play by typing (g)
    You can cash out by typing (c)
    You can enter the shop by typing (s)
    You can check your inventory by typing (i)
    You can quit by typing (q)\n
    What will you do: """)
    if izvele == 'b':
        print('---------')
        print('You currently have ' +str(vardata.balance)+ ' money!')
        print('---------')
    elif izvele == 'g':
        gameMenu()
    elif izvele == 'c':
        cashOut()
    elif izvele == 's':
        shopMenu()
    elif izvele == 'i':
        inventory()
    elif izvele == 'q':
        sys.exit()
    else:
        print('Sorry, that is not a valid option.')