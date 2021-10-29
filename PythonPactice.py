print("Hello World")
# a  = int(input())
# print(pow(a,3))


# Variables
name = "Ankit Mehta"
company = "Societe Generale Global Solutions Center"
role = "Software Engineer"
nameName = "dkjld"
_name = "Underscore variable name"
print(name, company, role, sep = "\n")
print(_name)
print(2 )

import math
from typing import ChainMap
a  = 3.1111111111111111111111111111111111
print(a)
print(math.ceil(a))

# Basic operators
print("***************** Basic Operators *************")
print("2 + 3",2 + 3)
print("2 * 3",2 * 3)
print("2 ** 3",2 ** 3)
print("3 / 2",3 / 2)
print("4.0 // 3",int(4.0 // 3)) # Type casting
print("5 - 3",5 - 3)
print( "8 % 5",8 % 5 )


# String Quotes
print("***************** String Quotes *************")
sentence1 = "This is 'really' amazing"
sentence2 = 'This is "really" amazing'

sentence3 = 'This is \'really\' amazing'
sentence4 = "This is \'really\" amazing"
 
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)

paragraph = '''
This is a 
long paragraph
'''
print(paragraph)


# String API & Functions
'''
For String API:
Go to python main site. Then go to documentation and then to the python3.
Choose string section you will get the list of different functions of string 
API in Python.
'''
print("***************** String Functions *************")

apple = "apple"
print('Upper Case: ', apple.upper())

mango = 'MANgo'
print('Lower Case: ',mango.lower())
print("Title Case: ",mango.title())

apple = '             Apple     '
print('Strip function: ',apple.strip().lower())

mango = "mAngo"
print("Capitalize: ", mango.capitalize())

#  Advanced String Manipulation

print("***************** String Advance Manipulation *************")

prefix = 'python is an '
suffix = 'awesome language. '

astr = prefix + suffix
print('Concatenation: ', astr)

astr = astr.replace("language", "snake")
print("Replacing 'language' with 'snake': ",astr,'\n')

astr = astr * 3         # Another way to conctenate
astr = astr.replace("snake","language")
print("Replaces all the 'snake' with 'language': ",astr,'\n')

astr = astr.replace('language', 'snake', 2 )
print("Replaces only the count(here count is 2) parameter entered for 'language' to 'snake': ", astr,'\n')

print('Count function "Returns all the instance entered in the argument of count function":  ', astr.count("an"))

# String Formatting

print("***************** String Formatting *************")

n = 11
f = 3.14592878456
s = "computer"

print("Here is a number : {:d}".format(n))
print("Here is a binary number of 10: {:b}".format(n))
print("Here is a string: {:s}".format(s))
print("Here is an exponent form number: {:e}".format(1000))
'''
There are many such formats. Some are:
e : exponent form e.g., 1000 as 1.000000e+03
b : binary form base(2)
o : octal form (base 8)
d : decimal form (base 10)
x : hexadecimal form (base 16)
f : floats (decimal numbers)
s : strings (default if none is specified)
'''
print("Print only three digit after decimal point for 3.1456783 : {:.3f}".format(3.1456783), sep = "\n")
print("Applying paading with 0 in fornt of 'f': {:015.3f}".format(f),sep = "\n")

print("Multiple variables in a single  format: {0} {1} {2}".format(n,f,s), sep = "\n")

print("Variable declaration within format function")
print("{name} own(s) {amount} of {objects}".format(
    name = "Ankit Mehta",
    amount = 5,
    objects = "mangoes."
))


'''
#  User Input

print("***************** User Input *************")
#  By default the return type of input() is string
first_name = input("Please enter your first name: ")
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")
age = int(input("Please enter your age: ")) # Type casting the string into int

first_name = first_name.capitalize()
last_name = last_name.capitalize()
middle_name = middle_name.capitalize()

print("Wihtout formatting: ", first_name, middle_name, last_name, "\nAge: ", age)

name_format = "{first} {middle:.1s} {last} \nAge: {age}"
print("With formating:", end = " ")
print(name_format.format(
    first = first_name,
    middle = middle_name,
    last = last_name,
    age = age
))

'''

# Lists
# Introduction to List

print("***************** Lists *************")

# Creating List
numbers = [1,2,3,4,5]
names = ["a",'b','c','d','e']

print(numbers)
print(names)

# Accessing the elements of a list
print('First element (element at index 0) for "names" list: ',names[0])
print('First element (element at index 0) for "numbers" list: ',numbers[0])

# Deleting the element in a list
print(names)
print("Delete an element at index 3:")
del names[3]
print(names)

#  Simple Difference between string and a list
'''
Lists are mutable while string are immutable.
Example:
msg = "Hello World"
del msg[0] # Gives error: 'str' object doesn't support item deletion
'''

#  List Methods

print("***************** List Methods *************")

#  Appeding to list and different ways to do it
print('Method 1 "names.append("f")"')
names.append("f")
print(names)
print('Method 2 "names = names + ["g","h"]"')
names = names + ["g","h"]
print(names)

# Removing the element of a list
# Method 1
print('Removing using "del" method by getting the index of "h"')
h_index = names.index("h")
del names[h_index]
print(names)

print("removing using 'remove()' function")
names.remove("g")
print(names)

#  Advanced List methods
print("***************** List Methods *************")

# Sorting, Inserting element and list-> sort

alpha1 = ["a", "f", "d", "e", "b"]
alpha2 = ["i",'g', 'h']
alpha_string = "jmnkloprqsuwtxvyz"
alpha3 = list(alpha_string)

print("Before Sorting")
print('Alpha1: ',alpha1)
print('Alpha2: ',alpha2)
print('ALpha3: ',alpha3)
alpha1.sort()
alpha2.sort()
alpha3.sort()

print("After Sorting")
print('Alpha1: ',alpha1)
print('Alpha2: ',alpha2)
print('ALpha3: ',alpha3)

print('Insert "c" at index 2: ')
alpha1.insert(2,"c")
print('Alpha1: ',alpha1)
print('Alpha2: ',alpha2)
print('ALpha3: ',alpha3)

print('Convert the list to string using join method with each element having an empty string between them: ')
alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)
alpha3 = ''.join(alpha3)
print('Alpha1: ',alpha1)
print('Alpha2: ',alpha2)
print('ALpha3: ',alpha3)

