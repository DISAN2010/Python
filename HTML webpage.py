def html(str1, str2, str3, str4, str5):
    #Title = str1.center(30)
    #print(Title, "\n<html>\n <head>\n   <title>\n      ", str2, "\n   </title>\n </head>\n\n <body>\n   <h1>", Header, "</h>\n\n   <p>", str4, "\n   </p>\n\n   <p>", str5, "\n   </p>\n </body>\n</html>")
    print(str1, "\n<html>\n <head>\n   <title>\n      ", str2, "\n   </title>\n </head>\n")
    print(" <body>\n   <h1>", str3, "</h>\n\n   <p>", str4, "\n   </p>\n\n   <p>", str5, "\n   </p>\n </body>\n</html>")

    
def get_title():
    Webpage_Title = input("Enter webpage title : ")
    Webpage_Title = Webpage_Title.center(25)
    Title = input("Enter title : ")
    Title = Title.capitalize()
    Header = input("Enter header : ")
    Header = Header.title()
    Para1 = input("Enter first paragraph : ")
    Para2 = input("Enter second paragraph : ")
    return Webpage_Title, Title, Header, Para1, Para2

def main():
    Webpage_title, title, header, para1, para2 = get_title()
    html(Webpage_title, title, header, para1, para2)


#Main starts from here
main()
