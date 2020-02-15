def main():
    Num=input ("Enter how many numbers to print in Fibonacci series:")
    Num = int(Num)
    First_number = 0
    Second_number = 1
    print(First_number)
    print(Second_number)
    Range = range(2, Num)
    for x in Range:
        Fibonacci_series = First_number + Second_number
        print(Fibonacci_series)
        First_number = Second_number
        Second_number = Fibonacci_series
       
        
#Main starts from here
main()
print("Above are the first 10 Fibonacci series")
