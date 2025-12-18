def my_list(data):
    result={}
    
    for i in data:
        id=i[0]
        value=i[1]
        
        if id not in result:
            result[id]=[]   
        result[id].append(value)

    for id in result:
        result[id]=tuple(result[id])

    return result

data=[(1,"a"),(2,"b"),(3,"c"),(2,"a"),(1,"c")]
print(my_list(data))

