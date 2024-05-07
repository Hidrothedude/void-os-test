import subprocess
import os   

os.system("cls")

print("""
██╗░░░██╗░█████╗░██╗██████╗░░░░░░░░█████╗░░██████╗
██║░░░██║██╔══██╗██║██╔══██╗░░░░░░██╔══██╗██╔════╝
╚██╗░██╔╝██║░░██║██║██║░░██║█████╗██║░░██║╚█████╗░
░╚████╔╝░██║░░██║██║██║░░██║╚════╝██║░░██║░╚═══██╗
░░╚██╔╝░░╚█████╔╝██║██████╔╝░░░░░░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░░░░░░░░╚════╝░╚═════╝░
""")

login_name = open('User/username.txt')
login_password = open('User/password.txt')   
l_un = login_name.read()
l_p = login_password.read()    

while True:
    login = input("Please enter the password for " + l_un + ":")

    if login == l_p:
        subprocess.run(["python", "home.py"])
    
    else:
        print("Wrong password!")