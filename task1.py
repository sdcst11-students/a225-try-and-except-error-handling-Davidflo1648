#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with a while loop along with a try...except 
# block so that the user will keep entering in a number
# until they have entered a value integer value

while True:
    number = input("Please enter in an integer value: ")
    try:
        print('Now attempting to convert value into an integer')
        number = int(number)
        print('Successfully converted into integer')
        break
    except Exception as e:
        print('There was an error. Please try again\n')

print(number)
