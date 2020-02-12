"""
Two digit or three digit number
"""

def number2(num2):
    if num2 > 9 and num2 < 100:
        print("Entered number is two digit", num2)
    elif num2 > 99 and num2 < 1000:
        print("Entered number is three digit", num2)
    else:
        print("Entered number is : ", num2)

def number1(num1):
    if num1 > 9 and num1< 100:
        print("Entered number is two digit", num1)
    elif num1 >99 and num1 < 1000:
        print("Entered number is three digit", num1)
    else:
        print("Entered number is : ", num1)

def get_number():
    num1 = input("Enter a number : ")
    num1 = int (num1)
    num2 = input("Enter another number : ")
    num2 = int(num2)
    return num1, num2

def main():
    First, Second = get_number()
    number1(First)
    number2(Second)

#Main starts from here
main()
