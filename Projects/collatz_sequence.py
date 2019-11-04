# This program performs different calculations based on whether a given
# number is even or odd.
def collatz(number):
    # Check if a number is divisible by 2 with 0 remainder.
    if number % 2 == 0:
        # Floor division means the // will always take the floor or lower number.
        result = number // 2
    # If the remainder is 1, the number is odd.
    elif number % 2 == 1:
        result = 3 * number + 1

    print(result)
    return result

try:
    num = int(input("Give me a number: "))
    while num > 0 and num != 1:
        num = collatz(num)
except ValueError:
    print("You must enter an integer.")
