def search_replace(txt1):
    words = txt1
    words_split = words.split()
    search_word = input("Enter the word to search : ")
    replace_word = input("Enter the word to replace with : ")
    for x in range(0,len(words_split)):
        if words_split[x] == search_word:
            words_split[x] = words_split[x].replace(search_word, replace_word)
    str1 = ' '.join(words_split)
    print(str1)
            
    
def get_text():
    Text = input("Start typing : ")
    return Text

def main():
    Text = get_text()
    search_replace(Text)

#Main starts from here
main()
