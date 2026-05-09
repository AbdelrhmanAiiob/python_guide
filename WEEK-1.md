# Back to [README](README.md)

- ALL DATA IN PYTHON IS OBJECT -
- COMMENTS IS VERY IMPORTANT IF USE IT RIGHT -
- type() => built-in function to know data types -
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

print1(type({'key':'value', 'age':21})) #=> dictionary

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
print(help('keywords'))

```

### Need to Know

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

