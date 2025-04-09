from datetime import datetime

class Bank:
    def __init__(self, name, balance):
        self.name = name,
        self.__balance = balance
        self.__history = []

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")
        self.__history.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> Deposited: {amount}")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            self.__history.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance
    
    def get_history(self):
        print(f"Transaction History: {self.name}")
        for entry in self.__history:
            print(entry)
        print("Current Balance:", self.__balance)

    def transfer(self, reciver, amount):
        if (amount > self.__balance):
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            reciver.__balance += amount
            self.__history.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> {amount} Transferred to {reciver.name}")
            reciver.__history.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} --> {amount} Received from {self.name}")


c1 = Bank("Alice", 1000)
c2 = Bank("Bob", 2000)

c1.deposit(500)
c2.deposit(1000)

print(c1.get_balance())
print(c2.get_balance())

c1.withdraw(200)
c2.deposit(10)
c1.deposit(500)
c2.withdraw(1000)

c1.transfer(c2, 100)
c2.transfer(c1, 300)

c1.get_history()
c2.get_history()




























































































































































































































































































































































