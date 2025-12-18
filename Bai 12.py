def my_list(names):
    unique_name=set()
    for name in names:
        unique_name.add(name.lower())
    
    result = []

    for name in unique_name:
        result.append(name.capitalize())
    
    return result
dict=["Binh","aN","TuNg","binh","Lam","lam"]
print(my_list(dict))