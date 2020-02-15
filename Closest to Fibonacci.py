def main():
    Number = input("Enter a number : ")
    Number = int(Number)
    First_number = 0
    Second_number = 1
    counter = 0
    infinity = float('inf')
    while counter < infinity:
        Fibonacci_series = First_number + Second_number
        if First_number == Number or Second_number == Number:
            print("Fibonacci Series : ", Number)
            break
        elif(First_number < Number and Second_number > Number):
            print(First_number, Number, Second_number)
            a = Number - First_number
            b = Second_number - Number
            if a < b:
                print("Closest Number : ", First_number)
            else:
                print("Closest Number : ", Second_number)
        First_number = Second_number
        Second_number = Fibonacci_series
    counter += 1
          

#Main starts from here
main()
