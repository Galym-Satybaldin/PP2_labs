sports_games = ["chess", "baseball", "baseball", "football", "basketball"]
sports_games.remove ("baseball") #only removes first occurence of baseball word
print (sports_games)


sports_games.pop(2) #removes element with index of 2
print (sports_games)

sports_games.pop() #removes last element
print (sports_games)

del sports_games [1] #works also as pop() but 
print (sports_games)

'''del sports_games #deletes the list completely
print (sports_games)'''

sports_games.clear() #list remains but it is empty now
print (sports_games)
