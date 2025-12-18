def student(da_nop,danh_sach_lop):
    sv_da_nop=danh_sach_lop and da_nop
    sv_chua_nop=danh_sach_lop - da_nop

    return (sv_da_nop,sv_chua_nop)

da_nop = {1, 2, 4, 6}
danh_sach_lop = {1, 2, 3, 4, 5, 6, 7}
sv_da_nop, sv_chua_nop = student(da_nop, danh_sach_lop)
print("Sinh viên đã nộp:", sv_da_nop)
print("Sinh viên chưa nộp:", sv_chua_nop)