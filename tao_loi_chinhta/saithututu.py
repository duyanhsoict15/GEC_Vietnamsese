import random

def tao_loi_chinh_ta(cu_original):
    # Tách câu thành các từ riêng lẻ
    tu = cu_original.split()

    # Đảo ngẫu nhiên thứ tự các từ
    random.shuffle(tu)

    # Ghép lại các từ để tạo câu mới
    cu_loi_chinh_ta = ' '.join(tu)

    return cu_loi_chinh_ta
cu_original = "Hôm nay là một ngày đẹp trời."
cu_loi_chinh_ta = tao_loi_chinh_ta(cu_original)
print(cu_loi_chinh_ta)
