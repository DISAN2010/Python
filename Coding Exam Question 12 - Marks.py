def maths_marks(num4):
    Max_marks = 100
    print("Total marks in Maths ", num4)
    Student_Percent = (num4 / Max_marks) * 100
    if Student_Percent > 90 and Student_Percent <= 100:
        print("Grade A in Mathematics")
    elif Student_Percent > 75 and Student_Percent <= 90:
        print("Grade B in Mathematics")
    elif Student_Percent > 34 and Student_Percent <= 75:
        print("Average grade in Mathematics")
    elif Student_Percent < 35 and Student_Percent > 0:
        print("Failed in Mathematics")
    else:
        print("Enter correct marks")

def science_marks(num2, num3):
    Max_marks = 100
    Student_Mark = num2 + num3
    print("Total marks in Science ", Student_Mark)
    Student_Percent = (Student_Mark / Max_marks) * 100
    if Student_Percent > 90 and Student_Percent <= 100:
        print("Grade A in Science")
    elif Student_Percent > 75 and Student_Percent <= 90:
        print("Grade B in Science")
    elif Student_Percent > 34 and Student_Percent <= 75:
        print("Average grade in Science")
    elif Student_Percent < 35 and Student_Percent > 0:
        print("Failed in Science")
    else:
        print("Enter correct marks")    


def english_marks(num1):
    Max_marks = 75
    print("Total marks in English ", num1)
    Student_Percent = (num1 / Max_marks) * 100
    if Student_Percent > 90 and Student_Percent <= 100:
        print("Grade A in English")
    elif Student_Percent > 75 and Student_Percent <= 90:
        print("Grade B in English")
    elif Student_Percent > 24 and Student_Percent <= 75:
        print("Average grade in English")
    elif Student_Percent < 25 and Student_Percent > 0:
        print("Failed in English")


def get_scores():
    english = input("Enter your English Marks : ")
    english = int(english)

    while english > 75:
        print("Enter correct marks")
        english = input("Enter your English Marks : ")
        english = int(english)
        
    science_theory = input("Enter your Science Theaory Marks : ")
    science_theory = int(science_theory)

    while science_theory > 75:
        print("Enter correct marks")
        science_theory = input("Enter your Science Theory Marks : ")
        science_theory = int(science_theory)
        
    science_practical = input("Enter your Science Practical Marks : ")
    science_practical = int(science_practical)
    
    while science_practical > 26:
        print("Enter correct marks")
        science_practical = input("Enter your Science Practical Marks : ")
        science_practical = int(science_practical)
            
    mathematics = input("Enter your Mathematics Marks : ")
    mathematics = int(mathematics)
    
    while mathematics > 100:
        print("Enter correct marks")
        mathematics = input("Enter your Maths Marks : ")
        mathematics = int(mathematics)
        
    return english, science_theory, science_practical, mathematics

def main():
    English, Science_Theory, Science_Practical, Mathematics = get_scores()
    english_marks(English)
    science_marks(Science_Theory, Science_Practical)
    maths_marks(Mathematics)

#Main starts from here
main()