print('Full converted alphabet string: ')
alphabet = alpha1 + alpha2 + alpha3
print(alphabet)

# Built-in List functions
# min, max, len, sum
print("***************** Built-in List functions *************")

numbers = [2,3,5,12,4**2]
message = "HelloWorld"

# For a list
print("Maximum in a list: ", max(numbers))
print("Minimum in a list: ", min(numbers))
print("Sum of a list: ", sum(numbers))
print("Length of the list: ", len(numbers))

# For a string

print("Maximum in a String: ", max(message))
print("Minimum in a String: ", min(message))
print("Length of the String: ", len(message))

# 2D arrays and array references
print("***************** 2D arrays and array references *************")

# import pprint function from the pprint module as a function called pretty_print
from pprint import pprint as pretty_print

# imports copy and deepcopy functions from the copy module
from copy import copy, deepcopy

nums_2d = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

print('print(nums_2d[1][3]):',nums_2d[1][3],"\n")

print('Print 2d Array: ', nums_2d)
print("Pretty Print of 2d Array: ")
pretty_print(nums_2d)

print("Pretty Print of 2d Array after change: ")
nums_2d[2][1] *= (-1)
pretty_print(nums_2d)

# Passing list as reference
letters = ['a','b','c','d','e']
letters_2d = [letters, letters, letters]
print("List passing as a reference")
pretty_print(letters_2d)

