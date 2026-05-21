# Arithmetic Operators:-
print(23**4%2-1+100/5//2*7**9)      #= 403536070.0
print(23**4%(6*3)+100/5//2*7**9)    #= 403536083.0

print('\n'); print('-' * 20); print('\n')

# List:-
players= ['mo salah', 'messi', 'cristiano', 'neymar']
print(players)       #=> ['mo salah', 'messi', 'cristiano', 'neymar']
print(type(players)) #=> list

games= ['rdr2', '1', 'witcher3', '2']
print(games)         #=> ['rdr2', '1', 'witcher3', '2']
print(type(games), end='\n\n')   #=> list

# list_index
print(players[-1]) #=> neymar
print(players[0].title())  #=> Mo Salah
print(type(players[0]))    #=> str
print(players[2])  #=> cristiano
print(players[1], end='\n\n')  #=> messi

# list_slicing
print(players[-1 : -3 : -1]) #=> Neymar, Cristiano
print(players[ :1], end='\n\n')  #=> Mo Salah

# list-edit
nationals= ['egypt', 'usa', 'kuwait', 'algeria']
nationals[1]= 'saudi'
nationals[-1]= 'jordan' 
nationals[1]= 'algeria'
nationals[2]= 3
print(nationals, end='\n\n')

nationals[2 : 4]= ['tunisia']
print(nationals, end='\n\n')

# list_methods #

# .append
print('-'*20, end='\n\n')
rdr2= ['arthur', 'uncle', 'micah']
rdr2.append('sadie')
rdr2.append(888)
print(rdr2)

rdr2_bad= ['pinkerton', 'red_indian']
rdr2.append(rdr2_bad)
print(rdr2)

# can index on new list.
print(rdr2[-1][0].capitalize())

# .extend
a= ['A', 'B']
e= ['C', 'D', 'F']
a.extend(e)
print(a, end='\n\n')

# .sort()
a= ['B', 'A', 'D', 'C']
z= [9, 8, 1, 6, 7, 8, 2, 4, 3, 5]

a.sort()
print(a)
a.sort(reverse= True)
print(a)
z.sort() 
print(z)
z.sort(reverse= True)
print(z, end='\n\n')

# .reverse()
x= [9, 8, 7, 6, 5, 4, 3, 2, 1]
b= ['A', 'B', 'C', 'D']
x.reverse()
b.reverse()
print(x)
print(b, end='\n\n')

# .clear()
x.clear()
print(x, end='\n\n')

# .copy()
a= [1, 2, 3, 4]
c= a.copy()
print(a)
print(c)

a.append(5)
print(a)
print(c, end='\n\n')

# .count()
z= [9, 8, 1, 6, 7, 8, 2, 4, 1, 1, 3, 5]
print(z.count(1), end='\n\n')

# .index()
print(z.index(9), end='\n\n')

# .insert
b= ['A', 'B', 'C', 'D']
b.insert(0, 123)
b.insert(-1, 5)
print(b, end='\n\n')

# .pop()
b= ['A', 'B', 'C', 'D']
c= b.pop(0)
print(b)
print(c.lower())

print('\n'); print('-' * 20); print('\n')

# tuple:-
guess= ('rock', 'paper', 'scissors')

# cant edit:-
# guess[0]= 1 error

a= (1, 2, 3)
b= (4, 5, 6)

# Everything in python is 'OBJECT'
print(a[1] + b[-1], end='\n\n') #> 8

# repeat.
b= (4, 5, 6)
print(b* 2, end='\n\n')

# LT_destruct
u= ('a', 'b', 'c')
a, b, c = u
print(a)
print(b)
print(c)

# to skip an index => TRICK
u= [1, 4, 2, 9, 3]
one, _, two, _,three = u
print(one)
print(two)
print(three, end='\n\n')