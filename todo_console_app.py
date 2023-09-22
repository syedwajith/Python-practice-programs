import os
from datetime import datetime

class ToDo:
    def __init__(self):
        self.todo_users = []
        self.tasks = []

    def validate_account(self, phone_no):
        for i in range(len(self.todo_users)):
            if self.todo_users[i]["phone_no"] == phone_no:
                return False
        return True 
    
    def account_verification(self, phone_no, password):
        t = (False, None)
        for i in range(len(self.todo_users)):
            if self.todo_users[i]["phone_no"] == phone_no:
                if self.todo_users[i]["password"] == password:
                    user = self.todo_users[i]
                    t = (True, user)
                    return t
        return t

    def create_account(self, name, phone_no, password):
        user_detail = {"name":name, "phone_no":phone_no, "password":password}
        self.todo_users.append(user_detail)

    def add_task(self, task, user_value):
        date = datetime.today().date()
        user_dict_val = {
            "name": user_value["name"], 
            "phone_no": user_value["phone_no"], 
            "password": user_value["password"],
            "task": task,
            "date": date
            }
        self.tasks.append(user_dict_val)

    def view_task(self, phone_no, password, name):
        print(f"Name : {name}")
        print(f"Phone No : {phone_no}")
        for i in range(len(self.tasks)):
            if self.tasks[i]["phone_no"] == phone_no and self.tasks[i]["password"] == password:
                print(f"Task : {self.tasks[i]['task']}")
                print(f"Date : {self.tasks[i]['date']}")

    def delete_task(self, phone_no, password, op):
        if op == "1":
            try:
                for i in range(len(self.tasks)):
                    if self.tasks[i]["phone_no"] == phone_no and self.tasks[i]["password"] == password:
                        self.tasks.remove(self.tasks[i])
                return True
            except:
                return False
            
        elif op == "2":
            try:
                for i in range(len(self.tasks)):
                    if self.tasks[i]["phone_no"] == phone_no and self.tasks[i]["password"] == password:
                        self.tasks.remove(self.tasks[i])
                        break
            except:
                return False

        elif op == "3":
            try:
                for i in range(len(self.tasks)-1, -1, -1):
                    if self.tasks[i]["phone_no"] == phone_no and self.tasks[i]["password"] == password:
                        self.tasks.remove(self.tasks[i])
                        break
                return True
            except:
                return False

def main():
    todo = ToDo()

    while True:
        print("1. Create Account")
        print("2. Add Task")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        n = input("Choose your option : ")

        if n == "1":
            name = input("Enter your name : ")
            phone_no = input("Enter your phone number : ")

            while (len(phone_no) != 10) or (not phone_no.isdigit()):
                phone_no = input("Please enter valid phone number : ")

            account_validation = todo.validate_account(phone_no)

            while account_validation == False:
                print("Phone number is already exists.")
                phone_no = input("Please enter valid phone number : ")

                while (len(phone_no) != 10) or (not phone_no.isdigit()):
                    phone_no = input("Please enter valid phone number : ")

                account_validation = todo.validate_account(phone_no)

            password = input("Enter your password : ")
            confirm_password = input("Retype your password : ")

            while password != confirm_password:
                print("Password is not matched...")
                confirm_password = input("Retype your password : ")

            todo.create_account(name, phone_no, password)
            os.system("cls")
            print("Account created successfully!!!")

        elif n == "2":
            phone_no = input("Enter your phone number : ")
            validation_phone_no = todo.validate_account(phone_no)

            if validation_phone_no:
                print("Sorry!!! Account is not there...")
            else:
                password = input("Enter your password : ")
                verify_acc, user_value = todo.account_verification(phone_no, password)

                while True:
                    if verify_acc:
                        task = input("Enter your task : ")
                        todo.add_task(task, user_value)
                        os.system("cls")
                        print("Task added successully!!!")
                        no = input("If you want to add another task press 1 or press 0 : ")

                        while no == "1":
                            task = input("Enter your task : ")
                            todo.add_task(task, user_value)
                            os.system("cls")
                            print("Task added successully!!!")
                            no = input("If you want to add another task press 1 or press 0 : ")

                        break
                    else:
                        password = input("Please enter your correct password : ")
                        verify_acc, user_value = todo.account_verification(phone_no, password)

        elif n == "3":
            phone_no = input("Enter your phone number : ")
            validation_phone_no = todo.validate_account(phone_no)

            if validation_phone_no:
                print("Sorry!!! Account is not there...")
            else:
                password = input("Enter your password : ")
                verify_acc, user_value = todo.account_verification(phone_no, password)

                while True:
                    if verify_acc:
                        name = user_value["name"]
                        os.system("cls")
                        todo.view_task(phone_no, password, name)
                        break
                    else:
                        password = input("Please enter your correct password : ")
                        verify_acc, user_value = todo.account_verification(phone_no, password)

        elif n == "4":
            phone_no = input("Enter your phone number : ")
            validation_phone_no = todo.validate_account(phone_no)

            if validation_phone_no:
                print("Sorry!!! Account is not there...")
            else:
                password = input("Enter your password : ")
                verify_acc, user_value = todo.account_verification(phone_no, password)

                while True:
                    if verify_acc:
                        print("1. Delete all tasks")
                        print("2. Delete first task")
                        print("3. Delete last task")
                        print("4. logout")

                        op = input("Choose your option : ")

                        if op == "1":
                            delete_val = todo.delete_task(phone_no, password, op)
                            if delete_val:
                                os.system("cls")
                                print("All tasks are deleted successfully!!!")
                            else:
                                print(None)

                        elif op == "2":
                            delete_val = todo.delete_task(phone_no, password, op)
                            if delete_val:
                                os.system("cls")
                                print("First task deleted successfully!!!")
                            else:
                                print(None)

                        elif op == "3":
                            delete_val = todo.delete_task(phone_no, password, op)
                            if delete_val:
                                os.system("cls")
                                print("Last task deleted successfully!!!")
                            else:
                                print(None)

                        elif op == "4":
                            os.system("cls")
                            break
                    else:
                        password = input("Please enter your correct password : ")
                        verify_acc, user_value = todo.account_verification(phone_no, password)

        elif n == "5":
            os.system("cls")
            print("Thank You!!! Good Bye!!!")
            break
        else:
            print("Please choose correct option")

if __name__ == "__main__":
    main()