def tank(num1, num2):
    Litres_percentage = (num1 / num2) * 100
    print("Litres in percentage : ", Litres_percentage)
    if Litres_percentage > 80:
        print("Alarm to close the valve!!!")
    elif Litres_percentage < 20:
        print("Need to buy more liquid to fill up the tank!!")
    else:
        print("Everything is ok")

def get_valve():
    num1 = input("Enter current level of ethanol in the tank : ")
    num1 = int(num1)
    return num1

def main():
    Tank_capacity = 900
    Valve = get_valve()
    tank(Valve , Tank_capacity)

#Main starts from here
main()
