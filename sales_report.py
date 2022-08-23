def generate_sales_report_melons_sold(filename):
    """Generate sales report showing total melons each salesperson sold."""
#not built as a function can't be called as easy

    salespeople = []
    melons_sold = []

    f = open('sales-report.txt')  #f is not a good variable name for file, hard to tell what it is

    for line in f:
        line = line.rstrip()
        entries = line.split('|')   #splitting line into salesperson, price sold, and melons sold
        salesperson = entries[0]
        melons = int(entries[2]) #changing melons sold to integer

        if salesperson in salespeople:                  #if salesperson there adds melons sold to salesperson
            position = salespeople.index(salesperson)      #indexing person to add melons sold might be better
            melons_sold[position] += melons                 #to use a dictionary?
            
        else:                                           #otherwise adds salesperson to list
            salespeople.append(salesperson)
            melons_sold.append(melons)

    
        for i in range(len(salespeople)):       #prints melons sold in range of salespeople
            print(f'{salespeople[i]} sold {melons_sold[i]} melons')

# print(generate_sales_report_melons_sold('sales-report.txt'))

def melons_sold_by_person(filename):
    """Opens file and returns salesperon and amount of melons they sold in a dictionary"""
    salesperson_dictionary = {}
    file = open(filename)
    for line in file:
        sales_person, sales, melons = line.rstrip().split("|")
        if sales_person in salesperson_dictionary:
            salesperson_dictionary[sales_person] += int(melons)
        else:
            salesperson_dictionary[sales_person] = int(melons)
    
    return salesperson_dictionary

melons_sold = melons_sold_by_person('sales-report.txt')



def print_sales_report_by_person(melons_sold_by_person):
    
    for salesperson, melons in melons_sold_by_person.items():
        print(f"{salesperson} has sold {melons}.")


print(print_sales_report_by_person(melons_sold))