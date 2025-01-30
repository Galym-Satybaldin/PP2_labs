s = {1, 2, 3}
s.add(4)
print(s)

s.clear()
print(s)

a = {1, 2, 3}
b = a.copy()
print(b)

x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print(x.difference(y))

x.difference_update(y)
print(x)

s = {1, 2, 3}
s.discard(2)
print(s)

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

a.intersection_update(b)
print(a)

print({1, 2, 3}.isdisjoint({4, 5, 6}))
print({1, 2}.issubset({1, 2, 3}))
print({1, 2, 3}.issuperset({1, 2}))

s = {1, 2, 3}
print(s.pop())
print(s)

s = {1, 2, 3}
s.remove(2)
print(s)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))

a.symmetric_difference_update(b)
print(a)

a = {1, 2, 3}
b = {4, 5, 6}
print(a.union(b))

a.update(b)
print(a)