food = {"cheese pizza", "quiche","morning bun","gummy bear","tea cake"}#DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
food=input()
if food in bakery_stock:
     print("{}".format(bakery_stock[food]))
else:
    print("We don't make that")