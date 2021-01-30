import sys

if len(sys.argv) != 2:
    print("\nPlease enter the year to be evaluated as the 1st arguement\n[py \"Written HW 1.py\" 2021]")
    sys.exit()
    
    
year = int(sys.argv[1])
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(str(year) + " is a leap year")
            sys.exit()
    else:
        print(str(year) + " is a leap year")
        sys.exit()

print(str(year) + " is not a leap year")