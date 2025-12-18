def dem_so_dong(ten_file):
    f=open(ten_file,"r",encoding="utf-8")
    count=0
    for line in f:
        count += 1
    f.close()
    return count
print(dem_so_dong("test.txt"))