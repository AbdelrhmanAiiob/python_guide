* **__Go to__**
  * __[README](../README.md)__
  * __[code.py](main.py)__
  * __[training.py](training.py)__
  <!-- * __[claudeAIassignment.py](assignments.py)__ -->

1. **set:-**
    * closed by {}
    * unique
    * nor ordered
    * only accept immutable data types
```py

game= {'rock', 'paper', 'scissors'}
print(game)
```

.union |
.add => 1argument
.copy(shallow)
.remove(error)
.discard(not_error_=> skip)
.pop(random)
.update(can update from list)



# syntax

.difference() | .difference_update(update the original set)
set1.difference(set2) |> set1 - set2
what in (set1) and not in set2


.intersection() | .intersection_update(update the original set)
set1.intersection(set2) |> set1 & set2
what in both "what in set1 & set2 as well"

.symmetric_difference() | .symmetric_difference_update(update the original set)
set1.symmetric_difference(set2) |> se1 ^ set2
what in 'set1' and not in 'set2' & what in 'set2' and not in 'set1' 


**BOOLEAN:-**
set1.issuperset(set2) #=> is all 'set2' data in 'set1'?
set1.issubset(set2)   #=> is all 'set1' data in 'set2'?
set1.isdisjoint(set2) #=> is 'set1,2' disjoint?