'''
Here if we make any changes in the letters list it will be reflected to all the references in the letters_2d
list because all the letters that are passed to the letters_2d as a reference are identical i.e., they have 
same id.
Example: See the below code
letters_2d[0][0] = 'f'
pretty_print(letters_2d)
Output is :
[['f', 'b', 'c', 'd', 'e'],
 ['f', 'b', 'c', 'd', 'e'],
 ['f', 'b', 'c', 'd', 'e']]

 so to overcome this we use copy from the copy module that will create a unique copy of the list that we want
 to copy as shown in below code:

letters_2d = [copy(letters), copy(letters), copy(letters)]
letters_2d[0][0] = 'g'
pretty_print(letters_2d)
Output is:
[['g', 'b', 'c', 'd', 'e'],
 ['f', 'b', 'c', 'd', 'e'],
 ['f', 'b', 'c', 'd', 'e']]

'''

print("Problems with the list as a reference: ")
letters_2d[0][0] = 'f'
pretty_print(letters_2d)

print("Using the copy function from copy modeule for passing list as a reference: ")
letters_2d = [copy(letters), copy(letters), copy(letters)]
letters_2d[0][0] = 'g'
pretty_print(letters_2d)


# List Slicing

print("***************** List Slicing *************")

#  Use range to generate a list of numbers
a = list(range(0,10))
print("Use range to generate a list of numebrs:", a)

print("first five elements in the list: ", a[0:5])
print("print from index '2' to the end of the list", a[2:len(a)])

'''
The slicing operator ":" can take three operator. Syntax is:
list_name[start: stop: steps] -> This returns all the elements of the list which range betweem [start,stop-steps]
start: starting index
stop: stopping index -1
steps: steps decides the next element. Index goes as follows:
initial index = start
next new index = start + steps
'''

print("Reverse list: ",a[::-1])
print("Reverse List with 2 steps:", a[::-2])
print("List with 2 steps:", a[::2] )
print("list with two steps with starting with start and edning with stop:", a[1:7:2])
print("Reverse list with two steps with starting with start and edning with stop:", a[7:1:-2])


# Control Flow

print("***************** Control Flow *************")

# If statement

age = 35
if age == 35:
    print("My age is 35!")

name = "Ankit"
if name == "Ankit":
    print("My name is Ankit")
    if age == 22:
        print("And my age is 22")

# Comparison Operators

print("***************** Comparison Operators *************")

'''
comparison operators: ==, != , <, >, >=, <=
'''

temperature = '''
(-∞,-30]    REALLY COLD!
(-30, 0)    COLD!
0           ZERO!
(0,20)      PERFECT!
[20,40)     HOT!
[40,∞)      REALLY HOT!

'''
#  Example


# print("Temperature distributiuon: ", temperature)
# t = int(input("Please enter the temperature: "))
# if (t <= -30):
#     print("REALLY COLD!")
# if (t < 0):
#     if (t > -30):
#         print("COLD!")
# if(t == 0):
#     print("ZERO!")
# if(t >0):
#     if( t <20):
#         print("PERFECT!")
# if(t >= 20):
#     if(t <40):
#         print("HOT!")
# if(t >= 40):
#     print("REALLY HOT!")


#  elif

print("\nElif Example: \n")
age = 22
if age == 12:
    print("age is 12")
elif age == 22:
    print("age is 22")
else:
    print("age does not match")


#  or, and, not
print("***************** 'and', 'or', 'and' operators *************")

T = True
F = False

statement1 = 3 > 4 # False
statement2 = 10 % 5 == 0 # True
statement3 = 'A'.lower() == 'a' # True

print("Comparision Examples for different types of statement type: ")
print("statement1 = 3 > 4 ->  \t", statement1)
print("statement2 = 10 % 5 == 0 ->  \t", statement2)
print("statement3 = 'A'.lower() == 'a' ->  \t", statement3)

# or
print("\n'or' operations")
if F or F: print("if F or F:")
if F or T: print("if F or T")
if T or F: print("if T or F")
if T or T: print("if T or T")

