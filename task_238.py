d = int(input('Enter dollars number: '))
ua = float(input('Enter hrivna exchange rate: '))

for i in range(1, d + 1):
    print(f'{i}        {(i * ua):.2f}')
