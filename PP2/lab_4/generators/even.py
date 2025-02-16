def evenNum(num):
    for i in range (2, num+1, 2):
        yield i

num = int(input())
l = list(evenNum(num))

print (', '.join(map(str, l)))