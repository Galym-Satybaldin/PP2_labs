'''
those which return True

print (bool (15))
print (bool ("hello")) #returns true
print (bool(['apple', 'cherry']))
'''

#return False
print (bool(""))
print (bool(None))
print (bool([]))
print (bool({}))

class EmptyBox:
    def __len__(self):
        return 0

nothing = EmptyBox()
print(len(nothing))    # Prints 0
print(bool(nothing))   # Prints False