'''

- The Week-2 partOne Training -
- The Level&Solve=> Depends on What u Learn Till Now -

'''

#nums_types:-

123
123.00
45+4j

num= 10
num= float(num)
print(num)
print(type(num), end='\n\n')

num = 159.650
num= int(num)
print(num)
print(type(num), end='\n\n')

print(100 - 115)
print(50 * 30)
print(21 % 4)
print(110 / 11)
print(97 // 20, end='\n\n')

games= ["rimworld   ", "cyberpunk 2077", "sleeping dogs", "mortal compat", "doom"]
print(games[0].capitalize().strip())
# print(games.pop(0).capitalize().strip())
first_one= games[0]
print(first_one.capitalize().strip())

print(games[-1].capitalize())
# last_one= games.pop(-1)
last_one= games[-1]
print(last_one.capitalize(), end='\n\n')

final= games[0].strip()
final_v2= games[2::2]
final_v2.insert(0, final)
print(final_v2, end='\n\n')

print(games[1::2])

games[-1:-3:-1]= ['witcher3', 'witcher3']
print(games, end='\n\n')

games= ["rimworld", "cyberpunk 2077", "sleeping dogs", "mortal compat", "doom"]
print(games[1:4])
print(games[-2:], end='\n\n')

online= ['fortnite', 'valorant', 'lol']
online.append('wild raft')
online.insert(0, 'sons of the forest')
print(online, end='\n\n')

del online[:2]
print(online)
trash= online.pop(-1)
print(online, end='\n\n')

friends = ["Salah", "Zayn"]
employees = ["Justin", "kevin"]
school = ["Ramadan", "Selena"]

friends.extend(employees); friends.extend(school)
print(friends, end='\n\n')

friends.sort()
print(friends)
friends.sort(reverse= True)
print(friends, end='\n\n')

print(len(friends), end='\n\n')

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])