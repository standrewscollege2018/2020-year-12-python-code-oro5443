def check(number):
    answer = number % 2
    return answer

number = int(input("enter a number: "))

if check(number) == 0:
    print(number, "is even")
else:
    print(number, "is odd")
