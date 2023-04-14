from random import randint
from time import sleep
from colorama import Fore
def cards():
    # Takes the information number of a card
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    cd = deck[randint(0, 11)]
    return cd
def cn():
    # Takes the name of the card
    names = ['hearts', 'diamonds', 'spades', 'clubs']

    names = names[randint(0,3)]
    return names
def translator():
    # translates the 2 starting cards tbat the player gets to numbers
    total = 0
    startingHand1 = cards()
    startingHand2 = cards()
    print(f'Your starting cards are {startingHand1} of {cn()} and {startingHand2} of {cn()}')
    if startingHand1 == 'J' or startingHand1 == 'Q' or startingHand1 == 'K':
        total += 10
    elif startingHand1 == 'A':
        total += int(input('What do you want the A to be? [1/11]: '))
    else:
        total += startingHand1
    if startingHand2 == 'J' or startingHand2 == 'Q' or startingHand2 == 'K':
        total += 10
    elif startingHand2 == 'A':
        total += int(input('What do you want the A to be? [1/11]: '))
    else:
        total += startingHand2
    return total
def randomCard():
    # Translates new random cards to numbers
    newCard = cards()
    total = 0
    print(f'Your new card is {newCard} of {cn()}')
    if newCard == 'J' or newCard == 'Q' or newCard == 'K':
        total += 10
    elif newCard == 'A':
        total += int(input('What do you want the A to be? [1/11]: '))
    else:
        total += newCard
    return total
def dealerInitialCard():
    # translates the 2 starting cards tbat the dealer gets to numbers
    total = 0
    startingHand1 = cards()
    print(f'The dealer is showing a {startingHand1} of {cn()}')
    if startingHand1 == 'J' or startingHand1 == 'Q' or startingHand1 == 'K':
        total += 10
    elif startingHand1 == 'A':
        total += 11
    else:
        total += startingHand1
    return total 
def dealerRandomCard():
     # Translates new random cards to numbers
    newCard = cards()
    total = 0
    print(f'The dealer new card is {newCard} of {cn()}')
    if newCard == 'J' or newCard == 'Q' or newCard == 'K':
        total += 10
    elif newCard == 'A':
        total += 1
    else:
        total += newCard
    return total
def main():
    print('')
    print('Welcome to Blackjack!')
    while True:
        # sum of the player cards from the translator
        print(Fore.GREEN)
        pc = translator()
        print(f'Your total is {pc} ')
        print(Fore.RED)
        dc = dealerInitialCard()
        while True:
            # Takes the action of the player 
            print(Fore.YELLOW)
            ac = str(input('What do you want to do? [H]it, [S]tand: '))
            ac = ac.upper()
            # Breaks the loop if it stands
            if ac == 'S':
                break
            # Draws a random card if it hits
            elif ac == 'H':
                print(Fore.BLUE)
                pc += randomCard()

                # Checks if it busted
                if pc > 21:
                    
                    print(Fore.RED + f'You busted, your total is {pc}')
                    break
                else:
                    print(Fore.BLUE +f'Your total is {pc}')
        while True:
            # Dealer AI
            if pc > 21:
                break
            if 21 > dc and pc > dc :
                print(Fore.MAGENTA)
                dc += dealerRandomCard()
                sleep(.5)
                print(f'The dealer total is {dc}')
                sleep(2)
                print(Fore.RESET)
            else:
                break
        # Checks the results
        if dc > 21:
            print(Fore.CYAN +'The dealer busted')
        if 21 >= pc and pc > dc and dc < 21 or dc > 21 and pc <= 21:
            print(Fore.GREEN + 'You win')
        else:
            print(Fore.RED +'You Lose')

        # Loop to play again
        yn = str(input(Fore.RESET + 'Do you wanna play again? [Y/N]: '))
        if yn.upper() == 'N':
            print('Thanks for playing!')
            quit()
        elif yn.upper() == 'Y':
            print("Let's play again then!")
        else:
            print("We're counting it as a yes")
    Fore.RESET

main()
