def names(fname, lname):
    print(fname, lname)
    for x in fname:
        for y in lname:
            a = fname[0:-1]
            b = lname[0:-1]
            print(fname, lname)
            fname = a
            lname = b

def get_input():
    Fname = input("Enter your first name : ")
    Lname = input("Enter your last name : ")
    return Fname, Lname

def main():
    First_name, Last_name = get_input()
    names(First_name, Last_name)

#Main starts from here
main()
