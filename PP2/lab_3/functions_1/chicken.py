'''
chicken = 1 head 2 legs

rabbit = 1 head 4 legs

x + y = 35
2x + 4y = 94

x = 35 - y

2(35-y) + 4y = 94
6y = 24
y = 4
x = 31

'''

heads = int(input())
legs = int(input())

def solve (heads, legs):
    rabbits = (legs - heads*2)//2
    chicken = heads - rabbits

    return rabbits, chicken

rabbits, chicken = solve (heads, legs)

print (rabbits)
print (chicken)