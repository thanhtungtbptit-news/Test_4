def avg_score(score):
    total=sum(score)
    course_number=len(score)   
    return total/course_number    

def classify_score(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    else :
        return "Yếu"
    
def phan_tich_diem(students):
    ket_qua = {}

    for ten in students:
        diem_tb = avg_score(students[ten])
        loai = classify_score(diem_tb)
        ket_qua[ten] = loai

    return ket_qua

students = {
    "An": [8, 7, 9],
    "Binh": [6, 6.5, 7],
    "Chi": [5, 5, 4],
    "Dung": [3, 4, 2]
}

print(phan_tich_diem(students))

