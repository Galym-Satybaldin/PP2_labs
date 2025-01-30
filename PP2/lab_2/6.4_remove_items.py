s = {"apple", "banana", "cherry"}

s.remove("banana")
print(s)

s = {"apple", "banana", "cherry"}
s.discard("banana")
print(s)

s = {"apple", "banana", "cherry"}
print(s.pop())
print(s)

s = {"apple", "banana", "cherry"}
s.clear()
print(s)

s = {"apple", "banana", "cherry"}
del s
print(s)


s = {"apple", "banana", "cherry"}

for item in s:
    print(item)