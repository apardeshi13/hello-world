# Defining the function
def bill():
    # Input prompts to get quantity of coffee and muffins
    # stored in strings cof and muf
    print("My Coffe and Muffin Shop")
    cof = int(input("Number of coffees bought?"))
    water = int(input("Number of water bottles bought?")
    candy = int(input("Number of candies bought?")
    muf = int(input("Number of muffins bought?"))
    # Calculate the total, turn into integer because variable can be string
    # calculate tax and grand total i.e. total with tax
    total = (cof*5)+(muf*4)+(water*1)+(candy*1)
    total = int(total)
    tax = 0.06*total
    gtotal = round(total + tax, 2)

    # Print the receipt with a summary with cost, quantity and grand total.
    print("My Coffee and Muffin Shop Receipt")
    print(cof, "Coffee at $5 each: $", cof*5)
    print(muf, "Muffins at $4 each: $", muf*4)
    print(water, "Water at $1 each: $", water*5)
    print(cof, "Candy at $1 each: $", candy*5)
    print("6% tax: $", total*0.06)
    print("-----------")
    print("Total: $", gtotal)
    print("Thank you for shopping with us!")
    # return the function bill so that it is closed
    return
# call the function bill() to run it
bill()
