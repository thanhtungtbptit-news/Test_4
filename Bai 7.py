def find_max(lst):
    max_value=lst[0]
    for i in lst:
        if i > max_value:
            max_value=i
    return max_value
print(find_max([3,4,6,7,8]))

