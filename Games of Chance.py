import random

money = 100


# Write your game of chance functions here
def coin_flip(guess, bet):
    global money
    if isinstance(bet, int) == False:
        print("Bet must be an integer")
    else:
        if bet > money:
            print("You bet ${bet} but you only have ${money}, you can't bet more than you have.".format(bet=bet, money=money))
        elif bet < 1:
            print("You cannot bet a negative amount. Please enter a bet of at least $1")
        else:
            num = random.randint(1, 2)
            # heads = 1
            # tails = 2
            if isinstance(guess, str) and "heads" in guess.lower() or isinstance(guess, str) and "tails" in guess.lower():
                if num == 1 and "heads" in guess.lower():
                    money += bet
                    print("You guessed correctly and won ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
                if num == 1 and "tails" in guess.lower():
                    money -= bet
                    print("You guessed incorrectly and lost ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
                if num == 2 and "tails" in guess.lower():
                    money += bet
                    print("You guessed correctly and won ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
                if num == 2 and "heads" in guess.lower():
                    money -= bet
                    print("You guessed incorrectly and lost ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
            else:
                print("Invalid entry, please enter \"heads\" or \"tails\"")
            return


def cho_han(guess, bet):
    global money
    if isinstance(bet, int) == False:
        print("Bet must be an integer")
    else:
        if bet > money:
            print("You bet ${bet} but you only have ${money}, you can't bet more than you have.".format(bet=bet, money=money))
        elif bet < 1:
            print("You cannot bet a negative amount. Please enter a bet of at least $1")
        else:
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            dice_sum = dice_1 + dice_2
            print("Dice one is {dice_1}".format(dice_1=dice_1))
            print("Dice two is {dice_2}".format(dice_2=dice_2))
            if dice_sum % 2 == 0 and "even" in guess.lower():
                money += bet
                print("You guessed correctly, the sum of the dice is even and you won ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
            if dice_sum % 2 == 0 and "odd" in guess.lower():
                money -= bet
                print("You guessed incorrectly, the sum of the dice is even and you lost ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
            if dice_sum % 2 != 0 and "odd" in guess.lower():
                money += bet
                print("You guessed correctly, the sum of the dice is odd and you won ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
            if dice_sum % 2 != 0 and "even" in guess.lower():
                money -= bet
                print("You guessed incorrectly, the sum of the dice is odd and you lost ${bet}. Your current balance is ${money}.".format(bet=bet, money=money))
        return


played_cards = []
p1_money = 100
p2_money = 100


def cards(bet):
    global p1_money
    global p2_money
    if isinstance(bet, int) == False:
        print("Bet must be an integer")
    else:
        if bet > p1_money and bet > p2_money:
            print("The bet was ${bet} but player one only has ${p1} and player two only has ${p2}, players cannot bet more than they have. Please enter a valid bet.".format(
                bet=bet, p1=p1_money, p2=p2_money))
        elif bet > p1_money:
            print("The bet was ${bet} but player one only has ${money}, players cannot bet more than they have. Please enter a valid bet.".format(bet=bet, money=p1_money))
        elif bet > p2_money:
            print("The bet was ${bet} but player two only has ${money}, players cannot bet more than they have. Please enter a valid bet.".format(bet=bet, money=p2_money))
        elif bet < 1:
            print("The bet was ${bet}, bets cannot be negative, please enter a postive number for your bet.".format(bet=bet))

        else:
            if len(played_cards) < 52:
                # player 1 cards
                p1_card = random.randint(2, 14)
                if played_cards.count(p1_card) < 4:
                    played_cards.append(p1_card)
                    if p1_card == 14:
                        print("Player one card: Ace")
                    if p1_card == 13:
                        print("Player one card: King")
                    if p1_card == 12:
                        print("Player one card: Queen")
                    if p1_card == 11:
                        print("Player one card: Jack")
                    if p1_card <= 10:
                        print("Player one card: {card}".format(card=p1_card))
                else:
                    while played_cards.count(p1_card) == 4:
                        p1_card = random.randint(2, 14)
                    played_cards.append(p1_card)
                    if p1_card == 14:
                        print("Player one card: Ace")
                    if p1_card == 13:
                        print("Player one card: King")
                    if p1_card == 12:
                        print("Player one card: Queen")
                    if p1_card == 11:
                        print("Player one card: Jack")
                    if p1_card <= 10:
                        print("Player one card: {card}".format(card=p1_card))

                # player 2 cards
                p2_card = random.randint(2, 14)
                if played_cards.count(p2_card) < 4:
                    played_cards.append(p2_card)
                    if p2_card == 14:
                        print("Player two card: Ace")
                    if p2_card == 13:
                        print("Player two card: King")
                    if p2_card == 12:
                        print("Player two card: Queen")
                    if p2_card == 11:
                        print("Player two card: Jack")
                    if p2_card <= 10:
                        print("Player two card: {card}".format(card=p2_card))
                else:
                    while played_cards.count(p2_card) == 4:
                        p2_card = random.randint(2, 14)
                    played_cards.append(p2_card)
                    if p2_card == 14:
                        print("Player two card: Ace")
                    if p2_card == 13:
                        print("Player two card: King")
                    if p2_card == 12:
                        print("Player two card: Queen")
                    if p2_card == 11:
                        print("Player two card: Jack")
                    if p2_card <= 10:
                        print("Player two card: {card}".format(card=p2_card))

                if p1_card > p2_card:
                    print("Player one wins")
                    p1_money += bet
                    p2_money -= bet
                if p1_card < p2_card:
                    print("Player two wins")
                    p1_money -= bet
                    p2_money += bet

                if p1_card == p2_card:
                    print("It's a tie")

                # print(sorted(played_cards))
                print("total cards drawn: {num}".format(num=len(played_cards)))
                # print("Player one wallet: ${p1_money}".format(p1_money = p1_money))
                # print("Player two wallet: ${p2_money}".format(p2_money = p2_money))

            else:

                print("All cards played.")
                played_cards.clear()
                # print(played_cards)
            return


roulette_money = 500
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
first_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
third_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

def roulette(guess, bet):
    global roulette_money
    result = random.randint(-1, 36)
    if bet > roulette_money:
        print("You bet ${bet} but you only have ${money} you cannot bet more than you have".format(bet=bet, money=roulette_money))
    elif bet < 1 and isinstance(guess, int) and guess < 1:
        print("Invalid guess and invalid bet. Please enter a number greater than 0 for your bet and a number between 1 and 36 if your guess is a single number bet")
    elif isinstance(guess, int) and guess < 1 and bet > 0:
        print("Invalid guess, please enter a number between 1 and 36 for your guess")
    elif bet < 1 and isinstance(guess, int) and 1 < guess < 36:
        print("Invalid bet, please enter a positive number for your bet.")
    elif isinstance(guess, list) and len(guess) != 2 and len(guess) != 3 and len(guess) != 4 and len(guess) != 5 and len(guess) != 6:
        print("You entered an invalid argument into the function please enter one of the following: \n An integer for a straight number bet \n \"odd\" or \"even\" for an odd/even bet \n \"red\" or \"black\" for a red/black bet \n \"high\" or \"low\" for a high/low bet \n \"1st dozen\", \"2nd dozen\" or \"3rd dozen\" for a dozens bet \n \"1st column\", \"2nd column\" or \"3rd column\" for a columns bet \n A list of 2 consecutive numbers for a split bet \n A list of 3 consecutive numbers for a street bet \n A list of 4 numbers for a sqaure bet \n A list of 5 numbers from -1 to 3 for a 5 number bet \n A list of 6 numbers for a six line bet.")
    elif isinstance(guess, str) and "red" not in guess.lower() and "black" not in guess.lower() and "high" not in guess.lower() and "low" not in guess.lower() and "even" \
                not in guess.lower() and "odd" not in guess.lower() and "1st column" not in guess.lower() and "first column" not in guess.lower() and "2nd column" not in guess.lower() and "second column" not in guess.lower() and "3rd column" not in guess.lower() and "third column" not in guess.lower() and "1st dozen" not in guess.lower() and "first dozen" not in guess.lower() and "2nd dozen" not in guess.lower() and "second dozen" not in guess.lower() and "3rd dozen" not in guess.lower() and "third dozen" not in guess.lower():
        print("You entered an invalid argument into the function please enter one of the following: \n An integer for a straight number bet \n \"odd\" or \"even\" for an odd/even bet \n \"red\" or \"black\" for a red/black bet \n \"high\" or \"low\" for a high/low bet \n \"1st dozen\" or \"first dozen\", \"2nd dozen\" or \"second dozen\" or \"3rd dozen\" or \"third dozen\" for a dozens bet \n \"1st column\" or \"first column\", \"2nd column\" or \"second column\" or \"3rd column\" or \"third column\" for a columns bet \n A list of 2 numbers for a split bet \n A list of 3 consecutive numbers for a street bet \n A list of 4 numbers for a sqaure bet \n A list of 6 numbers for a six line bet.")

    else:
        #single number bet
        if isinstance(guess, int):
            integer(result, guess, bet)
        # highs/lows, odds/evens/columns,dozens
        if isinstance(guess, str):
            string(result, guess, bet)
        # split bets
        if isinstance(guess, list) and len(guess) == 2:
            split_bet(result, guess, bet)
        #street bets
        if isinstance(guess, list) and len(guess) == 3:
            street_bet(result, guess, bet)
        # square bets
        if isinstance(guess, list) and len(guess) == 4:
            square_bet(result, guess, bet)
        # 5 number bets
        if isinstance(guess, list) and len(guess) == 5:
            five_number_bet(result, guess, bet)
        # 6 line bets
        if isinstance(guess, list) and len(guess) == 6:
            six_line_bet(result, guess, bet)

        print("Bet was ${bet}".format(bet=bet))
        print("Roulette money total is: ${money}".format(money=roulette_money))

    return

#Helper functions for the roulette function to make reading code easier.
def integer(result, guess, bet):
    global roulette_money
    if result == -1:
        roulette_money -= (bet)
        print("Double zero, you lost!")
    elif result == 0:
        roulette_money -= (bet)
        print("Zero, you lost!")
    elif result == guess:
            roulette_money += (bet * 35)
            print("You guessed {guess} and the result was {result}, you won!".format(guess=guess, result=result))
    elif result != guess:
            roulette_money -= (bet)
            print("You guessed {guess} and the result was {result}, you lost!".format(guess=guess, result=result))

def string(result, guess, bet):
    global roulette_money
    if result == - 1:
        roulette_money -= bet
        print("Double zero, you lost!")
    elif result == 0:
        roulette_money -= bet
        print("Zero, you lost!")

    # odds and evens bets
    elif "even" in guess.lower() and result % 2 == 0:
        roulette_money += bet
        print("You guessed {guess} and the result was {result}, You won!".format(guess=guess, result=result))
    elif "even" in guess.lower() and result % 2 != 0:
        roulette_money -= bet
        print("You guessed {guess} and the result was {result}, you lost!".format(guess=guess, result=result))
    elif "odd" in guess.lower() and result % 2 == 0:
        roulette_money -= bet
        print("You guessed {guess} and the result was {result}, you lost!".format(guess=guess, result=result))
    elif "odd" in guess.lower() and result % 2 != 0:
        roulette_money += bet
        print("You guessed {guess} and the result is {result}, You won!".format(guess=guess, result=result))

    # red/black bets
    elif result in red_numbers and "red" in guess.lower():
        roulette_money += bet
        print("You guessed red and the result is red, you won!")
    elif result not in red_numbers and "red" in guess.lower():
        roulette_money -= bet
        print("You guessed red and the result is black, you lost!")
    elif result in black_numbers and "black" in guess.lower():
        roulette_money += bet
        print("You guessed black and the result is black, you won!")
    elif result not in black_numbers and "black" in guess.lower():
        roulette_money -= bet
        print("You gussed black and the result is red, you lost!")

    # high/low bets
    elif "low" in guess.lower() and 0 < result <= 18:
        roulette_money += bet
        print("You guessed low and result is low. you won!")
    elif "low" in guess.lower() and result > 18:
        roulette_money -= bet
        print("You guessed low and result is high. you lost!")
    elif "high" in guess.lower() and 18 < result <= 36:
        roulette_money += bet
        print("You guessed high and result is high. You won!")
    elif "high" in guess.lower() and result < 18:
        roulette_money -= bet
        print("You guessed high and result is low. You lost!")

    # dozens bets
    elif "1st dozen" in guess.lower() and 0 < result <= 12 or "first dozen" in guess.lower() and 0 < result <= 12:
        roulette_money += (bet * 2)
        print("You guessed 1st dozen and the result is first dozen, you won!")
    elif "1st dozen" in guess.lower() and 12 < result <= 24 or "first dozen" in guess.lower() and 12 < result <= 24:
        roulette_money -= (bet)
        print("You guessed 1st dozen and the result is second dozen, you lost!")
    elif "1st dozen" in guess.lower() and 24 < result or "first dozen" in guess.lower() and 24 < result:
        roulette_money -= (bet)
        print("You guessed first dozen and the result is third dozen, you lost!")
    elif "2nd dozen" in guess.lower() and 12 < result <= 24 or "second dozen" in guess.lower() and 12 < result <= 24:
        roulette_money += (bet * 2)
        print("You guessed 2nd dozen and the result is second dozen, you won!")
    elif "2nd dozen" in guess.lower() and 0 < result <= 12 or "second dozen" in guess.lower() and 0 < result <= 12:
        roulette_money -= (bet)
        print("You guessed 2nd dozen and the result is first dozen, you lost!")
    elif "2nd dozen" in guess.lower() and 24 < result or "second dozen" in guess.lower() and 24 < result:
        roulette_money -= (bet)
        print("You guseed second dozen and the result is third dozen, you lost!")
    elif "3rd dozen" in guess.lower() and 24 < result or "third dozen" in guess.lower() and 24 < result:
        roulette_money += (bet * 2)
        print("You guessed 3rd dozen and the result is third dozen, you won!")
    elif "3rd dozen" in guess.lower() and 0 < result <= 12 or "third dozen" in guess.lower() and 0 < result <= 12:
        roulette_money -= (bet)
        print("You guessed 3rd dozen and the result is first dozen, you lost!")
    elif "3rd dozen" in guess.lower() and 12 < result <= 24 or "third dozen" in guess.lower() and 12 < result <= 24:
        roulette_money -= (bet)
        print("You guessed 3rd dozen and the result is second dozen, you lost!")

    # columns bets
    elif "1st column" in guess.lower() and result in first_column or "first column" in guess.lower() and result in first_column:
        roulette_money += (bet * 2)
        print("You guessed 1st column and the result is first column, you won!")
    elif "1st column" in guess.lower() and result in second_column or "first column" in guess.lower() and result in second_column:
        roulette_money -= (bet)
        print("You guessed 1st column and the result is second column, you lost!")
    elif "1st column" in guess.lower() and result in third_column or "first column" in guess.lower() and result in third_column:
        roulette_money -= (bet)
        print("You guessed 1st column and the result is third column, you lost!")
    elif "2nd column" in guess.lower() and result in second_column or "second column" in guess.lower() and result in second_column:
        roulette_money += (bet * 2)
        print("You guessed 2nd column and the result is 2nd column, you won!")
    elif "2nd column" in guess.lower() and result in first_column or "second column" in guess.lower() and result in first_column:
        roulette_money -= (bet)
        print("You guessed 2nd column and the result is 1st column, you lost!")
    elif "2nd column" in guess.lower() and result in third_column or "second column" in guess.lower() and result in third_column:
        roulette_money -= (bet)
        print("You guessed 2nd column and the result is 3rd column, you lost!")
    elif "3rd column" in guess.lower() and result in third_column or "third column" in guess.lower() and result in third_column:
        roulette_money += (bet * 2)
        print("You guessed 3rd column and the result is 3rd column, you won!")
    elif "3rd column" in guess.lower() and result in first_column or "third column" in guess.lower() and result in first_column:
        roulette_money -= (bet)
        print("You guessed 3rd column and the result is 1st column, you lost!")
    elif "3rd column" in guess.lower() and result in second_column or "third column" in guess.lower() and result in second_column:
        roulette_money -= (bet)
        print("You guessed 3rd column and the result is 2nd column, you lost!")

def split_bet(result, guess, bet):
    global roulette_money
    if guess[0] + 1 != guess[1] and guess[0] + 3 != guess[1]:
        print("invalid guess, second number should be first number + 1 or first number + 3")
    else:
        if result == -1:
            roulette_money -= bet
            print("Double Zero, you lost!")
        elif result == 0:
            roulette_money -= bet
            print("Zero, you lost!")
        elif result in guess:
            roulette_money += (bet * 17)
            print("You guessed {guess} and the result is {result}, you won!".format(guess=guess, result=result))
        else:
            roulette_money -= bet
            print("You guessed {guess} and the result is {result}, you lost!".format(guess=guess, result=result))

def street_bet(result, guess, bet):
    global roulette_money
    if guess[0] + 1 != guess[1] or guess[1] + 1 != guess[2]:
        print("Invalid bet, 2nd number should bet 1st number + 1 and 3rd number should be 2nd number plus 1")
    else:
        if result == -1:
            roulette_money -= (bet)
            print("Double Zero, you lost!")
        elif result == 0:
            roulette_money -= (bet)
            print("Zero, you lost!")
        elif result in guess:
            roulette_money += (bet * 11)
            print("You guessed {guess} and the result is {result}, you won!".format(guess=guess, result=result))
        else:
            roulette_money -= (bet)
            print("You guessed {guess} and the result is {result}, you lost!".format(guess=guess, result=result))

def square_bet(result, guess, bet):
    global roulette_money
    if guess[0] + 1 != guess[1] or guess[0] + 3 != guess[2] or guess[2] + 1 != guess[3]:
        print(
            "Invalid guess for a square bet. You guessed [{zero}, {one}, {two}, {three}], please enter a valid square bet.".format(
                zero=guess[0], one=guess[1], two=guess[2], three=guess[3]))
    else:
        if result == -1:
            roulette_money -= (bet)
            print("Double Zero, you lost!")
        elif result == 0:
            roulette_money -= (bet)
            print("Zero, you lost!")
        elif result in guess:
            roulette_money += (bet * 8)
            print("You guessed {guess} and the result is {result}, you won!".format(guess=guess, result=result))
        else:
            roulette_money -= (bet)
            print("You guessed {guess} and the result is {result}, you lost!".format(guess=guess, result=result))

def five_number_bet(result, guess, bet):
    global roulette_money
    if guess != [-1, 0, 1, 2, 3]:
        print("Invalid bet. Please enter [-1, 0, 1, 2, 3] for a 5 number bet".format(guess=guess))
    else:
        if result in guess:
            roulette_money += (bet * 6)
            if result == -1:
                print("Double Zero, you won!")
            elif result == 0:
                print("Zero, you won!")
            else:
                print("Result was {result}, you won!".format(result=result))
        else:
            roulette_money -= (bet)
            print("Result is {result}, you lost!".format(result=result))

def six_line_bet(result, guess, bet):
    global roulette_money
    if guess[0] + 1 != guess[1] or guess[1] + 1 != guess[2] or guess[2] + 1 != guess[3] or guess[3] + 1 != guess[4] or guess[4] + 1 != guess[5] or guess[
        0] not in first_column:
        print("Invalid six line bet, you entered {guess}. please enter six consecutive numbers".format(guess=guess))
    else:
        if result == -1:
            roulette_money -= (bet)
            print("Double Zero, you lost!")
        elif result == 0:
            roulette_money -= (bet)
            print("Zero, you lost!")
        elif result in guess:
            roulette_money += (bet * 5)
            print("You guessed {guess} and the result is {result}, you won!".format(guess=guess, result=result))
        else:
            roulette_money -= (bet)
            print("You guessed {guess} and the result is {result}, you lost!".format(guess=guess, result=result))









# Call your game of chance functions here
# roulette(5, 500)
# roulette("Even!", 5)
# roulette("ODD!", 5)
# roulette("RED!", 5)
# roulette("BLACK!" ,5)
# roulette("LOW!", 5)
# roulette("HIGH!", 5)
# roulette("1ST DOZEN!", 5)
# roulette("FIRST DOZEN!", 5)
# roulette("2ND DOZEN!", 5)
# roulette("SECOND DOZEN!", 5)
# roulette("3RD DOZEN!", 5)
# roulette("THIRD DOZEN!", 5)
# roulette("1ST COLUMN!", 5)
# roulette("FIRST COLUMN!", 5)
# roulette("SECOND COLUMN!", 5)
# roulette("2nd Column!@", 5)
# roulette("3RD COLUMN!!", 5)
# roulette("THIRD COLUMN", 5)
# roulette([1,2], 5)
# roulette([1,2,3],5)
# roulette([1,2,3,4],5)
# roulette([1,2,3,4,5,6], 5)
# roulette([1,2,3,4,5,6,7], 5)
#roulette("testing", 5)
# roulette(-5,5)
#roulette(5, -5)
# roulette(-5, -5)
# dave = p1_money
# roulette(100, 5)
# roulette("odd", 50)
# coin_flip("Heads@!@2", 10)
# coin_flip("TAILS!@@!", 10)
# coin_flip(5, 5)
# coin_flip(4, 6)
# coin_flip("heads", -5)
# coin_flip("heads", "5")
# print(money)
# print(coin_flip("Tails", 15))
# print(money)

# cho_han("even!!", 10)
# cho_han("ODD!@@#", 20)

# cards(5)
# cho_han("even", "4")
# print(coin_flip("Heads", 10))


# print(money)

# print(coin_flip("Tails", 15))
# print(money)

# print(cho_han("even", 10))
#print(cho_han("ODD", 20))