# and
print("\n'and' operations")
if F and F: print("if F and F:")
if F and T: print("if F and T")
if T and F: print("if T and F")
if T and T: print("if T and T")

# not
print("\n'not' operations")
if not T: print("not T")
if not F: print("not F")

# Some Practice Programs

print("***************** Some Practice Programs *************")

print("First Program description: ")
p1 = '''Problem 1:
Write a program that given two numbers 'a', 'b' print "divisible" 
if one of the two numbers divides the other
Here a = 46, b = 23 and c = 14
'''

print(p1)
a = 46
b = 23
c = 14
print("For a and b: ")
if a % b == 0  or b % a == 0 :
    print("divisible")
else:
    print("not divisible")

print("For a and c: ")
if a % c == 0  or c % a == 0 :
    print("divisible")
else:
    print("not divisible")


p2 = '''Problem2:
Given input a, b print a/b if b is not equal to zero
'''
print("\n",p2)
print("Note: Placed in a comment because it is asking for the input. To execute just uncomment the code.")
# a = int(input("Please enter a: "))
# b = int(input("Please enter b: "))

# if b == 0:
#     print("b is zero. Math Error")
# else:
#     print(a/b)

p3 = '''
Write a program that given three names prints "equal" if all three
names are equal to each other when lowercase
'''
print("Note: Placed in a comment because it is asking for the input. To execute just uncomment the code.")

# s1 = input("Please input string 1: ")
# s2 = input("Please input string 2: ")
# s3 = input("Please input string 3: ")

# s1 = s1.lower()
# s2 = s2.lower()
# s3 = s3.lower()
# if s1 == s2 and s2 == s3:
#     print("equals")
# else :
#     print("not equal")


# for loop
print("***************** Loop and Iterables *************")

print("\"in\" keyword")

a = [4,6,8]
s = "hello world"

'''
'in' can be used as a conditional operator
'''
print("check 5 in a", 5 in a)
print("check 4 in a", 4 in a)


print("\nFor Loop \n")

exp = '''
for i in a:
    print(i)

Output: a is 
'''
print(exp)
for i in a:
    print(i, end = " ")

print('\n')

# even numbers list print
exp = 'even numbers list print'
print(exp)
for i in [2,4,6,8,10]:
    print(i, end = " ")

print()

# odd numebrs list prin
exp = 'odd numbers list print'
print(exp)
for i in [1,3,5,7,9]:
    print(i, end = " ")

print('\n')

print("range(len(a)): ",range(len(a)))
exp = '''
for i in range(len(a)):
    print(a[i], end = " ")

Output: a is 
'''
print("for loop using range class: \n ", exp)
for i in range(len(a)):
    print(a[i], end = " ")
print('\n')


# while loop

print('while loop')

index = 0

name = ['ankit','adarsh','akash','verma','anil']
exp = '''
Code: 
name = ['ankit','adarsh','akash','verma','anil']
while index < len(name):
    print(name[index], end = " ")
    index+=1

Output: name is
'''
print(exp)
while index < len(name):
    print(name[index], end = " ")
    index+=1
print()
#  Another way of using while with range class
exp = '''
Code: 
total = 0
inx = 0
while inx in range(0,11):
    total = total + inx
    inx+=1
'''
print(exp)
total = 0
inx = 0
while inx in range(0,11):
    total = total + inx
    inx+=1
print("Sum of first 10 natural numbers using while loop with range class: ",total)


#  Iterables
print("***************** Iterables *************")

my_list = [1,2,3,4,5,6]
my_tuple = (1,2,3,4,5,6)
my_string = "Hello World!"

print("__iter__" in dir(my_list))
print("__iter__" in dir(my_tuple))
print("__iter__" in dir(my_string))

exp = ''' Here,
'__iter__' returing 'True'denotes that the list, tuple and string are all
iterables.
'''
print(exp)

