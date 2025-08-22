from Bank import Bank
from storage import save_accounts,load_accounts
accounts = load_accounts()
while True:
    choice = int(input('1.Create\n2.Login\n3.Exit'))
    if choice == 1:
        user_name = input('Enter Your Name')
        if user_name in accounts:
            print('User Already Exists')
        else:
            password = input('Enter password')
            deposit_amount = int(input('Enter amount to deposit'))
            accounts[user_name] = Bank(user_name,password,deposit_amount)
            print('Account Created')
            save_accounts(accounts)
    elif choice == 2:
        user_name = input('Enter Registered User Name')
        if user_name not in accounts:
            print('Invalid UserName')
        else:
            acc = accounts[user_name]
            check = input('Enter your password to login: ')
            print(acc.password,check)
            if check == acc.password:
                print('Login Successful')
            else:
                print('Invalid Password , Try again !')
                continue
            while True:
                sub_choice = int(input('\n1.Deposit\n2.Withdrawl\n3.check balance\n4.Transfer\n5.Transactions\n6.Exit'))
                if sub_choice==1:
                    amt = float(input('Enter amount to deposit'))
                    acc.deposit(amt)
                elif sub_choice==2:
                    amt = float(input('Enter amount to withdraw'))
                    acc.withdrawl(amt)
                elif sub_choice==3:
                    acc.check_balance()
                elif sub_choice==4:
                    reciever = input('Enter reciever name')
                    if reciever in accounts:
                        amt = int(input('Enter amount to transfer'))
                        acc.transfer(accounts[reciever],amt)
                    else:
                        print('Reciever Not Found')
                elif sub_choice==5:
                    print(acc.transactions)
                elif sub_choice==6:
                    break
                else:
                    print('Invalid Choice')
                save_accounts(accounts)
    elif choice==3:
        print('Thankyou !')
        save_accounts(accounts)
        break
    else:
        print('Invalid Choice')