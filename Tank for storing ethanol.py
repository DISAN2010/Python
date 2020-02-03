"""
A Chemical plant has a tank for storing ethanol
"""

def tank(num1, num2, num3):
    if num1 > num2:
        print("Alarm to close the valve!!!")
    elif num1 < num3:
        print("Need to buy more liquid to fill up the tank!!")
    else:
        print("Everything is ok")
    

def get_valve():
    num1 = input("Enter current level of ethanol in the tank : ")
    num1 = int(num1)
    return num1

def main():
    Tank_capacity = 900
    Range1 = 80
    Range2 = 20
    Valve = get_valve()
    tank(Valve , Range1, Range2)

#Main starts from here
main()
