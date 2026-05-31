# set:-

my_set= {1, 1.0, '1'}
  # set is unique 
    ## 1 == 1.0 |> so they share the same hash value
      ### treats them as a duplicate 

print(len(my_set), end='\n\n') #=> 2

set1 = {1, 2, 3}
set2 = {3, 4, 5}
  # x - x => difference
  # x & x => intersection
  # x ^ x => symmetric_difference

print(set1 ^ set2, end='\n\n') #=> {1, 2, 4, 5} 

my_set = {True, 1, 1.0}
  # True is evaluates to a value of '1'
    # so python logic as (Interpreted):-
      # => True <= first element save in memory
        # 1 == 1.0 and share the same hash with 'True'
          # so result will be first element save it in memory => 'True'

print(my_set, end='\n\n') #=> True

s1 = {1, 2, 3}
s2 = {4, 5}
# isdisjoint => always return bool

print(s1.isdisjoint(s2)) #=> True
