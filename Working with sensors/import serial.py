import serial
import time

ser = serial.Serial('COM5', 9600)
filename = "hc_sr04_data.csv"
with open(filename, 'a') as f: 
    while True:
        try:

            line = ser.readline().decode().strip() #read/decrpydistance
            timestamp = time.strftime('%Y%m%d%H%M%S') #timespamped

            f.write(f"{timestamp},{line}\n") #into the csv
            f.flush()
        except Exception as e:
            print("Error:", e)
            break
