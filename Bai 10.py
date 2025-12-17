def my_list(lst):
    result=[]
    for i in lst:
        if i % 2 == 0 and i> 10 :
            result.append(i)
    return result

lst= [3, 8, 10, 12, 15, 18, 20]
print(my_list(lst))


            