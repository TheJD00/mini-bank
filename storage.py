from Bank import Bank
import json
FILE = 'data/accounts.json'
def save_accounts(accounts):
    data = {user : acc.get_data() for user,acc in accounts.items()}
    with open(FILE,'w') as f:
        json.dump(data,f,indent=4)
def load_accounts():
    try:
        with open(FILE,'r') as f:
            data = json.load(f)
            return {user: Bank.from_dict(acc) for user,acc in data.items()}
    except FileNotFoundError:
        return {}