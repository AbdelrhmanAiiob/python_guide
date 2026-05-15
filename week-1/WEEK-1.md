* __Go to__
	* __[README](../README.md)__
	* __[Code.py](main.py)__

1. ALL DATA IN PYTHON IS OBJECT -
2.  COMMENTS IS VERY IMPORTANT IF USE IT RIGHT -
3. type() => built-in function to know data types -

### dataTypes:-
#### The starter pack will deal with.

```py

print(type("hello world!"))   #=> str

print(type(21))               #=> int   |> negative or positive

print(type(-21.00))           #=> float |> negative or positive

print(type(2==2))             #=> bool  |> Boolean => True or False

print(type([1, 2, 3]))        #=> list

print(type((1, 2, 'test')))   #=> tuple

print(type({1, 2, 'python'})) #=> set

print(type({'key':'value', 'age':21})) #=> dictionary

```

### variables:-
#### Data container.

- Can start from a-z, A-Z and underscore=> '_'
- Can have numbers, '_' in between
- Cant start with numbers or special characters
- Cant have special characters in between
- Case is sensitive

```py

# Syntax:-
hello= 'world'   # Normal
user_age= 21     # snake_case
isLegit= 'True'  # camelCase

# Reversed Keywords:-
	  # cannot save data in memory with those names.
help('keywords')

```

### Need to Know.

* **Source Code**
	* the original code you write
*  **Runtime**
	* the period app time to execute the code
* **Translation**
	* convert the source code to machine language
	* have two different types
		* Compiled
			* translate the whole file before runtime
			* translate and return the execute file so much faster than 'Interpreter'
			* discover the error before the execute 
		
		* Interpreter
			* translate line by line with runtime
			* discover the error once found so slower than 'Compiled'

### scape characters:- 
#### most use= 9
#### use it on strings "\character"

\b => back space
```py

print("Hello\bWorld") #=> HellWorld

```

\ => line escape 
```py

print("Hello\
python\
World") #=> HelloPythonWorld

```
\n => create new line
```py

print("Hello\nWorld") #=> Hello \n World

```

\\ => back slash escape 
```py

print("Hello\\World") #=> Hello\World

```

\' => single quote scape
```py

print("Hello\'World") #=> Hello'World

```

\" => double quotes scape
```py

print("Hello\"World") #=> Hello"World

```

\r => carriage return | take after '\r' word length and replaced in the first
```py

print("12345678\rWorld") #=> World678 

```

\t => tap
```py

print("Hello\tWorld") #=> Hello   World

```

\xhex #=> Hex value
```py

print("\x61\x69\x69\x6F\x62") #=> aiiob

```

### strings:-
  - ''' & """ 
    - save the output string write with same design

```py

print(
  '''lorem,
  why gtaVI not released till now rockstar
  ??????
  '''
) #=> The Output be the same

```

### indexing:-
- All data in python is object
- Every object has he's own elements
- Every element is an index and can access on it
- Can access on strings, lists, tuples, dictionaries, etc

```py

word= "django"

print(word[1]) #=> j
print(word[3]) #=> n
print(word[-1]) #=> o

players= [1, 2, 3, 4, 5, 'messi']
print(players[-1][0]) #=> m

```
### slicing:-
- last not included
- have [start(0) : end : steps(1)]

```py

msg= '''lorem, why gtaVI not released till now rockstar ?????? '''

print(msg[:6]) #=> lorem,
print(msg[11:17]) #=> gtaVI
print(msg[::2]) #=> skip one character

```

### stings methods:-

##### strip, rstrip, lstrip
- Remove the addons from the 'string' by default remove spaces
- .split() work on both sides before, after
- space is a character
- can append characters

```py

.strip() 
.lstrip() 
.rstrip()

```

##### title, capitalize
```py

.title()      #=> make the first character in every word is upper and after 'int'
.capitalize() #=> make the first character in just the first word upper and not after int

```

##### zfill
- put '0' before 'int' in 'string' type
- take the bigger num count as an argument

```py

.zfill()

```

##### split, rsplit
- convert the strings to list 
- by default replace 'space' to 'comma'
- take max num

```py

.split, .rsplit

```

##### upper, lower
```py

.upper() #=> make all characters uppercase
.lower() #=> make all characters lowercase

```

##### center
- put extensions on the string
- take width, addon
- reduce the input width with the extension and put the rest on both sides 
- if the rest not equal, will put the bugger after

```py

.center(5, "#")

```
##### count
- count the string character
- case sensitive
- if give word will count it, if give just an letter will count it

```py

.count()

```

##### swapcase
```py

.swapcase()

```


##### strtswith, endswith
- return BOOL
- take character, start, end
- slice? - so last not included & zero based

```py

.startswith()
.endswith()

```

##### index
- take substring, start, end
- if not found return error


##### find
- take substring, start, end
-  if not found return '-1'


##### rjust, ljust
- take width, fill character


##### splitlines
- return list by using new lines as a comma

##### expandtabs
- control on tabs by replacing '\t' character to whitespaces
- take int


##### istitle
- return bool


##### isspace
- return bool


##### islower
- return bool


##### isidentifier
- return bool 
- can be varName


##### isalpha
- return bool


##### isalnum
- return bool 
- have alpha or num


##### replace
- take oldValue, newValue, count(how many times right->left)


##### join
- take iterable(an element that accept 'looping')
- change LTSD to str and replace the comma with the separator

```py
# syntax.

## who need to join?
'-'

### join to what?
'-'.join(element)

```
