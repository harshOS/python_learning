def collatz(num):
    global number
    if num % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number


print("enter the value: ")
number = int(input())

while (number != 1):
    collatz(number)