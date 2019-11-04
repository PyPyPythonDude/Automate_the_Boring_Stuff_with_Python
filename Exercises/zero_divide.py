def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        # display an error message for the user if they attempt to divide by zero
        print("Error: Invalid argument")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
