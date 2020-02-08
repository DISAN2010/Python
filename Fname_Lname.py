def names(fname, lname):
    print("Name : ", fname.lower(), ", Surname : ", lname.lower())
    print(fname.upper(), lname.upper())
    print("---------------------  ---------")
    print(lname, ",", fname)

def get_input():
    Fname = input("Enter your first name : ")
    Lname = input("Enter your last name : ")
    return Fname, Lname

def main():
    First_name, Last_name = get_input()
    names(First_name, Last_name)

#Main starts from here
main()
