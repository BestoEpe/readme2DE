# readme2DE
monkemafia124
import serial

import time

import nariadb



from datetime import datetime



device=/dev/ttyACMG

try:

print ("Availee arduinoa", device) arduino serial.Serial (device, 9600)



except:

print ("Arduinoa ei saatu kiinni: ", device)



conn-mariadb.connect(user-"root", password-"HyTe", host-"localhost", database="Tiedot") cur conn.cursor()

while true:



try:

time.sleep (5)

now datetime.now()

dt string = now.strftime("%d/%m/%Y %H:%M:%S")

print (dt_string)

data arduino.readLine() print (data.decode('utf-8').replace("\n", ").replace("\r', ' '))

cur.execute("INSERT INTO Mittari (pvm, arvo) VALUES (adt_string","adata.decode('utf-8').replace("\n", "').replace("\n", *)***)

conn.commit()

except:

print ("Loopin koodi ei toiminut").

conn.close()
