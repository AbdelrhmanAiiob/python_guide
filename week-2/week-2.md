* **__Go to__**
  * __[README](../README.md)__
  * __[code.py](main.py)__
  * __[training.py](training.py)__
    * __[AI_test.py](claudeAI_test.py)__  
  <!-- * __[claudeAIassignment.py](assignments.py)__ -->

1. **Arithmetic Operators:-**
- Python deal with specific sort bigger -> smaller
  - and specific way if the arithmetic operation have parentheses '()'

- **Types & Sort:-**
  * Group 1
    * If there are multiple exponents (**) in one expression, they will execute from right -> left

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Exponent|**|High|

  * Group 2
    * If there are multiple operators in one expression, they will execute from left -> right

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Multiplication|*|Medium|
  |Division|/|Medium|
  |Floor division|//|Medium|
  |Modulus|%|Medium|

  * Group 3 
    * If there are multiple operators in one expression, they will execute from left -> right

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Addition|+|Low|
  |Subtraction|-|Low|


```py

23**4%2-1+100/5//2*7**9

#1- 9**7          => 40353607
  # 23**4%2-1+100/5//2*40353607

#2- 23**4         => 279841
  # 279841%2-1+100/5//2*40353607

#3- 279841%2      => 1
  # 1-1+100/5//2*40353607

#4- 100/5         => 20.0
  # 1-1+20.0//2*40353607

#5- 20.0//2       => 10.0
  # 1-1+10.0*40353607

#6- 10.0*40353607 => 403536070.0
  # 1-1+403536070.0

#7- 1-1           => 0
  # 0+403536070.0

#8- 0+403536070.0 => 403536070.0

# The Result => 403536070.0
```

---

  * **Manual arithmetic** operation sort.
    * now the highest priority go to '()'
      * #Here | 5**5+(20-1) |> will start with '**20-1**' no matter what. 


```py
(23**4%(6*3)+100/5//2*7**9) 

#1- 6*3            => 18 
  # (23**4%18+100/5//2*7**9) 

#2- 9**7           => 40353607
  # (23**4%18+100/5//2*40353607)

#3- 23**4          => 279841
  # (279841%18+100/5//2*40353607)

#4- 279841%18      => 13
  # (13+100/5//2*40353607)

#5- 100/5          => 20.0
  # (13+20.0//2*40353607)

#6- 20.0//2        => 10.0
  # (13+10.0*40353607)

#7- 10.0*40353607  => 403536070.0
  # (13+403536070.0)

#8- 13+403536070.0 => 403536083.0
  # (403536083.0)

# The Result => 403536083.0
```

---

2. **list:-**
    * Closed by => []
    * Not unique so can have diff data types
    * Ordered so can access all elements in it
    * Accept add, edit, delete
```py

# syntax:-
players= ['mo salah', 'messi', 'cristiano', 'neymar']
print(players)       #=> ['mo salah', 'messi', 'cristiano', 'neymar']
print(type(players)) #=> list

games= ['rdr2', '1', 'witcher3', '2']
print(games)         #=> ['rdr2', '1', 'witcher3', '2']
print(type(games))   #=> list
```
  #NOTE
  ```py

  # to remove more than element
  del list_name['start':'end']
  ```

  * **list_index:-**
```py
print(players[-1]) #=> neymar
print(players[0].title())  #=> Mo Salah |> here we can use string methods cause the output is 'string'.
print(type(players[0]))    #=> str
print(players[2])  #=> cristiano
print(players[1])  #=> messi
```

  * **list_slicing:-**
    * Slicing return a list of items.
    * By default slicing move +1 step left-right to forward, to go backwards from u need negative steps.
```py

print(players[-1 : -3 : -1]) #=> Neymar, Cristiano
print(players[ :1])  #=> Mo Salah
```

  * **list_edit:-**
```py

nationals= ['egypt', 'usa', 'kuwait', 'algeria']
nationals[1]= 'saudi'
nationals[-1]= 'jordan' 
nationals[1]= 'algeria'
nationals[2]= 3
print(nationals) #=> ['egypt', 'algeria', 3, 'jordan']

nationals[2 : 4]= ['tunisia']
print(nationals) #=> ['egypt', 'algeria', 'tunisia']
```

  * **list_methods:-**

  * append
    * append data in the last of the list
    * if append iterable will add as one element
