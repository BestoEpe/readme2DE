
import serial
import datetime
import mariadb


arduino = serial.Serial("/dev/ttyACM0")
arduino.baudrate=9600

conn = mariadb.connect(user='root', password='HyTe', host='localhost', database= 'Tiedot');
cur = conn.cursor()

while True:
    data = arduino.readline()
    #print (int(data.decode('utf-8').replace('\n','').replace('\r','').replace('\t','').split(" ")[1]))
    print(data.decode('utf-8').replace('\n','').replace('BPM: ','').replace('\r','').replace('\t',''))
    print(datetime.datetime.now())
    intoDB = data.decode('utf-8').replace('\n','').replace('BPM: ','').replace('\r','').replace('\t','')
    
    cur.execute(f"INSERT INTO Mittari (arvo, pvm) VALUES ({intoDB}, '{datetime.datetime.now()}')")
    #("+data.decode('utf-8').replace('\n', '').replace('\r','').replace('\t','').split(" ")[1]+") ")
    

    conn.commit()

conn.close()
