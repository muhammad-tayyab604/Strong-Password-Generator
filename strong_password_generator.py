import string
import random
import tkinter as tk
import customtkinter as ctk

characters=list(string.ascii_letters + string.digits + "!@#$%^&*()_+}{|:?><'")

def generat_random_password():
    length=int(input("Enter the length of the password:\n"))


    random.shuffle(characters)

    password=[]
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

generat_random_password()
while True:
    length=int(input("If you are not satisfy from this password please enter the length of the password AGAIN!:\n"))
    random.shuffle(characters)

    password=[]

    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))



    

