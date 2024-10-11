import random

def tao_loi_lap_lai_tu(cu_original):
    # Tách câu thành các từ riêng lẻ
    cac_tu = cu_original.split()

    # Tạo danh sách các từ bị lặp lại
    tu_loi_lap_lai = []

    for tu in cac_tu:
        # Kiểm tra xem từ có ít hơn 3 ký tự không thì không tạo lỗi
        if len(tu) >= 3:
            # Chọn một số lần lặp lại ngẫu nhiên từ 2 đến 4 lần
            so_lan_lap = random.randint(2, 4)
            tu_lap_lai = ' '.join([tu] * so_lan_lap)
        else:
            tu_lap_lai = tu

        tu_loi_lap_lai.append(tu_lap_lai)

    # Ghép lại các từ để tạo câu mới
    cu_loi_lap_lai = ' '.join(tu_loi_lap_lai)

    return cu_loi_lap_lai
cu_original = "Hôm nay là một ngày đẹp trời."
cu_loi_lap_lai = tao_loi_lap_lai_tu(cu_original)
print(cu_loi_lap_lai)
