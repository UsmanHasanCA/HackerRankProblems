# JAVA TO PYTHON TUTORIAL

#Creating comments

''' 
Block comments
More comments
More comments
'''

#Printing to the console

#Automatically adds line break between print commands
print("Hello")
print("Hello")

#Add end parameter to remove auto line breaking
print("Hello", end = "")
print("Hello")

#Escape characters in Python

#   \n will force a line break
print("He\nllo")

#	\t will force insert a tab
print("He\tllo")

#Combining string literals
print("Hello" + "world")

#Variable declaration
# Strings can be declared with double quotes or single quotes in Python
var = 'hello'
var1 = "hello"

# You do not need to define types, they are inherited
var2 = 3
var3 = 4.5
var4 = True

#printing variable types, concatenating with string literals
print('var2 =', var2) #using the comma adds a space
print('var2 = ', var2, sep = '') # using the sep parameter we can remove the automatic space from the comma

#Addition, subtraction, multiplication, division
div = 3/4
print('div = ', div, sep='')

#Integer division, known as "Floor divion" in Python
floordiv = 3//4 #denoted by two //
print("floordiv =", floordiv) # prints 0 because 0.75 in integer division is 0

#Exponents
exp = 2**3 # computes 2^3
print('Exponent=', exp)

#Modulus
mod = 4%2
print("Modulus= ", mod, sep='')

#To cast types if you need a specific type, use the following syntax
temp = int(3.75);
print(temp) # prints 3 instead of 3.75 since temp has been cast to an integer type variable

#Finding the maximum or minimum between two numbers
maximum = max(3,4)
minimum = min(3,4)
print('Maximum of (3,4) = ', maximum, ", Minimum of (3,4) = ", minimum, sep='')

#Taking user input
print('Enter a number: ')
num = input()
print('You entered:', num)

#Simplified user input code
numTemp = input('Enter a number: ')
print('You entered: ', numTemp, sep = '')

#If you need to ensure the user input is of a certain type just cast it
numTemp2 = float(input('Enter a floating point number: ')) # throws error if the input is not a float or int
print('You entered:', numTemp2)

#STRINGS/STRING OPERATIONS
testString = 'hello'

#finding the length of a string
print(len(testString)) #len is a built-in function
