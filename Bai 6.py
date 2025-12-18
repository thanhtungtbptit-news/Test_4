def list(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
data=[1,2,2,3,4,5,6,5,7]
print(list(data))
