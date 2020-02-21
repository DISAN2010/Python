def search_replace(txt1, str1, str2):
    print("Text what you have typed : ", txt1)
    if str1 in txt1:
        txt = txt1.replace(str1, str2)
        print("Text after replaced word : ", txt)
        
def get_text():
    Text = input("Start typing : ")
    Search_word = input("Word to search : ")
    Replace_word = input("Word to replace ; ")
    return Text, Search_word, Replace_word

def main():
    Text, Search_word, Replace_word = get_text()
    search_replace(Text, Search_word, Replace_word)

#Main starts from here
main()
