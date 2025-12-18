def my_list(lst):
    result=[]
    for i in lst:
        if i % 2 ==0 and i > 10:
            result.append(i)
    return result
lst=[2,3,11,24,25,18,22,30]    
print(my_list(lst))


            

            