###
# Good Morning America!
# Bill calculation program by Shirley Wu
# Student Number: 251082034

# Compute breakfast prices at Good Morning America

# Menu prices and Combo prices
EGG = 0.99
BACON = 0.49
SAUSAGE = 1.49
HASH_BROWN = 1.19
TOAST = 0.79
COFFEE = 1.09
TEA = 0.89
SMALL_BREAKFAST = EGG + HASH_BROWN + (TOAST * 2) + (BACON * 2) + SAUSAGE
REGULAR_BREAKFAST = (EGG * 2) + HASH_BROWN + (TOAST * 2)+ (BACON * 4) + (SAUSAGE * 2)
BIG_BREAKFAST = (EGG * 3) + (HASH_BROWN * 2) + (TOAST * 4) + (BACON * 6) + (SAUSAGE * 3)

# Ensure that user input is not case or space sensitive
def formatInput(textLine) :
 textLine = textLine.lower().strip()
 wordList = textLine.split()
 textLine = " ".join(wordList)
 textLine = textLine.replace(" ", "")
 return textLine

# "order" variable stores user input
order = ""
# "quantity" variable stores amount associated with user input
quantity = 0
# "cost" variable found by multiplying quantity by item price
cost = 0

# Loop will not proceed if termination code is entered
while order != "q" or "Q":
    # Prompt user for order
    order = print("Menu Options: Small Breakfast, Regular Breakfast, Big Breakfast, Egg, Bacon, Sausage, Hash Brown, Toast, Coffee, Tea")
    order = input("Enter item (q to terminate): ")
    order = formatInput(order)
    if order == "q":
        break
    # Prompt user for order quantity. Checks if user input is a numerical value
    quantity = input("Enter quantity: ")
    if quantity.isnumeric():
        quantity = int(quantity)
    else:
        print("Error")
        continue

# Compute pre-tax cost depending on menu item using if and elif statements for every menu item
    if order == "egg":
        cost = (EGG * quantity) + cost
    elif order == "bacon":
        cost = (BACON * quantity) + cost
    elif order == "sausage":
        cost = (SAUSAGE * quantity) + cost
    elif order == "hashbrown":
        cost = (HASH_BROWN * quantity) + cost
    elif order == "toast":
        cost = (TOAST * quantity) + cost
    elif order == "coffee":
        cost = (COFFEE * quantity) + cost
    elif order == "tea":
        cost = (TEA * quantity) + cost
    elif order == "smallbreakfast":
        cost = (SMALL_BREAKFAST * quantity) + cost
    elif order == "regularbreakfast":
        cost = (REGULAR_BREAKFAST * quantity) + cost
    elif order == "bigbreakfast":
        cost = (BIG_BREAKFAST * quantity) + cost
    else:
        print("Error. Re-enter menu item: ")

# Display and compute pre-tax cost, tax, and total cost, calculated to 2 decimal places
print("Pre-tax total: $" + "%.2f" % cost)
tax = cost * 0.13
print("Tax: $" + "%.2f" % tax)
print("Total: $" + "%.2f" % (tax + cost))
print("Thank you for eating at Good Morning America!")
# Order Total Complete!

