def max_or_min(lst1):
    print("Maximum number in the list is : ", max(lst1[:-1]))
    print("Minimum number in the list is : ", min(lst1[:-1]))

def number1(lst):
    for x in lst[:-1]:
        if x < 10:
            print("Entered number is single digit : " , x)
        elif x < 100:
            print("Entered number is two digit : ", x)
        elif x < 1000:
            print("Entered number is three digit : ", x)
        else:
            print("Entered number is : ", x)


def main():
    infinity = float('inf')
    Number = input("Enter a number : ")
    Number = int(Number)
    list = []
    list.append(Number)
    while Number < infinity:
        if Number == 0:
            break
        else:
            Number = input("Enter a number : ")
            Number = int(Number)
            list.append(Number)


    max_or_min(list)
    number1(list)
        
#Main starts from here
main()