```py

print('-'*20, end='\n\n')
rdr2= ['arthur', 'uncle', 'micah']
rdr2.append('sadie')
rdr2.append(888)
print(rdr2) #=> ['arthur', 'uncle', 'micah', 'sadie', 'marry', 888]

rdr2_bad= ['pinkerton', 'red_indian']
rdr2.append(rdr2_bad) #=> ['arthur', 'uncle', 'micah', 'sadie', 888, ['pinkerton', 'red_indian']]
print(rdr2)

# can index on new list.
print(rdr2[-1][0].capitalize()) #=> pinkerton
```

  * extend
    * extend other iterable with the list in the last on the list
```py

a= ['A', 'B']
e= ['C', 'D', 'F']
a.extend(e)
print(a) #=> ['A', 'B', 'C', 'D', 'F']

```

  * sort(reverse= False)
    * if 'int' 
      * smaller->bigger
    * if 'str'
      * alphabetical
    * Cant go both of them
      * reverse= False by default
```py

a= ['B', 'A', 'D', 'C']
z= [9, 8, 1, 6, 7, 8, 2, 4, 3, 5]

a.sort() #=> ['A', 'B', 'C', 'D']
print(a)
a.sort(reverse= True) #=> ['D', 'C', 'B', 'A']
print(a)
z.sort() #=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(z)
z.sort(reverse= True) #=> [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(z)
```

  * .reverse
    * it is just reverse
```py

x= [9, 8, 7, 6, 5, 4, 3, 2, 1]
b= ['A', 'B', 'C', 'D']
x.reverse()
b.reverse()
print(x) #=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b) #=> ['D', 'C', 'B', 'A']
```
  * clear
    * clear all data in list without remove it 
```py

list_name.clear()
```
  * copy
    * take shallow copy
      * if the main list edited, the copy not effect
```py

list_name.copy()
```
  * count
```py

list_name.count(element)
```
  * index
```py

list_name.index(element)
```
  * insert
    * append data in anyplace.
      * take index and put the data before
      * negative=> on the left
```py

b= ['A', 'B', 'C', 'D']
b.insert(0, 123)
b.insert(-1, 5)
print(b) #=> [123, 'A', 'B', 'C', 5, 'D']
```
  * pop
    * take index
      * take an element from the list
      * 'take it'=> make it independent  
```py

b= ['A', 'B', 'C', 'D']
c= b.pop(0)
print(b)         #=> ['B', 'C', 'D']
print(c.lower()) #=> a
```
---

3. **tuple:-**
    * Closed by '()' | can without it.
    * Ordered so can access the on it
    * Immutable so cant edit(by normal way)
    * Not unique
```py

#syntax:-
guess= ('rock', 'paper', 'scissors') #=> tuple.
guess= 'rock', 'paper', 'scissors'   #=> tuple.

num= ('tuple',) #=> tuple.
num= 'tuple',   #=> tuple. 

# cant edit:-
# guess[0]= 1 error
```

#NOTE-tupleEdit
```py

# to edit a 'tuple' for some reason.
  # change type, edit, back
    # using 'list()' & 'tuple()' built-in function.

nums= (1, 2, 3)
nums= list(nums)
nums[1]= 'two'
nums= tuple(nums)
print(nums)       #=> (1, 'two', 3)
print(type(nums)) #=> tuple
```

  * repeat
```py

b= (4, 5, 6)
print(b* 2)
```

  * **tuple_methods:-**

    * .count() = TomatoTomato
    * .index() = TomatoTomato

    * LT_destruct |LT= list, tuple|
      ```py

      u= ('a', 'b', 'c')
      a, b, c = u
      print(a)
      print(b)
      print(c)

      # to skip an index => TRICK |Fake container|
      u= [1, 4, 2, 9, 3]
      one, _, two, _,three = u
      print(one)
      print(two)
      print(three, end='\n\n')
      ```





















