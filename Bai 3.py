def boolen(x,list):
    for i in x:
        if i == list:
            return True
    return False
print(boolen([1,2,3],3))

def creat(list):
    kq=set()
    for i in list:
        kq.add(i)
    return kq
print(creat([1,2,3,4,5,2]))

