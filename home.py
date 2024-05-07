import time
import os
import socket
import psutil
import subprocess

os.system("cls")

battery = psutil.sensors_battery()
login_name = open('User/username.txt')
login_password = open('User/password.txt')
l_n = login_name.read()
l_p = login_password.read()
while True:

    os.system("cls")

    print("""
██╗░░░██╗░█████╗░██╗██████╗░░░░░░░░█████╗░░██████╗
██║░░░██║██╔══██╗██║██╔══██╗░░░░░░██╔══██╗██╔════╝
╚██╗░██╔╝██║░░██║██║██║░░██║█████╗██║░░██║╚█████╗░
░╚████╔╝░██║░░██║██║██║░░██║╚════╝██║░░██║░╚═══██╗
░░╚██╔╝░░╚█████╔╝██║██████╔╝░░░░░░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░░░░░░░░╚════╝░╚═════╝░
    """)
    print("Welcome " + l_n)
    print("The current date is " + time.strftime("%d/%m/%Y"))
    print("The battery is at: ")
    print(battery.percent)
    print("""
[1]Open web browser
[2]Open text editor
[3]Open file exploer
[4]Open terminal
[5]Close os safley
    """)
    select = input("[?]: ")

    if select == '1':
        subprocess.run(["python", "brows.py"])

    if select == '2':
        subprocess.run(["python", "edit.py"])

    if select == '3':
        subprocess.run(["python", "file.py"])

    if select == '4':
        subprocess.run(["python", "Terminal.py"])

    if select == '5':
        quit