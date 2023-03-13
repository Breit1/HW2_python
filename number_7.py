num = int(input())
kol = 0
for i in range (1, num + 1):
    if num % i == 0:
        kol += 1
print(kol)