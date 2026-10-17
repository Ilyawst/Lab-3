import sys
n = int(input())
r = ''
if n > 9:
    sys.exit()
else:
    for i in range(1, n + 1):
        r += str(i)
        print(r)
        