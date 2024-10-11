import random

def tao_loi_chinh_ta_trong_cau(cu_original):
    # Tách câu thành các từ riêng lẻ
    cac_tu = cu_original.split()

    # Tạo danh sách các từ bị xáo trộn
    tu_loi_chinh_ta = []

    for tu in cac_tu:
        # Chuyển từ thành danh sách các ký tự
        ky_tu = list(tu)

        # Kiểm tra xem từ có ít hơn 3 ký tự không thì không tạo lỗi
        if len(ky_tu) >= 3:
            # Đảo ngẫu nhiên vị trí các ký tự (trừ ký tự đầu và ký tự cuối)
            for i in range(1, len(ky_tu) - 2):
                j = random.randint(i + 1, len(ky_tu) - 1)
                ky_tu[i], ky_tu[j] = ky_tu[j], ky_tu[i]

        # Ghép lại các ký tự để tạo từ mới
        tu_moi = ''.join(ky_tu)
        tu_loi_chinh_ta.append(tu_moi)

    # Ghép lại các từ để tạo câu mới
    cu_loi_chinh_ta = ' '.join(tu_loi_chinh_ta)

    return cu_loi_chinh_ta
cu_original = "Hôm nay là một ngày đẹp trời."
cu_loi_chinh_ta = tao_loi_chinh_ta_trong_cau(cu_original)
print(cu_loi_chinh_ta)
