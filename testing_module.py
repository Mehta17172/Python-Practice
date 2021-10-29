import string_functions # this gives the __name__ of the string_functions.py
print(__name__) # this denotes that the currently we are running 'THIS' script i.e., tesing_module.py

# this denotes that the currently we are running 'THIS' script i.e., tesing_module.py
if __name__ == '__main__':
    print("Printing string funtions: ")
    # assert function is a true pr false function that checks the condition
    # syntax: assert condition, statements(if condition failed)
    assert string_functions.first_half("abcd") == "ab", "First half is failing"
    assert string_functions.last_half("abcd") == "cd", "Last half is failing"


