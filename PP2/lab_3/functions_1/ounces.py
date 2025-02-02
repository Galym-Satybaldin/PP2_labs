grams = int(input("weight in grams: "))


def ou_to_gr (grams):
    return 28.3495231 * grams

ounces = ou_to_gr(grams)
print (f'your weight in ounces is: {ounces}')

'''
OR  
ounces = 1
grams = int(input())

def ou_to_gr (grams):
    global ounces 
    ounces = k * grams

ou_to_gr(grams)
print ("weight: " ounces)

'''


