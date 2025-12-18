def thong_ke_file(ten_file):
    ds_so = []

    with open(ten_file, "r", encoding="utf-8") as f:
        for dong in f:
            so = int(dong.strip())
            ds_so.append(so)

    tap_khong_trung = set(ds_so)
    so_lon_nhat = max(ds_so)
    so_nho_nhat = min(ds_so)
    trung_binh = sum(ds_so) / len(ds_so)

    return (tap_khong_trung, so_lon_nhat, so_nho_nhat, trung_binh)

print(thong_ke_file("numbers.txt"))
