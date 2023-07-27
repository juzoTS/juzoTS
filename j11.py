##import random
##import time
##
##print("dice!")
##
##while 1:
##    value = random.randint(1,6)
##    print("Dice value: %d" %value)
##    time.sleep(2)
##    

##import time
##
##start = int(input("startvalue: "))
##end = int(input("endvalue: "))
##
##
##while start <= end:
##    print("Count: %d" %start)
##    start += 1

##
##start = int(input("startvalue: "))
##end = int(input("endvalue: "))
##
##for start in range(start, end+1, 1):
##    print("count %d" % start)

import sys
start = int(input("start: "))
end = int(input("end :"))

SUM = 0

if start <= end:
    while start <= end:
        print("Count: %d" %start)
        SUM += start
        start += 1
else:
    sys.exit()
