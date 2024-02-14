import random  #imports randoms 

def welcome_message(): #function named welcome_message
    print(" 💲💲✨💰Welcome to Emoticons Slots!!💰✨💲💲") #welcomes the user 
    print("""⠀⠀
 ⠀⠀⠀⠀⠀⠀   ⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠀⠀⣤⣄⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿ ⢸⣿⣿⡇ ⢸⣿⣿⡇⢸⣿⣿⡇ ⣿⡇⠀⠀⠛⠛⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇ ⢸⣿⣿⡇⢸⣿⣿⡇ ⣿⡇⠀⠀⣷⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⡇ ⢸⣿⣿⡇⢸⣿⣿⡇⠀⣿⡇⠀⣾⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⡇⠀⣿⡿⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠙⠃⠀⠀⠀
    ⠀⠀⠀⠀⢀⣴⣿⠟⠛⠛⢻⡿⠛⠛⠛⢻⣿⣿⡟⠋⠉⠉⠛⢿⣦⡀⠀⠀⠀⠀
    ⠀⠀⠀⢰⣿⣿⣥⣤⣤⣤⣾⣧⣤⣤⣤⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⡆⠀⠀⠀
    ⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠀ ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀""") #prints fake slot machine (no action) for details 
    
    while True:
        try:
            welcome = input(" \n      Are you ready to win big (y/n):  ") #asks user to play game
            if welcome.lower() != 'y': 
                if welcome.lower() == 'n':
                    print("\nNevermind(ᗒᗣᗕ)! I guess you don't want to win big....") # user does not want to play
                else:
                    print("Invalid Input👎. Please enter 'y' to play or 'n' to end game.") # user invalid input
            else:
                print("\n     This is going to be funヾ( ˃ᴗ˂ )◞ !\n") # user says 'y' to play game 
                break #ends loop
        except ValueError:
            print("Invalid Input👎🏽") #ValueError 

def display_symbols_amounts(): #function named display_symbols_amounts 
    print("Win big when you match three of the same emoticons in a row! Check out your winning options:") 
    for symbol, value in symbols_amounts.items(): 
        print(f"\n{symbol}: $ {value}\n") ## shows symbols with winning amounts 

def get_starting_balance(): #function named get_starting_balance
    while True:
        try: 
            starting_balance = int(input("Enter your initial balance💰: ")) #asks the user for starting balance
            if starting_balance <= 0:
                print("Balance cannot be negative, Please enter a valid number.") #user needs to enter a valid number
                continue
            return starting_balance #returns to start of loop
        except ValueError:
            print("Invalid Input👎🏽. Please enter a valid number.") #User invalid input 
def get_bet_amount(starting_balance): #function named get_bet_amount | parameter named starting_balance
    while True:
        try: 
            bet_amount = int(input("Enter your bet amount💰: ")) #asks user to enter bet amount
            if bet_amount <= 0: # if bet_amount is less than or equal to 0 then its invalid 
                print("Bet cannot be negative. Please enter a valid number.") #tells user to enter valid number
                continue
            if bet_amount > starting_balance: # if bet_amount is greater than starting_balance then its invalid 
                print("Bet amount cannot exceed your current balance. Please enter a valid bet.") #invalid 
                continue
            return bet_amount # returns to start of loop 
        except ValueError: # value error 
            print("Invalid bet👎🏽. Please enter a valid bet.") #invalid 

def spin_reels(): #function named spin reels 
    print("\nLet's get this party started. Spinning the reels...\n") # lets user know that the reel is spinning 
    for _spins in range(3):
        print("✨💰✨💰✨💰✨💰✨💰✨\n") # reel spinning 
        print("╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾")
        print()
    print("The moment of truth is here! The results are in!!\n") # about to show the results to the player
        
