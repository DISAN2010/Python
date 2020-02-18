def passcode(Random_num, num1):
    lst = []
    
    a = Random_num - 1
    b = Random_num - 2
    c = Random_num + 1
    d = Random_num + 2
    
    count = 1
    attempts = 4
    
    while count < attempts:
        if num1 == Random_num:
            print("Welcome!!!")
            break
        elif num1 > 0 and num1 < b:
            print("invalid passcode")
            num1 = input("Enter Passcode : ")
            num1 = int(num1)
            lst.append(num1)
        elif num1 > d:
            print("INVALID PASSCODE")
            num1 = input("Enter Passcode : ")
            num1 = int(num1)
            lst.append(num1)
        elif num1 == a or num1 == b or num1 == c or num1 == d:
            print("InVaLiD PaSsCoDe")
            num1 = input("Enter Passcode : ")
            num1 = int(num1)
            lst.append(num1)

        count +=1

    else:
        if num1 > 0 and num1 < b:
            print("invalid passcode")
        elif num1 > d:
            print("INVALID PASSCODE")

        for x in lst:
            if x == a or x == b or x == c or x == d:
                num1 = input("Enter Passcode : ")
                num1 = int(num1)
                break
        if num1 == Random_num:
            print("Welcome!!!")
        else:
            print("Login FAILED!!!")    

def get_numbers():
    random_no = input("Choose Random number : ")
    random_no = int(random_no)
    number = input("Enter Passcode : ")
    number = int(number)    
    return random_no, number

def main():
    Random_no, number = get_numbers()
    passcode(Random_no, number)

#Main starts from here
main()
