* __Go to__
  * __[README](../README.md)__
  * __[code.py](main.py)__
  * __[assignments.py](assignments.py)__
  <!-- * __[claudeAIassignment.py](assignments.py)__ -->

## Arithmetic Operators:-
- Python deal with specific sort bigger -> smaller
  - and specific way if the arithmetic operation have parentheses '()'

### Types & Sort:-
* Group 1
  * If there are multiple exponents (**) in one expression, they will execute from right -> left

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Exponent|**|High|

---

* Group 2
  * If there are multiple operators in one expression, they will execute from left -> right

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Multiplication|*|Medium|
  |Division|/|Medium|
  |Floor division|//|Medium|
  |Modulus|%|Medium|

---

* Group 3 
  * If there are multiple operators in one expression, they will execute from left -> right

  |**operator**|**sign**|**priority**|
  |------------|--------|------------|
  |Addition|+|Low|
  |Subtraction|-|Low|

---

* Manual arithmetic operation sort.

---

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




























