list1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
list2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
list3 = [1, 13, 25]

ob_elements = list(filter(lambda x: x in list1, list2))

not_in_list = list1 + list2
not_in_list = list(filter(lambda x: x not in ob_elements, not_in_list))
in_list1 = list(filter(lambda x: x not in ob_elements, list1))
in_list2 = list(filter(lambda x: x not in ob_elements, list2))


if ob_elements:
    print(f"1){len(ob_elements)} элемента: {ob_elements}")
    print(f"2){len(not_in_list)} элементов: {not_in_list}")
    print(f"3){len(in_list1)} элементов: {in_list1}")
    print(f"4){len(in_list2)} элементов: {in_list2}")
else: print("Общих элементов нет.")