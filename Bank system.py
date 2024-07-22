def show_balance():
    print("**************************")
    print("your balance is: ${:.2f}".format(balance))
    print("**************************")

def deposit():
    print("**************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("**************************")
    if amount < 0:
       print("That's not a valid amount")
       return 0
    else:
       return amount

def withdraw():
    print("**************************")
    withdrawal_amount = float(input("Enter the withdrawal amount: "))
    print("**************************") 

    if withdrawal_amount > balance:
        print("Insufficient balance")
    elif withdrawal_amount < 0:
       print("Invalid amount")
    else:
       return withdrawal_amount

balance = 0
is_running = True
 
while is_running:
    print("\n**************************")
    print("       Banking program       ")
    print("**************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. exit")
   
    choice= int(input("Enter your Choice(1-4) : "))

    if choice == 1:
      show_balance()
    elif choice == 2:
      balance += deposit()
      show_balance()
    elif choice == 3:
      balance -= withdraw()
      show_balance()
    elif choice == 4:
      is_running = False
    else:
       print("Enter a valid choice")

print("Thank you, Have a nice day")
print("\n")