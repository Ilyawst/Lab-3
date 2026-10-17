n = int(input())

max_score = 0
zero = False

for i in range(n):
    score = int(input())

    if score > max_score:
        max_score = score
    if score == 0:
        zero = True

print(max_score)
if zero == True:
    print("Yes")
else:
    print("No")
    