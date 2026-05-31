* **__Go to__**
  * __[README](../README.md)__
  * __[code.py](main.py)__
  * __[training.py](training.py)__
  <!-- * __[claudeAIassignment.py](assignments.py)__ -->

1. **set:-**
	 * Closed by {}
	 * In data unique
	 * Not ordered => so cant access 'Index'
	 * Only accept immutable data types => nums, strings, tuple, etc
			```py

			game= {'rock', 'paper', 'scissors'}
			print(game)
			```

	* **set_methods:-** 

		*  **.union |**
			```py
			
			numbers= {1, 2, 3, 4}
			nulpha= {'one', 'two', 'three',  'four'}

			print(numbers.union(nulpha), end='\n\n')
			print(nulpha|numbers, end='\n\n')
			```
		
		*  **.add => '1' element**
			```py
			
			nulpha= {'one', 'two', 'three',  'four'}

			nulpha.add(1)
			nulpha.add((1, 2))
			print(nulpha)
			```
		
		*  **.copy(shallow)**
			```py
			
			tuPac= {'california love', 'hit em up'}
			biggie= tuPac.copy()

			biggie.add('big poppa')
			biggie.add('warning')
			print(tuPac)
			print(biggie)
			```
		
		*  **.remove(error)**
			```py
			
			liverpool= {'mo salah', 'arne slot', 'virgil'}

			liverpool.remove('arne slot')
			print(liverpool)
			```
		
		*  **.discard(not_error => skip)**
			```py
			
			liverpool= {'mo salah', 'lamine yamal', 'virgil'}

			liverpool.discard('lamine Yamal')
			liverpool.discard('mo salah')
			print(liverpool)
			```
		
		*  **.pop(random)**
			```py
			
			tuPac= {'california love', 'hit em up', 'all eyez on me', 'shorty wanna be a thug'}
			
			print(tuPac.pop())
			```
		
		*  **.update(can extend from list)**
			* Update the set, adding elements from all others.
			```py
			
			luck= {'win', 'lose'}
			luckV2= ['draw']
			luck.update(luckV2)

			print(luck.pop().upper())
			```

	* **set_edit:-**

    	* .difference() & .difference_update(update the original set)
    		* set1.difference(set2) |> set1 - set2
    		* what in (set1) and not in set2
    		```py

    		afcon_champions= {'egypt', 'morocco', 'algeria', 'senegal', 'nigeria'}
    		afcon_nationals= {'tunisia', 'libya', 'morocco', 'algeria'}
    		print(afcon_champions.difference(afcon_nationals), end='\n\n')
    		#      what here       is not       here

    		group_two_afcon= afcon_nationals - afcon_champions 
    		afcon_champions.difference_update(afcon_nationals)
    		print(group_two_afcon)
    		print(afcon_champions)
    		```

			* .intersection() & .intersection_update(update the original set)
				* set1.intersection(set2) |> set1 & set2
				* what in both => "what in set1 & set2 as well"
				```py

				caf_champions_league = {
					'alahly', 'zamalek', 'sundowns', 'taraji',
					'wydad', 'mazembe', 'raja', 'hafia_conakry'
				}
				caf_confederation_cup = {
					'zamalek', 'raja', 'sundowns', 'sfax',
					'USMA', 'berkane', 'etoile_du_sahel', 'FAR_rabat'
				}

				most_titles= caf_champions_league.intersection(caf_confederation_cup)
				#              what here             and             here as well  

				most_titles= list(most_titles) ; most_titles.sort()
				print(most_titles)
				```

			* .symmetric_difference() & .symmetric_difference_update(update the original set)
				* set1.symmetric_difference(set2) |> se1 ^ set2
				* what in 'set1' and not in 'set2' & what in 'set2' and not in 'set1' 
				```py

				caf_champions_league= {'alahly', 'sundowns', 'taraji', 'wydad'}
				caf_confederation_cup= {'zamalek', 'raja', 'sfax', 'USMA'}

				caf_champions= caf_champions_league.symmetric_difference(caf_confederation_cup) 
				#              what here not there      and          what here not there
				print(caf_champions) 
				```


	* **BOOLEAN:-**
		```py

		# set1.issuperset(set2) #=> is all 'set2' data in 'set1'?
		print(numsetV1.issuperset(numsetV2))                #=> True
		print(numsetV2.issuperset(numsetV1), end='\n\n')    #=> False
		
		# set1.issubset(set2)   #=> is all 'set1' data in 'set2'?
		print(numsetV2.issubset(numsetV1))                  #=> True
		print(numsetV1.issubset(numsetV2), end='\n\n')      #=> False
		
		# set1.isdisjoint(set2) #=> is 'set1,2' disjoint?
		print(numsetV2.isdisjoint(numsetV1))                #=> False
		print(numsetV1.isdisjoint(numsetV2))                #=> False
		```



