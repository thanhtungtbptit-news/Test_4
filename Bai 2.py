def count(tuple,x):
    count = 0 
    for i in tuple:
        if i == x:
            count += 1
    return count
s=(1,2,3,3,3,3,4,5,6)
print(f"Số lần xuất hiện ",count(s,3))