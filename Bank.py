class Bank:
    def __init__(self,user_name,password,balance=0.0):
        self.user_name = user_name
        self.password = password
        self.balance = balance
        self.transactions = []
    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f'Deposited {amount}')
    def withdrawl(self,amount):
        if amount > self.balance:
            print('Insufficient Funds')
            return
        self.balance -= amount
        self.transactions.append(f'Withdrew {amount}')
        print('Withdrawl Successfful')
    def transfer(self,other_account,amount):
        if amount > self.balance:
            print('Insufficient Funds')
            return
        self.balance-=amount
        other_account.balance += amount
        self.transactions.append(f'Transferred {amount} to {other_account.user_name}')
    def get_data(self):
        return{
            'user_name' : self.user_name,
            'password' : self.password,
            'balance' : self.balance,
            'transactions' : self.transactions
        }
    
    @classmethod
    def from_dict(cls,data):
        acc = cls(data['user_name'],data['password'],data['balance'])
        acc.transactions = data.get('transactions',[])
        return acc
    def check_balance(self):
        print(f'Your CUrrent Balance is {self.balance}')