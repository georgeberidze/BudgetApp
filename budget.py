class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.balance = 0
        self.total_withdraw = 0
        
    def deposit(self, amount, description=""):
        record = {}
        record['amount'] = amount
        record['description'] = description
        self.ledger.append(record)
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            'There are enough funds'
            record = {}
            record['amount'] = -amount
            record['description'] = description
            self.ledger.append(record)
            self.balance -= amount
            self.total_withdraw += amount
            return True
        else:
            'Not enough funds'
            return False
        
    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            'There is enough balance'
            self.withdraw(amount, f"Transfer to {category.category_name}")
            category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            'Not enough balance'
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            'There is sufficient balance'
            return True
        else:
            'Not enough balance'
            return False

    def __str__(self):
        'When Print(Object) is called'
        space = (30 - len(self.category_name))//2
        char = "*"
        text = ""
        text += f"{char*space}{self.category_name}{char*space}\n"     
        for line in self.ledger:
            text += f"{line['description'][:23]}{line['amount']:>{30 - len(line['description'][:23])}.2f}\n"
        text += f"Total: {self.get_balance():.2f}"
        return text 

def create_spend_chart(categories):
    'Outputs the chart of percentages'
    text = ""
    all_withdraws = 0
    for category in categories:
        all_withdraws += category.total_withdraw

    # Print header and bars
    text += "Percentage spent by category\n"
    for percent in range(100,-10, -10):
        text += f"{percent:>3}| "
        for category in categories:
            if percent <= round((category.total_withdraw / all_withdraws)*100, 0):
                text += "o  "
            else:
                text += f"{' '*3}"
        text +="\n"
    text += f"{'-'*(1+(3*len(categories))):>{(5+(3*len(categories)))}}\n"

    # prints the footer
    names = [category.category_name for category in categories]    
    count = 0
    while count < len(max(names, key=len)):
        for letter in names:
            if names.index(letter) == 0:
                'first name'
                text += (" "*5)
            try:
                text += f"{letter[count]}{' '*2}"
            except:
                'There are no more letters'
                text +=(" "*3)
        
        count += 1  
        if count != len(max(names, key=len)):
            'Last line is reached'
            text+="\n"  

    return text