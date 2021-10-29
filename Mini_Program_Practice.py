#  Write a mini program for a calculator

import sys # sys.exit() to terminate the program

line = input("Please enter the expression: ").split(" ")
left = int(line[0]) # Left operand
op = line[1] # Operator
right = int(line[2]) # right operand

val = 0
if op == "+":
    val += left + right
elif op == "-":
    val += (left - right)
elif op == "*":
    val += left * right;
elif op == "/":
    if not(right != 0):
        print("Divide by 0. Math error")
        sys.exit()
else:
    print("Please enter the appropriate operator. Invalid '{operator}'".format(operator = op))
    sys.exit()

print("{expression} = {value}".format(expression = line, value = val))
