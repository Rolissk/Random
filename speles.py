import random, sys, vardata

def secretNumber():
    print('Hello to he secret number game!\nYou will have 6 attempts to guess the number!')
    while True:
        vardata.balance = vardata.balance - 5
        secretNumb = random.randint(1,30)
        print('Im thinking of  anumber between 1 and 30')

        for guessesTaken in range(1,6):
            print('Take a guess')
            guess=int(input())

            if guess<secretNumb:
                print('Guess is too low')
            elif guess>secretNumb:
                print('Guess is too high')
            else:
                break

        if secretNumb == guess:
            print('Congrats, you guessed it in ' +str(guessesTaken) +' guesses and you\'ve earned 10 points!')
            vardata.balance = vardata.balance + 10
        else:
            print('The number i was thinking of was ' +str(secretNumb) +'!')
        snizvele = input('If you\'d like to play again, type (a) or press enter to quit!')
        if snizvele == 'a':
            continue
        elif snizvele == '':
            break

def rockPaperScissors():
    print('ROCK, PAPER, SCISSORS')
    while True:
        vardata.balance = vardata.balance - 5
        while True:
            print('Your turn: (r)ock (p)aper (s)cissors')
            plMove = input()
            if plMove == 'r' or plMove =='p' or plMove =='s':
                break
            print('type one of r, p, s.')
        
        if plMove == 'r':
            print('Rock vs')
        elif plMove == 'p':
            print('Paper vs')
        elif plMove == 's':
            print('Scissors vs')

        randomNum = random.randint(1,3)
        if randomNum == 1:
            comMove = 'r'
            print('Rock')
        elif randomNum == 2:
            comMove = 'p'
            print('Paper')
        elif randomNum == 3:
            comMove = 's'
            print('Scissors')
        
        if plMove == comMove:
            print('Its a Tie, you get your money back!')
            vardata.balance = vardata.balance + 5
        elif plMove == 'r' and comMove == 's':
            print('You win!')
            vardata.balance = vardata.balance + 10
        elif plMove == 'p' and comMove == 'r':
            print('You win!')
            vardata.balance = vardata.balance + 10
        elif plMove == 's' and comMove == 'p':
            print('You win!')
            vardata.balance = vardata.balance + 10
        elif plMove == 'r' and comMove == 'p':
            print('You lose')
        elif plMove == 'p' and comMove == 's':
            print('You lose')
        elif plMove == 's' and comMove == 'r':
            print('You lose')
        rpsizvele = input('If you want to play again, type (a) or press enter to quit')
        if rpsizvele == 'a':
            continue
        elif rpsizvele == '':
            break
    

def coinFlip():
    while True:
        vardata.balance = vardata.balance - 5
        coinPick = input('Pick your side of the coin: (h)eads or (t)ails!')
        if coinPick == 'h':
            print('You call heads!')
        elif coinPick == 't':
            print('You call tails!')
        coinRng = random.randint(0,1) 
        if coinRng == 0:
            coinRng = 'h'
            print('Coin has landed on the head!')
            if coinPick == coinRng:
                vardata.balance = vardata.balance + 10
                print('You win!')
            else:
                print('You lose!')
        if coinRng == 1:
            coinRng = 't'
            print('Coin has landed on the tails!')
            if coinPick == coinRng:
                vardata.balance = vardata.balance + 10
                print('You win!')
            else:
                print('You lose!')
        cfizvele = input('If you want to play again, type (a) or press enter to quit!')
        if cfizvele == 'a':
            continue
        if cfizvele == '':
            break

def spinWheel():
    print("""Welcome to spin the wheel!
    Get 2 of the same number and win, get 3 and get the jackpot!""")
    while True:
        print('If you want to play, type (spin), press enter to quit')
        atbilde = input()
        if atbilde == 'spin':
            vardata.balance = vardata.balance - 5
            print('Spinning the wheel!\n')
            pirmais = random.randint(1,5)
            print('1st number is ' + str(pirmais))
            otrais = random.randint(1,5)
            print('2nd number is ' + str(otrais))
            tresais = random.randint(1,5)
            print('3rd number is ' + str(tresais))
        elif atbilde == '':
            break
        if pirmais == otrais and pirmais == tresais and otrais == tresais:
            print('JACKPOT!')
            vardata.balance = vardata.balance + 20
        elif pirmais == otrais or pirmais == tresais or otrais == tresais:
            print('You won a small prize!')
            vardata.balance = vardata.balance + 10
        else:
            print('You lost!')
            