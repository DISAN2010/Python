def max_occ_words(book):
    try:
        with open(book, "r") as FH:
            Words = dict()
            all_text = FH.read()
            lines = all_text.split()
            for x in lines:
                if len(x) < 5 or x.startswith("H") or x.startswith("T") or x.startswith("W") or x.startswith("Y"):
                    continue
                else:
                    word = x
                    occurence = lines.count(x)
                    Words[word] = occurence

            def get_occ(word):
                return Words.get(word)

            count = 0
            print("Top 50 most repeated words are : \n")
            for key in sorted(Words, key=get_occ, reverse=True):
                if count < 50:
                    print(key, Words[key])
                count += 1
                if count == 50:
                    break

    except IOError:
        print("Could not open")
    except:
        print("OOps")

def get_book():
    book = "Oliver Twist.txt"
    return book

def main():
    Book = get_book()
    max_occ_words(Book)

#Main starts form here
main()
