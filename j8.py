import sys

a = int(input("too oruulnu :"))

if a <= 0:
    print("sorog too")
    print("program exits")
    sys.exit()

else:
    if ( a % 2 == 0):
        print("tegsh too")
    else:
        print("songoi too")


