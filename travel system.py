"""this allows customers to calculate the total cost of their holiday"""
departureloc = ["AUCKLAND", "WELLINGTON", "CHRISTCHURCH"]
departures = [["AUCKLAND", 0, "international airport"], ["WELLINGTON", 50, "connection flight required"], ["CHRISTCHURCH", 75, "connection flight required"]]
destinationloc = ["SYDNEY", "TONGA", "SHANGHAI", "LONDON"]
destinations = [["SYDNEY", 326], ["TONGA", 378], ["SHANGHAI", 1436], ["LONDON", 2376]]
accommodation = [["SYDNEY", 120], ["TONGA", 40], ["SHANGHAI", 60], ["LONDON", 80]]
price = 0
ask = True
def pricer(price):
    print("your trip will cost $", price)
    return(price)

def destinationask():
    ask2 = True
    while ask2 == True:
        print("what is your destination")
        for location in destinations:
            print(" ".join(map(str, location)))
        b = input()
        b = b.upper()
        print(b)
        result2 = [destination for destination in destinations if destination[0] == b]
        if result2 == []:
            print("please enter a valid input")
            print("please check your spelling")
        else:
            ask2 = False
            print("sweet")
            destination = destinationloc.index(b)
            print()
            print("this will cost $")

        
    

while ask == True:
    print("where are you departing from?")
    for location in departures:
        print(" ".join(map(str, location)))
    a = input()
    a = a.upper()
    print(a)
    result = [departure for departure in departures if departure[0] == a]
    if result == []:
        print("please enter a valid input")
        print("please check your spelling")
    else:
        ask = False
        location = departureloc.index(a)
        print(departures[location][2])
        addprice = departures[location][1]
        print("this departure requires an additional cost of $", addprice)
        price = price+addprice
        pricer(addprice)
        destinationask()
