from microbit import *  
while True:  
    raw = pin0.read_analog() * (3300 / 1024.0)
    sleep(500)
    temp_C = ((raw - 500) / 10)
    print(round(temp_C,3))
    sleep(1000)