def digits(number):
    number = str(number)    
    print("The number of digits in the number is : ", len(number))

def get_number():
    num1 = input("Enter a number : ")
    num1 = int(num1)
    return num1

def main():
    Number = get_number()
    digits(Number)

#Main starts from here
main()
