def digits(num1):
    if num1 < 10:
        num1 = num1 + 7
        print("Single digit added with 7 is : ", num1)
        num1 = str(num1)
        print("Number in its unit place is : ", num1[-1])
    elif num1 < 100:
        num1 = num1 ** 5
        print("Two digit power to the 5 is : ", num1)
        num1 = str(num1)
        print("Last 2 digit of the number is : ", num1[-2:])
    else:
        num2 = input("Enter another number : ")
        num2 = int(num2)
        num1 = num2 + num1
        print("Sum of 2 numbers : ", num1)
        num1 = str(num1)
        print("Last 3 digits of the number is : ", num1[-3:])

def get_number():
    Number = input("Enter a number : ")
    Number = int(Number)
    return Number

def main():
    Number = get_number()
    digits(Number)

#Main starts from here
main()
