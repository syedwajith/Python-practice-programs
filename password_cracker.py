from random import *
import os

user_pwd = input("Enter your password : ")
pwd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '0','1','2','3','4','5','6','7','8','9']
cracked_pwd = ""

while(cracked_pwd != user_pwd):
    cracked_pwd = ""
    for i in range(len(user_pwd)):
        guess_pwd = pwd[randint(0,len(pwd) - 1)]
        cracked_pwd = str(guess_pwd) + str(cracked_pwd)
        print(cracked_pwd)
        print("Cracking password...Please wait...")
        os.system("cls")
print("Your Password is : ", cracked_pwd)