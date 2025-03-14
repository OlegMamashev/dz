list1 = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]

def santa_user(a: list) -> dict:
    santa = dict()
    for i in list1:
        if len(i)==2:
            santa[i[0]] = i[1]
        else:
            santa[i[0]] = None
    return santa
print(santa_user(list1))
