def my_list(lst):
    numb={}
    for i in lst:
        if i in numb:
            numb[i] += 1
        else :
            numb[i] = 1
    return numb
print(my_list([1,1,1,2,3,4,4,5,6,7]))        
