"""
global variables - variables created outside of a function 
local variables - variables created inside of a function and they can;t be recalled outside of it
"""

x = 6

def operation():
    y = 8
    print (3+y)

operation()
print (3+x)



"""
def myfunc():
  global x  = makes this variable global, even if it's in function
  x = "fantastic"
  
"""