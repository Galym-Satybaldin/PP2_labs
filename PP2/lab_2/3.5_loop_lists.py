sports_games = ["chess", "baseball", "football", "basketball"]

for sport in sports_games:
    print (sport)
print ("\n")

#or

for i in range (len(sports_games)):
    print (sports_games[i])
print ("\n")

#or
i = 0
while i < len(sports_games):
    print (sports_games[i])
    i = i+1

print ("\n")

#list comrehension

[print(x) for x in sports_games]