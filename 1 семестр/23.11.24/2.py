def func(a: str) -> None:
    list1 = []
    test_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    for i in a:
        list1.append(i)
    list1.append(None)
    for i in range(0, len(list1)):
        if list1[i]:
                if list1[i+1]:
                    if test_dict[list1[i]] < test_dict[list1[i+1]]:
                        f = list1[i+1]
                        list1[i+1] = None
                        sum += test_dict[f] - test_dict[list1[i]]
                    else:
                        if list1[i] in test_dict:
                            sum += test_dict[list1[i]]
                else:
                    if list1[i] in test_dict:
                        sum += test_dict[list1[i]]

    print(sum)

s = "MCMXCIV"

func(s)