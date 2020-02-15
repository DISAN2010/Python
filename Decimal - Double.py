def main():
    Range = range(94, 108)
    for x in Range:
        if x < 100:
            x = x/2
            print(x)
        elif x > 99:
            x = x*2
            print(x)
                       
#Main starts from here
main()
