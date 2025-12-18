def ghi_list_ra_file(lst, ten_file):
    f = open(ten_file, "w", encoding="utf-8")
    for item in lst:
        f.write(str(item) + "\n")
    f.close()