def slots_game(bet_amount, active_balance, progressive_jackpot): # functions slot_game | Parameter bet_amount, starting_balance
    payout = 0 # amount won/lost
    
    first_spin = random.choice(symbols) #first spin is going to be a random symbol 
    second_spin = random.choice(symbols) #second spin is going to be a random symobl 
    third_spin = random.choice(symbols) #third spin is going to be a random symbol

    top_reel = [random.choice(symbols), random.choice(symbols), random.choice(symbols)]
    middle_reel = [first_spin, second_spin, third_spin]
    bottom_reel = [random.choice(symbols), random.choice(symbols), random.choice(symbols)]
    print()

    print(" | ", top_reel[0], " | ", top_reel[1], " | ", top_reel[2], " | ") #random sybmols with no reward
    print(" ╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾")

    print(" | ", middle_reel[0], " | ", middle_reel[1], " | ", middle_reel[2], " | ") #winning row with random sybmols 
    print(" ╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾")

    print(" | ", bottom_reel[0], " | ", bottom_reel[1], " | ", bottom_reel[2], " | ") #random sybmols with no reward
    print(" ╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾╾")

    # Scatter Symbols
    scatter_count = top_reel.count('  SCATTER  ') + middle_reel.count('  SCATTER  ') + bottom_reel.count('  SCATTER  ')
    if scatter_count >= 3:
        payout += 100
        print(f"Congrats! You won 100 extra coins for having 3+ SCATTERs in all reels!\n") # scatter gives player 100 coins for 3 of them 

    # Wild Symbols
    wild_count = middle_reel.count('    WILD   ') # count how many WILD symbols in middle reel

    # check if all the same symbol
    if first_spin == second_spin and second_spin == third_spin: # 1 = 2 & 2 = 3 
        payout += symbols_amounts[first_spin]
        if payout >= 1000: # custom message for jackpot
            payout += progressive_jackpot # payout + pro jackpot 
            print(f"You won $ {progressive_jackpot} extra coins from the progressive jackpot!!\n")  # shows progressive jackpot to player 
            print(f"Congrats🎉!! You won the jackpot of $ {payout} coins!!!\n") #shows jackpot winnings + progressive jackpot 
            print("""
                    /\_/|
                  /  $^$| 
               \/___|||_|💰\n""") #prints jackpot cat 
        elif payout > 0: # default message
            print(f"Congrats◝(ᵔᵕᵔ)◜!! You won $ {payout} coins.\n") # shows player winnings 

    elif wild_count == 2: # if 2 wild symbols in middle reel
        other_symbol_list = [symbol for symbol in middle_reel if symbol != '    WILD   '] # new list of non WILD symbols
        if other_symbol_list:
            other_symbol = other_symbol_list[0] # get payout from dict
            payout += symbols_amounts.get(other_symbol, 0) # update balance
        if payout >= 1000: # custom message for jackpot
            payout += progressive_jackpot
            print(f"You won $ {progressive_jackpot} extra coins from the progressive jackpot!!\n") # shows progressive jackpot to player 
            print(f"Congrats🎉!! You won the jackpot of $ {payout} coins!!!\n") #shows jackpot winnings + progressive jackpot 
            print("""
                    /\_/|
                  /  $^$| 
               \/___|||_|💰\n""") #prints jackpot cat 
        elif payout > 0: # default message
            print(f"Congrats◝(ᵔᵕᵔ)◜!! You won $ {payout} coins.\n") #shows winnings 
        else:
            active_balance -= bet_amount
            print("Better luck next time! You lost this spin (ᵕ︵ᵕ). \n") #player lost this spin 
            return active_balance, payout

    elif wild_count == 1: # if 1 wild symbols in middle reel
        other_symbols = [symbol for symbol in middle_reel if symbol != '    WILD   '] # new list of non WILD symbols
        if other_symbols[0] == other_symbols[1]:
            payout += symbols_amounts.get(other_symbols[0], 0) # get payout from dict
        if payout >= 1000: # custom message for jackpot
            payout += progressive_jackpot
            print(f"You won $ {progressive_jackpot} extra coins from the progressive jackpot!!\n") # shows progressive jackpot to player 
            print(f"Congrats🎉!! You won the jackpot of $ {payout} coins!!!\n") #shows jackpot winnings + progressive jackpot 
            print("""
                    /\_/|
                  /  $^$| 
               \/___|||_|💰\n""") #prints jackpot cat 
        elif payout > 0: # default message
            print(f"Congrats◝(ᵔᵕᵔ)◜!! You won $ {payout} coins.\n") #shows winnings 
        else:
            active_balance -= bet_amount
            print("Better luck next time! You lost this spin (ᵕ︵ᵕ). \n") #player lost the spin 
            return active_balance, payout

    else:
        active_balance -= bet_amount  # balance - each bet 
        print("Better luck next time! You lost this spin (ᵕ︵ᵕ). \n") #player lost the spin 
        return active_balance, payout
        
    active_balance += payout - bet_amount # update balance
    return active_balance, payout

