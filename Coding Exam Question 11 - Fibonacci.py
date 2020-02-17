def main():
    counter = 0
    First_no = 1
    Second_no = 1
    count = 2
    infinity = float('inf')
    print("Below are the  first 12 even Fibonacci numbers : ")
    
    while count < infinity:
        Fibonacci = First_no + Second_no
        if First_no % 2 == 0:
            print(First_no)
            counter += 1
        elif counter == 12:
            break
        
        First_no = Second_no
        Second_no = Fibonacci
        count += 1

#Main starts from here
main()
