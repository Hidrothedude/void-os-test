import subprocess
import platform
import socket
import time
import os

os.system("cls")

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Void Terminal [Version 1.00]")
while True:
	code = input(">>> ")
	if code == 'ping':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))
	if code == 'local':
		print("Your Local IPS Is: " + host_ip)
		print("Your Desktop Name Is: " + host_name)
	if code == 'date':
		print("The Local Date Is: " + time.strftime("%d/%m/%Y"))
	if code == 'list':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)
	if code == 'list -a':
		file = input("Enter The Direct File Path To Read: ")
		dir_list2 = os.listdir(file)
		print("Files and directories in '", file, "':")
		print(dir_list2)
	if code == 'help':
		print("these are all the commands and what they do")
		print("ping  ping a website a amount of times")
		print("local it shows you your local ips and your desktop name")
		print("date it will show you your local date")
		print("list will list all files in c:/")
		print("list -a will list all file in a path")
		print("help it will show you all the commands and what they do")
		print("clear it will clear the screen")
		print("bios this is how to change your name and your password")
		print("exit it will exit the terminal and go back to the main menu")
	if code == 'clear':
		os.system("cls")
	if code == 'bios':
		login_name = open('User/username.txt')
		login_password = open('User/password.txt')   
		l_un = login_name.read()
		l_p = login_password.read()

		while True:
			login = input(str("Please enter the password for " + l_un + " to open bios: "))
			if login == l_p:

				os.system("cls")

				print("Opening bios")
				os.system("cls")
				print("[1] User name: " + l_un)
				print("[2] Password: " + l_p)
				print("Host Name: " + host_name)
				print("Local ips: " + host_ip)

				edit_b = input("Enter [?] to change setting: ")
				if edit_b == '1':
					edit_n = input("Enter new username: ")
					with open('User/username.txt', 'w') as f:
						f.writelines(edit_n)
					print("Your Username has been changed to " + edit_n)
					input("Press enter to close the window: ")
				
				edit_b = input("Enter [?] to change setting: ")
				if edit_b == '2':
					edit_p = input("Enter new Password: ")
					with open('User/Password.txt', 'w') as f:
						f.writelines(edit_p)
					print("Your Password has been changed to " + edit_p)
					input("Press enter to close the window: ")

			else:
				print("Wrong password for" + l_un)
	if code == 'exit':
		subprocess.run(["python", "home.py"])
