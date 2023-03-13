num = int(input())
kol = 0
f = 1
while num > 0:
    f *= num
    num -= 1
    kol += f + 1
print(kol)