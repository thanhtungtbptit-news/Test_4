def doc_file_scores(ten_file):
    ds = []
    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            ten, diem = dong.split()
            ds.append((ten, int(diem)))
    return ds


def tong_hop_diem(ds):
    temp = {}
    for ten, diem in ds:
        if ten not in temp:
            temp[ten] = [diem]
        else:
            temp[ten].append(diem)

    ket_qua = {}
    for ten in temp:
        ket_qua[ten] = sum(temp[ten]) / len(temp[ten])

    return ket_qua


def ghi_ket_qua_ra_file(dic, ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        for ten, diem_tb in dic.items():
            f.write(f"{ten}: {diem_tb}\n")



ds = doc_file_scores("scores.txt")
ket_qua = tong_hop_diem(ds)
ghi_ket_qua_ra_file(ket_qua, "result.txt")
