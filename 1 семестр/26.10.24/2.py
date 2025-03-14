a = str("113")


def getnumbers(number):
    numbers = dict()
    for n in range(len(number)):
        if number[n] in numbers:
            numbers[f'{number[n]}'] = numbers.get(f"{number[n]}",0) + 1
        else:
            numbers.setdefault(number[n],1)
    return numbers

pr = getnumbers(a)
print(pr)
for i in range(len(a)):
    new = a[i]
    for n in range()