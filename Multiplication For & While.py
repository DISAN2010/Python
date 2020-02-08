def multiplication(num2):
    x = 1
    while x<11:
        print(num2, "*", x, "=", num2*x)
        x+=1
        
def get_number():
    Number = input("Enter the number to multiply : ")
    Number = int(Number)
    return Number

def main():
    Number = get_number()
    #multiply(Number)
    multiplication(Number)

        
#Main starts from here
main()
