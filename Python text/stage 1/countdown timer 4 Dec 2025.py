import time
timer=int(input("write your timer: "))
while timer >= 0:
    print(timer)
    timer -=1
    time.sleep(1)