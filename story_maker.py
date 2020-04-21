import sys
from window import get_inputs,seed,slice

def new_file(random):
    with open("your_story.txt", "w") as WFH:
        WFH.write("# Created by story_maker.py\n")
        WFH.write("\n"+random+"\n")
        WFH.write("\n# Copyright, DISAN 2019")
        
    with open("your_story.txt", "r") as RFH:
        all_lines = RFH.read()
        print(all_lines)

def main():
    if __name__ == "__main__":
        File = sys.argv[1]
        seed(File)
        Length, Start, End = get_inputs()
        Random = slice(Length, Start, End, File)
        Random = ''.join(Random)
        new_file(Random)
        
#Main starts from here
main()
