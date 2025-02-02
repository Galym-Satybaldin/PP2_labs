f = int(input("fahrenheits: "))

def f_to_c (f):
    return (5/9)*(f-32)

c = f_to_c(f)
print (f'your temp in C: {c}')