# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
def isEven(number):
    print(number%2 == 0)

isEven(num)
        

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def evenOrOdd(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd")

evenOrOdd(num)
