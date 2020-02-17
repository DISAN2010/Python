def sqrt(lst1):
    for num in lst1:
        if num > 99 and num < 1000:
            num = num ** 0.5
            print("Sqrt of three digit num is : ", num)
        else:
            print("Entered number is not a three digit: ", num)            

    
def digits(num1):
    lst = []
    lst.append(num1)
    infinity = float('inf')
    while num1 < infinity:
        if num1 == 0:
            break
        else:
            num1 = input("Enter 3 digit number : ")
            num1 = int(num1)
            lst.append(num1)

    sqrt(lst[:-1])

def get_num():
    number = input("Enter 3 digit number : ")
    number = int(number)
    while number == 0:
        break
    return number

def main():
    Number = get_num()
    digits(Number)

#Main starts from here
main()
