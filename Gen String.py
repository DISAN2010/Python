def give(num1):
    if num1 == 5:
        print('0'*4+'1'*4+'2'*4+'3'*4+'4'*4)
    else:
        print('0'*2+'1'*2+'2'*2)
        

def get_number():
    Number = input("Enter number 5 or 3 : ")
    Number = int(Number)
    return Number

def main():
    Number = get_number()
    give(Number)

#Main starts from here
main()
