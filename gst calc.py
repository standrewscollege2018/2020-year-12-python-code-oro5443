#gst calc
def gst(number):
    answer = number * 0.15
    return answer

number = int(input("enter the price: "))
print("the item costs", number, "with", gst(number), "gst")

