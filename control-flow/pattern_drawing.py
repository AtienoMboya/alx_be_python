# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

while row < size:
    # Use a for loop to print asterisks in each row
    for col in range (size):
        print("*", end="")
    print() # Print new line at the end of each row
    row+=1
