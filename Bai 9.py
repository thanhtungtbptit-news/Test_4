def my_dict(key,value):
    result={}
    for i in key:
        result[i]=key[i]

    for i in value:
        if i in result:
            result[i] += value[i]
        else:
            result[i] = value[i]
    return result

key ={"a":2,"b": 3}           
value = {"b": 4, "c": 5}

print(my_dict(key,value))

             
