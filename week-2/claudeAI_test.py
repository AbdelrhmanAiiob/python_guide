# 1 #

x, y = 10, 20
x, y = y, x + y

# Solve:- (Right Answer)

  # x= 10
  # y= 20

  # x, y = y, x+y
    ## right first |-> on old values
      # y= 20
      # x= 10+20 => 30
        # after this give the new variables the new data.

print(x, y) #=> 20, 30 

print("-" *20)

# 2 #

tech = "Python"
print(tech[15:30])

#=> ''

print("-" *20)

# 3 #

msg = "Elzero"

  # start => o
  # skip  => r | So now complete 2steps
  # got   => e
  # skip  => z | So now complete 2steps
  # got   => l

print(msg[::-2]) #=> oel

print("-" *20)

# 4 #

text = "elzero-web_school"

  # make upper after => ' ', '-', '_' #

print(text.title()) #=> Elzero-Web_School

print("-" *20)

# 5 #

languages = "Python,Django,Git,Linux"

  # ['Python', 'Django', 'Git,Linux']

print(languages.split(",", 2)) #=> ['Python', 'Django', 'Git,Linux']

print("-" *20)

# 6 #

empty = ""
print(empty.isspace()) #=> False

print("-" *20)

# 7 #

print(14 % -3) #=> -1
print(-14 % 3) #=> 1

print("-" *20)

# 8 #

print(type(7 // 2.0)) #=> float

print("-" *20)

# 9 #

2 + 3 * 2 ** 2

# (2 + 3 * 2 ** 2)
  # 2^2
    # 4

# (2 + 3 * 4)
  # 3 * 4
    # 12

# (2 + 12)
  # 2 + 12
    # 14

print(2 + 3 * 2 ** 2) #=> 14

print("-" *20)

# 10 #

  # Shallow copy=> the main container point on specific value 
    # when you take a copy from it, take from the pointer 
      # so any edit on it -> result be on both sides original, copy

list1 = [[1, 2], [3, 4]]
list2 = list1.copy()
list2[0][0] = 99
print(list1[0][0]) #=> 99

print("-" *20)

# 11 #

  # Search from right->left and change the just first character

items = [10, 20, 30, 20, 10]
items.remove(20)
print(items) #=> [10, 30, 20, 10]

print("-" *20)

# 12 #

  # .insert method take an index, element
    # and put the element on left side or before the index

nums = [1, 2, 4]
nums.insert(-1, 3)
print(nums) #=> [1, 2, 3, 4]

print("-" *20)

# 13 #

  # .sort(reveres=False)
    # if num   => from smaller->bigger
    # if alpha => from a-z

  # sort the elements in the same memory place #

my_list = [3, 1, 2]
result = my_list.sort()

print(result)  #=> NONE
print(my_list) #=> [1, 2, 3]

print("-" *20)

# 14 #

  # .extend deal with index by index

chars = ['a', 'b']
chars.extend('cd')
print(chars) #=> ['a', 'b', 'c', 'd']

print("-" *20)

# 15 #

  # everything in python is object
    # so can deal with any data

my_tuple = ([1, 2], 3)
my_tuple[0].append(3)
print(my_tuple) #=> [[1, 2, 3], 3]

print("-" *20)

# 16 #

  # the arithmetic will execute first
    # so the output is=> 10

val = (5) * 2
print(type(val)) #=> 10

print("-" *20)

# 17 #

  # t += |-> mean t = t+t

t = (1, 2)
t += (3, 4)
print(t) #=> (1, 2, 3, 4)
