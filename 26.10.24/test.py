data = [('a', 1), ('b', 1), ('b', 2)]
d1 = {}
for key, val in data:
    d1[key] = d1.get(key, []) + [val]
print(d1)