list_iterator = iter(my_list) # List iterator creation
tuple_iterator = iter(my_tuple) # Tuple iterator creation
string_iterator = iter(my_string) # String iterator creation


exp = '''
Now, let's see how the for loop function in context of iterators,
for elem in my_list:
    print(elem)

Iterator function for loop: 
list_iterator = iter(my_list)

while True:
    try:
        next_elem = next(list_iterator)
        print(next_elem, end = ' ')
    except StopIteration:
        break
    
Output is : my_list is: 
'''

print(exp)

while True:
    try:
        next_elem = next(list_iterator)
        print(next_elem, end = ' ')
    except StopIteration:
        break
print()

#  Problems
print("***************** Problems *************")

exp = '''\n
problem 1: 
sum of even numbers in a list
'''
print(exp)

total = 0
my_list = [1,2,3,4,5,6,7,5,234,234,253,26,36,2,52]
for i in my_list:
    if i % 2 == 0:
        total = total + i

print("sum of even numbers in the given list is: ", total)

exp = '''
Problem 2: 
Extract consonants from a string
'''
print(exp)
alpha = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM'
vowels = 'aeiouAEIOU'
my_string = "Packet publishing rocks!"

character_without_consonants = []
for ch in my_string:
    if ch in vowels or ch not in alpha:
        continue
    else:
        character_without_consonants.append(ch)
consonants_string = ''.join(character_without_consonants)
print('Extracted consonants string from my_string "{given_string}" is : {consonants}'.format(given_string = my_string, consonants = consonants_string))

# Functions

print("***************** Functions *************")

PI = 3.141592
def circle_area(r):
    return PI * r * r

def show_message():
    print("Using area_circle functions, area of circle for different 'r'")

show_message()

print('Area of circle with radius {:d} is {:.3f}'.format(5, circle_area(5)))
print('Area of circle with radius {:d} is {:.3f}'.format(10, circle_area(10)))
print('Area of circle with radius {:d} is {:.3f}'.format(15, circle_area(15)))

# Arguments and Paramaeters

print("***************** Arguments and Paramaeters *************")

def printNumbers(a,b): # Here a and b will be calles as parameters
    print(a,b)

print("Here 1,2 is called arguments while a and b are called parameters: ")
printNumbers(1,2)


# Default parameter
from datetime import datetime as dt
def record_time( message, time = dt.now()):
    print("{:}, time: {:}".format(message, time))
# Default parameter need not to be mentioned while calling the function. 
# It will directlty assign the default value to that argument
record_time("It  is the morning") 
# Or we can simply overwrite the default value by mentioning the argument.
record_time("It  is the morning", "Dec, 29th, 1998")

# Variadatic parameter
# When we want to pass multiple argument inside a function. That parameter is known as variadatic
# parameter. It is stored in a tuple. We declare a parameter as variadatic by inserting aestrick(*)
# infront of the parameter name

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Addition of variable number of numbers using variadatic parameter supported function add: {:d}".format(add(1,2,3,4,5,6,7,8)))

# Problems
print("***************** Problems *************")
exp = '''
Problem 1:
Reverse a given string
'''
print(exp)
def reverse(s):
    reverse_string = ""
    for i in range(0,len(s)):
        reverse_string += s[len(s) - i - 1]
    return reverse_string
my_string = "Hello World!"
print("Reverse a given string. Given String is: {:s} \nReversed String is: {:s}".format(my_string,reverse(my_string)))

