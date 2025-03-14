list1 = [1, 2, 3, 4, 4, 8]
list1 = list(set(list1))
# print(list1)

# mnozestva = list(filter(lambda x: [x, b for b in list1 if b!=x] in list1))
# mnozestva = list(map(lambda x: [x, [b for b in list1 if b != x]], list1))
mnozestva = list(map(lambda x: [[x, b] for b in list1[list1.index(x):] if b != x], list1))

print(mnozestva)