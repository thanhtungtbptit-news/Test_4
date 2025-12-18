def doc_file_tao_dict(ten_file):
    ket_qua = {}

    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            ten, diem = dong.split()
            diem = int(diem)

            if ten not in ket_qua:
                ket_qua[ten] = [diem]
            else:
                ket_qua[ten].append(diem)

    return ket_qua

print(doc_file_tao_dict("data.txt"))

