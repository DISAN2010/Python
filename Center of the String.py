def sent(str1):
    infinity = float('inf')
    sentence = str1
    print("Last character of the sentence is : ", sentence[-1])
    print("Last 5 characters of the sentence is : ", sentence[-5:])
    print("2nd and 5th position of the sentence is : ", sentence[1], "and", sentence[4])
    length = len(sentence)
    if length % 2 == 0:
        index = length/2
        index = int(index)
        print(sentence[index-1], sentence[index], sentence[index+1])
    else:
        index = length/2
        index = index-0.5
        index = int(index)
        print(sentence[index-1], sentence[index], sentence[index+1])  
    

def get_input():
    String = input("Start typing : ")
    return String

def main():
    Sentence = get_input()
    print(Sentence)
    sent(Sentence)


#Main starts from here
main()
