def my_list(lst):
    result={}
    for i in range (len(lst)):
        value=lst[i]
        if value not in result:
            result[value]=[]
        result[value].append(i)
    return result
lst=[1,2,3,1,3,4,2]
print(my_list(lst))    
