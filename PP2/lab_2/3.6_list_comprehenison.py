list = ["chess", "baseball", "football", "basketball"]
new_list = [x for x in list if "a" in x]
print (new_list)

newlist = [x.upper() for x in list] 
print (new_list)

#  newlist = [expression for item in iterable if condition == True] 


newls = [x for x in range(10)] 
print (newls)

newlist1 = [x for x in range(10) if x < 5] 
print(newlist1)