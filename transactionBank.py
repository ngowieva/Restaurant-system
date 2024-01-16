import json

class Bank:
    
    def __init__(self, filename):
        self.filename = filename
        self.user = {}
        
    def load_user(self):
        try:
            with open(self.filename, 'r') as file:
                self.user = json.load(file)
        except FileNotFoundError:
            pass
    
    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.user, file)
            
    def withdraw(self, username):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= self.user[username]['balance']:
            self.user[username]['balance'] -= amount
            print(f"Withdraw completed. Your new balance is $ {self.user[username]['balance']}")
        else:
            print("Insufficient funds. Withdraw failed.")
            
    def deposit(self, username):
        amount = float(input('Enter amount to deposit: '))
        self.user[username]['balance'] += amount
        print(f"Deposit complete. Your new balance is $ {self.user[username]['balance']}")        
             
    def register_user(self):
        username = input('Enter username: ')
        password = input('Enter password: ')
        initial_balance = float(input('Enter initial balance: '))
        
        if username not in self.user:
            self.user[username] = {'password': password, 'balance': initial_balance}
            print(f"User '{username}' registered successfully")
        else:
            print("Username already exists. Please choose a different username")
            
    def login(self, username, password):
        if username in self.user and self.user[username]['password'] == password:
            print('Welcome', username)
            return True
        else:
            print('Invalid username or password. Try again')
            return False

# Specify file to store user info
filename = 'user_data.json'
                
# Create object
my_bank = Bank(filename) 
my_bank.load_user()

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input('Enter your choice (1-3):\n ')
    if choice == '1':
        my_bank.register_user()
    elif choice == '2':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        
        if my_bank.login(username, password):
            while True:
                print(f"Current balance: $ {my_bank.user[username]['balance']}")
                print("\n4. Deposit")
                print("5. Withdraw")
                print("6. Logout")
                sub_choice = input('Enter your choice (4-6): ')
                
                if sub_choice == '4':
                    my_bank.deposit(username)
                elif sub_choice == '5':
                    my_bank.withdraw(username)
                elif sub_choice == '6':
                    print('Logout successful. See you later.')
                    break
                else:
                    print('Invalid choice')
    elif choice == '3':
        my_bank.save_users()
        print('Exiting the program')
        break
    else:
        print('Invalid choice')
