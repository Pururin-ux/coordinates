print("Введите параметр а:")
a=float(input())
print("Введите параметр b:")
b=float(input())
k=0
eps=1e-4
Sum0=0
c: float = (a * (k ** 2) + 1) / (a * (k ** 4) + (k ** 2) + b)
while abs(c)>=eps:
    Sum0+=c
    k+=1
    c: float = (a * (k ** 2) + 1) / (a * (k ** 4) + (k ** 2) + b)
print(c)

