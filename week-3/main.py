# syntax:-
game= {'rock', 'paper', 'scissors', 2}
print(game, end='\n\n') #=> not ordered

# union & |
numbers= {1, 2, 3, 4}
nulpha= {'one', 'two', 'three',  'four'}

# print(nulpha|(1, 2, 3)) # just work with 'set'
print(numbers.union(nulpha), end='\n\n')
print(nulpha|numbers, end='\n\n')

# add
nulpha= {'one', 'two', 'three',  'four'}
nulpha.add(1)
nulpha.add((1, 2))
print(nulpha, end='\n\n')

# copy(shallow)
tuPac= {'california love', 'hit em up'}
biggie= tuPac.copy()

biggie.add('big poppa')
biggie.add('warning')

print(tuPac)
print(biggie, end='\n\n')

# remove(error)
liverpool= {'mo salah', 'arne slot', 'virgil'}
liverpool.remove('arne slot')
print(liverpool, end='\n\n')

# discard(not_error => skip)
liverpool= {'mo salah', 'lamine yamal', 'virgil'}
liverpool.discard('lamine Yamal')
liverpool.discard('mo salah')
print(liverpool, end='\n\n')

# pop(random)
tuPac= {'california love', 'hit em up', 'all eyez on me', 'shorty wanna be a thug'}
print(tuPac.pop(), end='\n\n')

# update(can extend from list)
luck= {'win', 'lose'}
luckV2= ['draw']
luck.update(luckV2)

print(luck.pop().upper(), end='\n\n')

#.difference() & .difference_update(update the original set)

afcon_champions= {'egypt', 'morocco', 'algeria', 'senegal', 'nigeria'}
afcon_nationals= {'tunisia', 'libya', 'morocco', 'algeria'}
print(afcon_champions.difference(afcon_nationals), end='\n\n')
#      what here       is not       here

group_two_afcon= afcon_nationals - afcon_champions 
afcon_champions.difference_update(afcon_nationals)

print(group_two_afcon)
print(afcon_champions, end='\n\n')

#.intersection() & .intersection_update(update the original set)

caf_champions_league = {
    'alahly', 'zamalek', 'sundowns', 'taraji',
    'wydad', 'mazembe', 'raja', 'hafia_conakry'
  }

caf_confederation_cup = {
    'zamalek', 'raja', 'sundowns', 'sfax',
    'USMA', 'berkane', 'etoile_du_sahel', 'FAR_rabat'
  }

most_titles= caf_champions_league & caf_confederation_cup
#               what here        and        here as well  

most_titles= list(most_titles) ; most_titles.sort()
print(most_titles, end='\n\n')

#.symmetric_difference() & .symmetric_difference_update(update the original set)
caf_champions_league= {'alahly', 'sundowns', 'taraji', 'wydad'}
caf_confederation_cup= {'zamalek', 'raja', 'sfax', 'USMA'}

caf_champions= caf_champions_league ^ caf_confederation_cup
#              what here not there and what here not there
print(caf_champions, end='\n\n')

# Return Boolean:-
numsetV1= {1, 2, 3, 4, 5, 40, 30}
numsetV2= {2, 40, 3, 5, 30}

# set1.issuperset(set2) #=> is all 'set2' data in 'set1'?
print(numsetV1.issuperset(numsetV2))                #=> True
print(numsetV2.issuperset(numsetV1), end='\n\n')    #=> False

# set1.issubset(set2)   #=> is all 'set1' data in 'set2'?
print(numsetV2.issubset(numsetV1))                  #=> True
print(numsetV1.issubset(numsetV2), end='\n\n')      #=> False

# set1.isdisjoint(set2) #=> is 'set1,2' disjoint?
print(numsetV2.isdisjoint(numsetV1))                #=> False
print(numsetV1.isdisjoint(numsetV2))                #=> False

