# Notes
  # All Data in Python is Objects.
  # Comments is very important if use it right. 
  # type() is used to check the data type

# dataTypes

print(type("hello World!")) # 1- str - String

print(type(1)) # 2- int - Integer
print(type(-400)) # 2- int - Integer

print(type(1.0)) # 3- Float 
print(type(-40.00)) # 3- Float

print(type(True)) # 4- bool - Boolean
print(type(False)) # 4- bool - Boolean
print(type(2==2)) # 4- bool - Boolean

print(type([1, 2, 3])) # 5- List
print(type([1, 2, 'Test'])) # 5- List

print(type((1, 2, 3))) # 6- Tuple
print(type((1, 2, 3, 'Test'))) # 6- Tuple

print(type({'key':'value', 'age':21})) # 7- dict - dictionary

print(type({1, 2, 3, 'test'})) # 8- set

# variables

# Can start from a-z, A-Z and underscore=> '_'
# Can have nums, '_' in between 
# Cant start with nums or special characters
# Cant have special characters in between
# Case is sensitive

# syntax:-
name= 'username'
a, b, c = 1, 2, 3

# ways to titled

age= 21 # Normal

user_age = 21 # snake_case

userAge = 21 # camelCase

# Important Definition # 

# source code
  # the original code u write.

# runtime
  # period app time to executing the code

# Translation
  # convert the source code to machine language

  # have two diff types
    # compilation % Interpretation

      # compilation
        # translate the whole code file before the 'runtime' and return the execute
        
        # Interpretation
          # translate the code line by line in 'runtime' 

# reversed words if wanna know
  # cannot save data in memory with those names.

print(help('keywords'))
