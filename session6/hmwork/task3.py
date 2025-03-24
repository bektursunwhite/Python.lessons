def common_elements(lst1, lst2): 
    all_lst = lst1 + lst2
    unique_num = set(all_lst)

    return unique_num

print(common_elements([1, 2, 3, 4,], [3, 4, 5, 6]))