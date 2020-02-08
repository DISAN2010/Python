def statistics(lst1):
    Balls_faced = len(lst1)
    print("Balls faced : ", Balls_faced)
    Dots = 0
    Fours = 0
    Sixes = 0
    for x in lst1:
        if x == '0':
            Dots = Dots + 1
        elif x == '4':
            Fours = Fours + 1
        elif x == '6':
            Sixes = Sixes + 1
            
    Balls_faced = int(Balls_faced)
    lst1 = [int(i) for i in lst1[:-1]]
    Total_score = sum(lst1)
    print("Total score is : ", Total_score)
    Strike_rate = (Total_score / Balls_faced) * 100
    print("Strike rate is : ", Strike_rate)

    print("No. of balls wasted : ", Dots + 1)
    print("No. of fours : ", Fours)
    print("No. of sixes : ", Sixes)
        
def match(num1):
        infinity = str('inf')
        lst = []
        lst.append(num1)
        while num1 < infinity:
            if num1 == '':
                print("Out he is gone")
                break
            else:
                num1 = input("Runs scored by the batsmen : ")
                num1 = str(num1)
                if num1 == '.':
                    num1 = num1.replace(".", "0")
                lst.append(num1)

        statistics(lst)
    
def get_number():
    Number = input("Runs scored for the current ball : ")
    Number = str(Number)
    return Number

def main():
    Number = get_number()
    for x in Number:
        if x == '':
            print("Out for the first ball")
            break
        else:
            match(Number)    
    
#Main starts from here
main()
