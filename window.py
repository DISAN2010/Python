import random

def seed(file):
    try:
        print("\nContents in file : ")
        with open(file, "r") as FH:
            all_lines = FH.read()
            print(all_lines)
        
    except IOError:
        print("Could not open file")
    except:
        print("Oops")
    
def slice(length, start, end, file):
    
    with open(file, "r") as FH:
        FH.seek(start)
        part_lines = FH.read(end)
        print("Characters in text starting between", str(start)+"th", "and ending with", str(end)+"th", "are : ", part_lines)
        Random = random.sample(part_lines, length)

        for x in range(0, len(Random)):
            while Random[x] == ' ':
                Random[x] = random.sample(part_lines, 1)
                Random[x] = ''.join(Random[x])
                if Random[x] == ' ':
                    Random[x] = random.sample(part_lines, 1)
                    Random[x] = ''.join(Random[x])
                else:
                    break
        
        return Random
    
def get_inputs():
    length = input("Enter the length to pick randomly from text: ")
    length = int(length)
    start = input("Enter the starting point to start from text: ")
    start = int(start)
    end = input("Enter the ending point to end from text: ")
    end = int(end)
    return length, start, end

def get_file():
    file = input("File to open : ")
    file = file +".txt"
    return file

def main():
    if __name__ == "__main__":
        File = get_file()
        seed(File)
        Length, Start, End = get_inputs()
        Random = slice(Length, Start, End, File)
        Random = ','.join(Random)
        print("\nRandom", Length, "sequential characters between", str(Start)+"th", "and", str(End)+"th", "character in text is :", Random)

#Main starts from here
main()
