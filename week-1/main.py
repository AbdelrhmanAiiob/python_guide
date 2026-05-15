# DataTypes.

print(type("hello world!"))   #=> str
print(type(21))               #=> int   |> negative or positive
print(type(-21.00))           #=> float |> negative or positive
print(type(2==2))             #=> bool  |> Boolean => True or False
print(type([1, 2, 3]))        #=> list
print(type((1, 2, 'test')))   #=> tuple
print(type({1, 2, 'python'})) #=> set
print(type({'key':'value', 'age':21})) #=> dictionary

print('\n'); print('-' * 20); print('\n')

# Variables.
hello= 'world'   # Normal
user_age= 21     # snake_case
isLegit= 'True'  # camelCase

# Reversed Keywords:-
  # cannot save data in memory with those names.
help('keywords')

print('\n'); print('-' * 20); print('\n')

print("Hello\bWorld") #=> HellWorld
print("Hello\
python\
World") #=> HelloPythonWorld
print("Hello\nWorld") #=> Hello \n World
print("Hello\\World") #=> Hello\World
print("Hello\'World") #=> Hello'World
print("Hello\"World") #=> Hello"World
print("12345678\rWorld") #=> World678 
print("Hello\tWorld") #=> Hello   World
print("\x61\x69\x69\x6F\x62") #=> aiiob

print('\n'); print('-' * 20); print('\n')

# strings.
print(
  '''lorem,
  why gtaVI not released till now rockstar
  ??????
  '''
) #=> The Output be the same

print(
  """lorem,
  why gtaVI not released till now rockstar
  ??????
  """
) #=> The Output be the same

print('\n'); print('-' * 20); print('\n')

# indexing.
word= "django"

print(word[1]) #=> j
print(word[3]) #=> n
print(word[-1]) #=> o

players= [1, 2, 3, 4, 5, 'messi']
print(players[-1][0]) #=> m

# slicing
msg= '''lorem, why gtaVI not released till now rockstar ?????? '''
print(msg[:6]) #=> lorem,
print(msg[11:17]) #=> gtaVI
print(msg[::2]) #=> skip one character

print('\n'); print('-' * 20); print('\n')

# stringsMethods.

# strip, rstrip, lstrip
name= '  aiiob  '
age= ' 21   '
password= '##@#@$@%^$^&$15pss664ass5344$$$##%@$@'

print(name)
print(name.strip(), end='\n\n')

print(age)
print(age.strip(), end='\n\n')

print(password)
print(password.strip(" !@#$%^&*()"), end='\n\n')
print(password.rstrip(" !@#$%^&*()"), end='\n\n')
print(password.lstrip(" !@#$%^&*()"), end='\n\n')

# title, capitalize
msg= "lorem, why gtaVI not 4released till 3now rockstar"
print(msg.title())
print(msg.capitalize())

# zfill
a, b, c, d, e = '1', '11', '111', '1111', '11111'
print(a.zfill(5)) #=> 00001
print(b.zfill(5)) #=> 00011
print(c.zfill(5)) #=> 00111
print(d.zfill(5)) #=> 01111
print(e.zfill(5), end='\n\n') #=> 11111

# split, rsplit
user_say= 'you forget a thousand things every day make sure this is one of them'
user_say2= 'you-forget-a-thousand-things every day-make-sure-this is-one of-them'

print(user_say.split())
print(user_say.split(' ',2))
print(user_say.rsplit(' ', 5), end='\n\n')

print(user_say2.split('-'))
print(user_say2.rsplit('-', 1), end='\n\n')

# upper, lower
print('USER'.lower())
print('user'.upper())

# .center(width, fill_character)
name= 'cristiano'
name= name.center(16, '$')
print(name, end='\n\n')

# count
cbc= 'trump is the smartest guy ever -___-'
print(cbc.count(' '))
print(cbc.count('Smartest'))
print(cbc.count('t'), end='\n\n')

# swapcase
print('rImWORld'.swapcase(), end='\n\n')

# startswith, endswith
someone= "Your value doesn't decrease based on someone's inability to see your worth"
print(someone.startswith('o', 12, 15))
print(someone.endswith('e', 0, 10))

# .index(subString, start, end)
name= 'aiiob'
print(name.index('i', 0), end='\n\n')
# print(name.index('z', 0))

# find(subString, start, end)
name= 'aiiob'
print(name.find('i', 2))
print(name.find('z', 0), end='\n\n')

# rjust, ljust
name= 'aiiob'
print(name.rjust(10, '#'))
print(name.ljust(10, '#'), end='\n\n')

# splitlines
vGames= 'valorant\nminecraft\nrimworld'
vGames_v2= ''' DOOM
gtav
witcher3
rdr2
'''
print(vGames.splitlines())
print(vGames_v2.splitlines(), end='\n\n')

# expandedtabs
name= 'leo\tmessi'
print(name.expandtabs(8), end='\n\n')

# replace
privileges= 'admin'
print(privileges)
print(privileges.replace('admin', 'user'))
print(privileges.replace('a', 'A'), end='\n\n')

# istitle
print(privileges.istitle(), end='\n\n')

# isspace
print(privileges.isspace(), end='\n\n')

# islower
print(privileges.islower(), end='\n\n')

# isupper
print(privileges.isupper(), end='\n\n')

# isidentifire
print(privileges.isidentifier(), end='\n\n')

# isalpha
print(privileges.isalpha(), end='\n\n')

# isalnum
print(privileges.isalnum(), end='\n\n')

# join()
fruits= ["apple", "banana", "cherry"]
print(' & '.join(fruits), end='\n\n')

