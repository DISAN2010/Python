def vowel_a(str2):
    infinity = float('inf')
    length = len(str2)
    index = 0
    lst = []
    while length < infinity:
        A_vowel = str2.find("a", index)
        if A_vowel == -1:
            break
        else:
            lst.append(A_vowel)
            index = A_vowel + 1

    print("Number of words containing vowel A is : ", len(lst))

                       
def words(str1):
    sent = str1.split()
    No_of_words = len(sent)
    print("Number of words in the sentence : ", No_of_words)

def get_input():
    String = input("Start typing : ")
    return String

def main():
    Sentence = get_input()
    print(Sentence)
    words(Sentence)
    vowel_a(Sentence)


#Main starts from here
main()