def receipt(starting_balance, final_balance, total_payout, bet_amount, counter):
    
    print("\n\nThanks for playing ^•ﻌ•^ฅ♡! Here is your cashout ticket: \n ") #prints the receipt for player 
    print(f"\nStarting Balance:$ {starting_balance} coins ") #starting balance 
    if(total_payout >= 0):
        print(f"\nTotal Amount Won:$ {total_payout} coins") #total winnings 
    else:
        print(f"\nTotal Amount Lost:$ {total_payout} coins") #total lost
    print(f"\nTotal Amount Bet:$ {counter * bet_amount} coins") # total amount bet
    
    print(f"\nFinal Balance:$ {final_balance} coins.") # final balance at the end of game 
    

def add_money(active_balance):
    while True:
        choice = input("Do you want to add more money💲? (Y/N): ")  #asks the user to add more moeny 
        if choice.lower() == 'y':
            additional_funds = int(input("\nHow much would you like to deposit💰?: ")) #asks the user how much money 
            active_balance += additional_funds
            print(f"\nYour new balance is ${active_balance}.\n") #shows the user the new balance after adding add funds
            break
        if choice.lower() == 'n':
            break
        else:
            print("Invalid Input👎🏽. Please enter 'y'  or 'n'") #error message 
    return active_balance

def main():
    global symbols, symbols_amounts
    symbols = ['¯\\_(ツ)_/¯ ','   (°_°)   ','( ͡° ͜ʖ ͡°)','  (ᴗᵔᴥᵔ)   ', '    WILD   ', '  SCATTER  '] # list of symbols
    symbols_amounts = {('¯\\_(ツ)_/¯ '):10,('   (°_°)   '):20,('( ͡° ͜ʖ ͡°)'):50,('  SCATTER  '):100,'    WILD   ':250,('  (ᴗᵔᴥᵔ)   '):1000} # sets value for symbols 
    payout = 0
    bet_amount = 0
    starting_balance = 0
    active_balance = 0
    total_payout = 0
    progressive_jackpot = 0
    
    welcome_message() #calls welcome message

    display_symbols_amounts() # displays the coin amount for each symbol on win

    starting_balance = get_starting_balance() # retrieve starting balance from user

    bet_amount = get_bet_amount(starting_balance) # retrieve bet amount from user

    spin_reels() # simulate spinning reels

    active_balance, payout = slots_game(bet_amount, starting_balance, progressive_jackpot) # first run
    total_payout += payout #total + payout
    counter = 0
    while True:
        choice = input("Do you want to spin again✨💰? (Y/N): ") #asks the play to spin again 
        counter += 1
        if choice.lower()== 'y':
            # if they want to play again and the user is out of money
            #print(active_balance, bet_amount)
            if active_balance < bet_amount:
                print("\nYou do not have enough money to play ☹!\n")
                # ask user if they want to add money when they run out
                active_balance = add_money(active_balance)
            if active_balance < bet_amount: 
                receipt(starting_balance, active_balance, total_payout, bet_amount, counter) #calls receipt for slots game 
                print("\nBetter luck next time ☘!") # player lost game 
                return 0 #exits the program
            progressive_jackpot+=10  # adds 10 to each play until play wins jackpot 
            active_balance, payout = slots_game(bet_amount, active_balance, progressive_jackpot)
            total_payout += payout  #total + payout 
        
        elif choice.lower() == 'n':
            if active_balance > 0:
                receipt(starting_balance, active_balance, total_payout, bet_amount, counter)  #calls receipt for slots game 
                print("\nCongratulations!! Please see Casino Cashier to redeem your winnings[̲̅$̲̅]-(^ ̮ ^)›")  #tells the user to cash out at casino cashier 
                return 0 #exits the program
            else:
                receipt(starting_balance, active_balance, total_payout, bet_amount, counter) #calls receipt for slots game 
                print("\nBetter luck next time ☘!")   # player lost game 
                return 0 #exits the program 

main()


  
