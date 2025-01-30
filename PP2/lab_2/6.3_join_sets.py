a = {"a", "b", "c"}
b = {1, 2, 3}

c = a.union(b)
print(c)

c = a | b
print(c)

x = {"a", "b", "c"}
y = {1, 2, 3}
z = {"John", "Elena"}
w = {"apple", "bananas", "cherry"}

s = x.union(y, z, w)
print(s)

s = x | y | z | w
print(s)

m = {"a", "b", "c"}
n = (1, 2, 3)

r = m.union(n)
print(r)