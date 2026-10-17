n = int(input())

count = 0
k = 1

while count < n:
    for _ in range(k):
        print(k, end=' ')
        count += 1
        if count == n:
            break
    k += 1
