from time import sleep
from random import randint, choice
import getpass

colour_list = [
    "\033[36;1m", "\033[31;1m", "\033[32;22m", "\033[33;6m", "\033[0;32m",
    "\033[;1m", "\033[;7m", "\033[;4m", "\033[;6m", "\033[36;7m", "\033[1;31m",
    "\033[4;31m"
]


def Menu_A():
	menu_loop = True
	while menu_loop == True:
		menu_A = input("Input L for Login, or R for Registration >> ").upper()
		if menu_A == "L":
			menu_A = False
			username = login()
			return username
		if menu_A == "R":
			menu_A = False
			username = register()
			return username
		else:
			print("Please Input L, or R")

#Currently Unused Code
#def Menu_B():
#   print(f"Welcome to Burbet Lite's Centre, {username}")
#   print()
#   print("Please Input a number from the list")
#   print("A) Games\nB) Profile\n")
#   menu_loop = True
#   while menu_loop == True:
#     menu_A = input("Please Input a letter from the list >> ").upper()
#     if menu_A == "A":
#       print("N/A")
#       menu_loop = False
#     if menu_A == "B":
#       print("N/A")
#       menu_loop = False
#     else:
#       print("Please Input a letter from the list >> ")


def readfile():
	file = open("login_details.txt", "r")
	file = file.readlines()


def register():
	import datetime
	currenttime = datetime.datetime.now()
	timestamp = currenttime.strftime("%d-%m-%Y %H:%M:%S")

	file = open("login_details.txt", "a")

	print(f"\033{colour_list[0]}Please Enter a username.\033[0m")
	username = input(" >> ").lower()

	print(f"\033{colour_list[0]}Now, Please enter a password.\033[0m")
	password = input(" >> ").lower()

	balance = 1.00
	tier = "bronze"

	file.write(str(f"\n{username},{password},{timestamp},{balance},{tier}"))
	file.close()

	print("...")
	sleep(1)
	print("...")
	sleep(1)
	print("\n" * 4)
	print(
	    f"\033{colour_list[0]}Congratulations, You now have a Bronze Burbet Account\033[0m"
	)
	print()
	return username


def login():
	sleep(0.5)
	print()
	print("Please Input your Login Details...")
	wrong_count = 0
	user_loop = True

	login_details = []
	file = open("login_details.txt", "r")
	lines = file.readlines()
	file.close()

	for line in lines:
		line = line.strip()
		login_details.append(line.split(","))

	while user_loop == True:
		#global username
		username = input("Please Input Username >> ").lower()
		for item in login_details:
			if username == item[0]:
				print("...")
				print("\n" * 2)
				sleep(1)
				print(f"\033{colour_list[4]}Username Accepted\033[0m")
				print()
				sleep(1)
				passwordloop = True
				while passwordloop == True:
					password = getpass.getpass(
					    "Please Input Password (Input is hidden) >> ").lower()
					if password == item[1]:
						print("...")
						print("\n" * 2)
						sleep(1)
						print(f"\033{colour_list[4]}Password Accepted\033[0m")
						print()
						sleep(1)
						passwordloop = False
						return username  ####EXIT POINT

					else:
						print("...")
						print()
						sleep(1)
						print(
						    f"\033{colour_list[10]}Password Not Found, Please Try Again\033[0m"
						)
						wrong_count += 1
					if wrong_count == 8:
						print(f"\033{colour_list[11]}Out of Attempts")
						print()
						passwordloop = False
						auth0()  ####EXIT POINT
		else:
			print("...")
			print()
			sleep(1)
			print(
			    f"\033{colour_list[10]}Username Not Found, Please Try Again\033[0m"
			)
			print()
			sleep(1)
			wrong_count += 1
		if wrong_count == 8:
			print(f"\033{colour_list[11]}Out of Attempts")
			menu_loop = False
			auth0()  ####EXIT POINT


def auth0():
	print()
	print("___________________________________________________________")
	print(
	    f"\033{colour_list[11]}Unfortunately You have been blocked from Burbet Lite for 100 seconds.\033[0m"
	)
	print()
	for wait in range(1, 102):
		wait -= 1
		print(f"\033{colour_list[11]}{wait}...")
		sleep(1)


print(
    f"\033{colour_list[9]}___________________WELCOME TO BURBET LITE___________________\033[0m"
)
print(
    f"\033{colour_list[9]}___________________________V.0.1____________________________\033[0m"
)
print()
sleep(1)

print("___________________________________________________________")
print()
print("Please Login or Register")

username = Menu_A()

print("Entrance Accepted")
print()

print(f"Welcome to Burbet Lite's Centre, {username}")
print()
print("Please Input a number from the list")
print("A) Games\nB) Profile\n")
menu_loop = True
while menu_loop == True:
	menu_A = input("Please Input a letter from the list >> ").upper()
	if menu_A == "A":
		print("N/A")
		menu_loop = False
	if menu_A == "B":
		print("N/A")
		menu_loop = False
	else:
		print("Please Input a letter from the list >> ")
