# Prompt the user to enter a number
# The input() function gets a string, which is then converted to an integer using int()
number = int(input("Enter a number: "))

# Check the remainder when the number is divided by 2
if number % 2 == 0:
    # If the remainder is 0, the number is even
    print("The number {} is Even.").format(number)
else:
    # Otherwise, the number is odd
    print("The number {} is Odd.").format(number)
