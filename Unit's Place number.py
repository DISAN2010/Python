"""
Print the number in its unit’s place
"""

def digits(num1):
    if num1 < 10:
        num1 = num1 + 7
        print("Total after adding 7 is : ", num1)
        num1 = str(num1)
        num1 = list(num1)
        print("Unit's place is : ", num1[-1])
    elif num1 < 100:
        num1 = num1 ** 5
        print("Total after exponentiation of 5 is : ", num1)
        num1 = str(num1)
        num1 = list(num1)
        print("Unit's place is : ", num1[-1])
    else:
        num2 = input("Enter another number : ")
        num2 = int(num2)
        num1 = num1 + num2
        print("Total after adding both numbers is : ", num1)
        num1 = str(num1)
        num1 = list(num1)
        print("Unit's place is : ", num1[-1])

def get_number():
    num1 = input("Enter the number : ")
    num1 = int(num1)
    return num1

def main():
    Number = get_number()
    digits(Number)

#Main starts from here
main()