exp = '''
Problem 2:
Check whether a given string is a palindrome or not
'''
print(exp)
def is_palindrome_first_way(s):
    for i in range(0,len(s)//2):
        if s[i] != s[len(s) - i -1]:
            print("'{:s}' is not a palindrome. Palindrome check done using first function".format(s))
            return 
    print("'{:s}' is a palindrome. Palindrome check done using first function ".format(s))

def is_palindrome_second_way(s):
    if s == s[::-1]:
        print("'{:s}' is a palindrome. Palindrome check done using first function".format(s))
    else:
        print("'{:s}' is not a palindrome. Palindrome check done using first function".format(s))

print("Palindrome check from first function: ")
is_palindrome_first_way(my_string)
print("Palindrome check from second function: ")
is_palindrome_second_way(my_string)

print("Some more examples:")
is_palindrome_first_way("aba")
is_palindrome_second_way("aba")
is_palindrome_first_way("aab")
is_palindrome_second_way("aab")
is_palindrome_first_way("abba")
is_palindrome_second_way("abba")
print()
# Advance Examples
print("***************** Advanced Problems *************")

exp = '''
Problem: 
Implementting the shift cipher.
The shift cipher that we will implement will use the characters a-z
Able to specify a shift value:
"bcde" with shift 0 -> "bcde:
"bcde" with shift 1 -> "cdef:
"bcde" with shift 3 -> "efgh:
"xyz" with shift 1 -> "yza:
'''

print(exp)

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift = 3):
    encrypt_string = ""
    for ch in s:
        idx = alpha.index(ch)
        encrypt_string += alpha[(idx + shift) % 26]
    return encrypt_string

def decrypt(s, shift = 3):
    decrypt_string = ""
    for ch in s:
        idx = alpha.index(ch)
        decrypt_string += alpha[(idx - shift) % 26]
    return decrypt_string

my_string = "helloworld"
print('Encryption of {:s} is: {:s}'.format(my_string,encrypt(my_string,1)))
my_string = encrypt(my_string,1)
print('Decryption of {:s} is: {:s}'.format(my_string,decrypt(my_string,1)))

# Recursion

print("***************** Recursion *************")

# Example 1

print("Example 1: Using recursion doubling a number: ")
def double(n):
    if n == 0:
        return 0
    else:
        return double(n-1) + 2

print("Double of 18 is {:d}".format(double(18)))

# Example 2

print("Example 2: Using recursion to find the 'a' exponent 'b':")
def exponential(b,e):
    if e == 0:
        return 1
    else:
        return exponential(b, e-1) * b

print("3 exponent 6 is: {:d} ".format(exponential(3,6)))

# Recursion Examples

print("***************** Recursion Examples *************")

exp = '''
Example 1: Recursively count vowels in a string
'''
print(exp)

def count_vowels(s, i = 0):
    if i == len(s): 
        return 0
    if s[i] in 'aeiou':
        return count_vowels(s, i+1) + 1
    return count_vowels(s, i+1) + 0

my_string = "helloworld"
print("Vowels in {:s} is {:d}".format(my_string,count_vowels(my_string)))

exp = '''
Example 2: Recursively count the sum of the digits in a number
'''
print(exp)

def sum_of_digits(n):
    if n == 0:
        return 0
    return sum_of_digits(n//10) + (n % 10)

my_number = 123456789
print("Sum of {:d} is {:d}".format(my_number, sum_of_digits(my_number)))

exp = '''
Example 3: Computing the nth fibonacci number recursively
'''
print(exp)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0,10):
    print("{:d}th fibonacci number is {:d}".format(i,fibonacci(i)))


#  Modules

print("***************** Modules *************")

print("Custom module volume.py\nIts contents:")

import volume
from volume import *

print(dir(volume)) # dir() is a built in function that tell us the contents of a particular module

print("Volume of sphere of radius 7: {:f}".format(sphere_vol(7)))
print("Volume of cube of dimensions 7X5X8: {:f}".format(cube_vol(7,5,8)))
print("Volume of cone with base radius 7 and height as 8: {:f}".format(cone_vol(7,8)))

# Modules and Testing

print("***************** Modules and Testing *************")

print("\nNote:See the string_functions.py and testing_module.py file for this section\n")

# Python and Picture Manipulation
print("***************** Python and Picture Manipulation *************")

print("\nNote: For this please refer to the image_manipulation.py file\n")
  

# Classes and objects
# Functional Programming
# Advanced data structures
# : Hash tables
# : Heaps
# : Trees