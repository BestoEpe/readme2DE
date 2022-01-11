import serial
import time 
import mariadb

arduino = serial.Serial("/devttyACM0")
arduino.baudrate=9600

conn = mariadb.connect(user='root', password='SALASANA', host='localhost', database= 'Tulokset');
cur =conn.cursor()

while True:
    data = arduino.readline()
    print (int(data.decode('utf-8').replace('\n', '').replace('\r','').replace('\t', '').split('')[1]))
    cur.execute("INSERT INTO Syke (BPM) VALUES ("+data.decode('utf-8').replace('\n', '').replace('\r','').replace('\t','').split("")[1]+ ") ")

    conn.commit()
    conn.close()