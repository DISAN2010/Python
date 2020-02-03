"""
Total percentage marks and rank the student
"""

def percentage_english(num1):
    English = 80
    Result = (num1/English) * 100
    if Result >=90 and Result <= 100:
        print("First Class")
    elif Result >=75 and Result < 90:
        print("Second Class")
    elif Result >=36 and Result < 75:
        print("Average")
    elif Result <=35 and Result >= 0:
        print("Failed")
    else:
        print("Please enter your marks correctly")

def percentage_science(num2):
    Science = 90
    Result = (num2/Science) * 100
    if Result >=90 and Result <= 100:
        print("First Class")
    elif Result >=75 and Result < 90:
        print("Second Class")
    elif Result >=36 and Result < 75:
        print("Average")
    elif Result <=35 and Result >= 0:
        print("Failed")
    else:
        print("Please enter the marks correctly")

def percentage_mathematics(num3):
    Mathematics = 100
    Result = (num3/Mathematics) * 100
    if Result >=90 and Result <= 100:
        print("First Class")
    elif Result >=75 and Result < 90:
        print("Second Class")
    elif Result >=36 and Result < 75:
        print("Average")
    elif Result <=35 and Result >= 0:
        print("Failed")
    else:
        print("Please enter the marks correctly")
        
def get_scores():
    English_Marks = input("Enter your English Marks : ")
    English_Marks = int(English_Marks)
    Science_Marks = input("Enter your Science Marks : ")
    Science_Marks = int(Science_Marks)
    Mathematics_Marks = input("Enter your Mathematics Marks : ")
    Mathematics_Marks = int(Mathematics_Marks)
    return English_Marks, Science_Marks, Mathematics_Marks
    
def main():
    English_Marks, Science_Marks, Mathematics_Marks = get_scores()
    percentage_english(English_Marks)
    percentage_science(Science_Marks)
    percentage_mathematics(Mathematics_Marks)

#Main starts from here
main()
