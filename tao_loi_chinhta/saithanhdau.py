import random

def tao_loi_thanh_dau_tu_trong_cau(cu_original):
    # Tách câu thành các từ riêng lẻ
    cac_tu = cu_original.split()

    # Tạo danh sách các từ với thanh đau bị thay đổi
    tu_loi_thanh_dau = []

    for tu in cac_tu:
        # Kiểm tra xem từ có ít hơn 3 ký tự không thì không tạo lỗi
        if len(tu) >= 3:
            # Chọn ngẫu nhiên một vị trí trong từ để thay đổi thanh
            vi_tri_thay_doi = random.randint(0, len(tu) - 1)
            thanh_moi = random.choice(['sắc', 'huyền', 'hỏi', 'ngã'])
            tu_moi = tu[:vi_tri_thay_doi] + thanh_moi + tu[vi_tri_thay_doi + 1:]
        else:
            tu_moi = tu

        tu_loi_thanh_dau.append(tu_moi)

    # Ghép lại các từ để tạo câu mới
    cu_loi_thanh_dau = ' '.join(tu_loi_thanh_dau)

    return cu_loi_thanh_dau
cu_original = "Hôm nay là một ngày đẹp trời."
cu_loi_thanh_dau = tao_loi_thanh_dau_tu_trong_cau(cu_original)
print(cu_loi_thanh_dau)
