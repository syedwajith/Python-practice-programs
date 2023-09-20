import random
import os

class Bank:
    def __init__(self):
        self.accounts = []

    def validate_account(self, account_no, pin):
        t = ()
        for i in range(len(self.accounts)):
            if self.accounts[i]["account_no"] == account_no:
                if self.accounts[i]["account_no"] == account_no and self.accounts[i]["pin"] == pin:
                    t = (True, i, True)
                    return t
                else:
                    t = (False, i, True)
                    return t
                
        t = (True, 0, False)
        return t
    
    def validate_acc(self, account_no):
        t = (False, 0, None, None)
        for i in range(len(self.accounts)):
            if self.accounts[i]["account_no"] == account_no:
                name = self.accounts[i]["name"]
                account_no = self.accounts[i]["account_no"]
                t = (True, i, name, account_no)
                return t
            
        return t

    def validate_account_no(self,acc_no):
        for i in range(len(self.accounts)):
            if self.accounts[i]["account_no"] == acc_no:
                self.generate_account_no()
            
        return acc_no

    def generate_account_no(self):
        while True:
            acc_no = ""
            for _ in range(10):
                acc_no += str(random.randint(0,9))

            validate_acc_no = self.validate_account_no(acc_no)

            if acc_no == validate_acc_no:
                return validate_acc_no

    def validate_phone_no(self, ph_no):
        while True:
            for i in range(len(self.accounts)):
                if self.accounts[i]["phone_no"] == ph_no:
                    print("Phone number already exists...")
                    ph_no = input("Please enter your phone number : ")

                    while (len(ph_no) != 10) or (not ph_no.isdigit()):
                        ph_no = input("Please enter your valid phone number : ")

                    self.validate_phone_no(ph_no)

            break

        return ph_no

    def create_account(self, name, phone_no, account_no, pin, amount):
        phone_no_validation = self.validate_phone_no(phone_no)
        account = {"name":name, "phone_no":phone_no_validation, "account_no":account_no, "pin":pin, "balance":amount}
        self.accounts.append(account)

    def withdraw_amount(self, index_val, amount):
        t = (0, False)
        if 0 <= amount <= self.accounts[index_val]["balance"]:
            self.accounts[index_val]["balance"] -= amount
            balance = self.accounts[index_val]["balance"]
            t = (balance, True)
            return t
        else:
            return t

    def deposite_amount(self, index_val, amount):
        self.accounts[index_val]["balance"] += amount

    def balance_enquiry(self, index_val):
        return self.accounts[index_val]["balance"]

def main():
    bank = Bank()
    print("Welcome to our bank!!!")

    while True:
        print("Choose your process...")
        print("1. Create Account")
        print("2. Withdraw Amount")
        print("3. Deposite Amount")
        print("4. Balance Enquiry")
        print("5. Exit")
        n = input("Which process you want ??? : ")

        if n == "1":
            print("Welcome to our Bank!!! \nCreate your account here...")
            name = input("Enter your name : ")
            phone_no = input("Enter your phone number : ")

            while (len(phone_no) != 10) or (not phone_no.isdigit()):
                phone_no = input("Please enter your valid phone number : ")

            account_no = bank.generate_account_no()
            print(f"Your account number : {account_no} ")
            pin = input("Enter your four digit pin : ")

            while (len(pin) != 4) or (not pin.isdigit()):
                pin = input("Please enter your valid four digit pin : ")

            amount = float(input("Initial amount to deposite : "))

            bank.create_account(name, phone_no, account_no, pin, amount)
            os.system("cls")
            print("Account created Successfully!")

        elif n == "2":
            account_no = input("Enter your account number : ")
            pin = input("Enter your four digit pin : ")
            validate, index_val, bool_val = bank.validate_account(account_no, pin)

            while validate == False:
                pin = input("Please enter your valid four digit pin : ")
                validate, index_val, bool_val = bank.validate_account(account_no, pin)

            if bool_val:
                amount = float(input("Enter withdraw amount : "))
                os.system("cls")
                balance, b = bank.withdraw_amount(index_val, amount)

                if b:
                    print(f"Amount withdrawn successfully...\nYour Balance : {balance}")
                else:
                    print("Insufficient Balance!!!")

            else:
                print("Account is not available.")


        elif n == "3":
            account_no = input("Enter your account number : ")
            validate, index_val, name, account_num = bank.validate_acc(account_no)

            if validate:
                print(f"Name : {name}")
                print(f"Account Number : {account_num}")
                amount = float(input("Enter amount to deposite : "))
                deposite = bank.deposite_amount(index_val,amount)
                os.system("cls")
                print("Amount deposited successfully.")
            else:
                print("Account is not available.")

        elif n == "4":
            account_no = input("Enter your account number : ")
            pin = input("Enter your four digit pin : ")
            validate, index_val, bool_val = bank.validate_account(account_no, pin)

            while validate == False:
                pin = input("Please enter your valid four digit pin : ")
                validate, index_val, bool_val = bank.validate_account(account_no, pin)

            if bool_val:
                balance = bank.balance_enquiry(index_val)
                print(f"Your Balance : {balance}")
            else:
                print("Account is not available.")

        elif n == "5":
            os.system("cls")
            print("We will meet again... Thankyou!!! GoodBye!!!")
            break
        else:
            print("Please Choose correct option")

if __name__ == "__main__":
    main()