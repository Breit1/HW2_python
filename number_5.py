max_1 = int(input())
kol = 1
while (i := (int(input()))) != 0:
    if max_1 == i:
        kol += 1
    elif i>max_1:
        kol = 1
        max_1 = i

print(kol)