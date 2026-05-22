'''

- The Week-1 Training -
- The Level&Solve=> Depends on What u Learn Till Now -

'''

name= 'aiiob'
age= '21'
country= 'egypt'
print(
  f'''
  "Name: {name.capitalize()}"
  "Age: {age}"
  "Country: {country.capitalize()}"
  '''
)

print('\n'); print('-' * 20, end='\n\n')#-----------------------

print(
  f"Hello, {name.capitalize()} You are '{age}' Old Now and Live Location is {country.capitalize()}"
)

print("-"*20)

print(type(name))
print(type(age))
print(type(country))

print('\n'); print('-' * 20, end='\n\n')#-----------------------

# output needed -> the same with signs -> in one line
# "Hello '{Aiiob}', How You Doing \ """ Your Age Is "'21\'"" + And\/ Your Country Is: Egypt\'\"
print(
  f'"Hello \'{{{name.capitalize()}}}\', How You Doing \\ """ Your Age Is "\'{age}\\\'"" + And\\/ Your Country Is: {country.capitalize()}\\\'\\\" "'
)

# Why Use Triple {{{}}} ? #
# {name.capitalize()} 		=> Normal variable => Will Print the Variable Data Normally.
# {{name.capitalize()}} 	=> Literal Text		 => Will Print the Literal Anything Inside The 'First Curly Brackets'
# {{{name.capitalize()}}} => Variable Inside Literal Braces => Like 'Double' but if Found Variable Will Print The Data of it

print('\n'); print('-' * 20, end='\n\n')#-----------------------

champions= 'al ahly of egypt'
print(champions[1])
print(f"'{champions[2]}'")
print(champions[-1])

print('\n'); print('-' * 20, end='\n\n')#-----------------------

name = 'Elzero'

# Needed Output
# "lze"
# "Ezr"
# "rzE"
print(name[1:4])
print(name[::2])
print(name[::2][::-1]) #=> - all data in python is object -

print('\n'); print('-' * 20, end='\n\n')#-----------------------

team= "#@#@barcelona#@#@"

# Needed Output
# barcelona
print(team.strip('#@').capitalize())

print('\n'); print('-' * 20, end='\n\n')#-----------------------

num= "9"
print(num.zfill(4))

num= "15"
print(num.zfill(4))

num= "130"
print(num.zfill(4))

num= "950"
print(num.zfill(4))

num= "1500"
print(num.zfill(4))

print('\n'); print('-' * 20, end='\n\n')#-----------------------

first= "aiiob"
print(first.ljust(20, '@'))
second= "python_django"
print(second.ljust(20, '@'))

print('\n'); print('-' * 20, end='\n\n')#-----------------------

msg= "I Love Python And Although Love elzero.org"
print(msg.count('Love'))

print('\n'); print('-' * 20, end='\n\n')#-----------------------

goat= 'rdr2'
print(goat.index('r'))
print(goat.find('r', 1))

print('\n'); print('-' * 20, end='\n\n')#-----------------------

msg= "I <3 Python And Although <3 elzero.org"
msg= msg.replace('<3', 'Love', 2)
print(msg.title())