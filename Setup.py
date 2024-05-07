import subprocess

print("""
██╗░░░██╗░█████╗░██╗██████╗░░░░░░░░█████╗░░██████╗
██║░░░██║██╔══██╗██║██╔══██╗░░░░░░██╔══██╗██╔════╝
╚██╗░██╔╝██║░░██║██║██║░░██║█████╗██║░░██║╚█████╗░
░╚████╔╝░██║░░██║██║██║░░██║╚════╝██║░░██║░╚═══██╗
░░╚██╔╝░░╚█████╔╝██║██████╔╝░░░░░░╚█████╔╝██████╔╝
░░░╚═╝░░░░╚════╝░╚═╝╚═════╝░░░░░░░░╚════╝░╚═════╝░
""")

name = input("Please enter your User Name to be displayed: ")
password = input("Please enter your password to login: ")

with open ('User/username.txt', 'w') as f:
    f.writelines(name)

with open ('User/password.txt', 'w') as f:
    f.writelines(password)

Setup_Done = 'sd'

with open ('User/Setup_Done.txt', 'w') as f:
    f.writelines(Setup_Done)

print("Setup complete")
input("Press enter to open the login window: ")
subprocess.run(["python", "Login.py"])