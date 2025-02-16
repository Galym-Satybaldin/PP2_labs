def three_four(num):
    for i in range(1, num+1):
        if (i%3 ==0 and i%4 == 0):
            yield i

num = int(input())
l = list(three_four(num))

for i in l:
    print (i)