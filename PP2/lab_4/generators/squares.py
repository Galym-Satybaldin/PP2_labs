def squares (num):
    i = 1
    for i in range (i, num+1):
        yield i**2

num = int(input())
print (list((squares(num))))