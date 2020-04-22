import re

def items_removed(total_bill, items_present, bill, total):
    try:
        with open(total_bill, "r") as FH:
            all_lines = FH.read()
            print("\nBill in the Supermarket:\n")
            print(all_lines)
            
        with open(items_present, "r") as FH:
            list_of_items = []
            list_of_items_removed = []
            print("\nWhatsApp message with the list of items already present at home\n")
            for items in FH:
                parts = items.split("\n")
                product = parts[0]
                print(product)
                list_of_items.append(product)
            
            for item in list_of_items:
                for key in list(bill.keys()):
                    if key == item:
                        removed_items = bill.pop(key)
                        list_of_items_removed.append(removed_items)

            list_of_items_removed = [int(i) for i in list_of_items_removed]

            print("\nTotal amount of the bill :", total)
            
            Total_Saved = sum(list_of_items_removed)
            print("Amount of money Sunita and her husband saved for themselves :", Total_Saved)
            
            Total_Payed = int(total) - Total_Saved
            print("Total amount payed : ", Total_Payed)
             
    except IOError:
        print("Could not open file")
    except:
       print("Oops")

def bill(file):
    try:           
        with open(file, "r") as FH:
            bill = dict()
            for line in FH:
                if not line.strip() or line.startswith("#") or line.startswith("=") or line.startswith("Sl"):
                    continue
                else:
                    parts = re.split(': |[.]|\n', line)
                    if line.startswith("TOTAL"):
                        items = parts[0].strip()
                        price = parts[1].strip()
                        total = price
                    else:
                        items = parts[1].strip()
                        price = parts[2].strip()

                    bill[items] = price

            return bill, total         

    except IOError:
        print("Could not open file")
    except:
        print("Oops")
                

def get_file():
    file = input("File to open : ")
    file = file + ".txt"
    return file

def main():
    Total_Bill = get_file()
    Bill, Total = bill(Total_Bill)
    Items_Present = get_file()
    items_removed(Total_Bill, Items_Present, Bill, Total)

#Main starts from here
main()

