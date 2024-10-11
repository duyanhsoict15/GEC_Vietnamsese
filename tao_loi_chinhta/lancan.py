import random

def tao_loi_sai_ky_tu_trong_tu(tu_goc, ty_le_loi=0.5):
    phim_lan_can = {
        'q': 'wsa',
        'w': 'qasde',
        'e': 'wsdf',
        'r': 'edfgt',
        't': 'rfghy',
        'y': 'tghju',
        'u': 'yhjki',
        'i': 'ujklo',
        'o': 'iklp',
        'p': 'ol',
        'a': 'qwsxz',
        's': 'qwedcxza',
        'd': 'wersfxcv',
        'f': 'ertdgcvb',
        'g': 'rtyfhvbn',
        'h': 'tyugjvbnm',
        'j': 'yuihknm',
        'k': 'uiojlnm',
        'l': 'iopkm',
        'z': 'asx',
        'x': 'zasdc',
        'c': 'xsdfv',
        'v': 'cdfgb',
        'b': 'vfghn',
        'n': 'bghjm',
        'm': 'nhjk',
    }

    tu_loi = list(tu_goc)
    for i in range(len(tu_loi)):
        if random.random() < ty_le_loi and tu_loi[i] in phim_lan_can:
            # Lựa chọn ngẫu nhiênký tự lân cận
            ky_tu_loi = random.choice(phim_lan_can[tu_loi[i]])
            tu_loi[i] = ky_tu_loi

    tu_loi = ''.join(tu_loi)
    return tu_loi

def tao_loi_sai_ky_tu_trong_cau(cau_goc, ty_le_loi=0.5):
    tu_khoang_cach = cau_goc.split()
    cau_loi = []

    for tu in tu_khoang_cach:
        tu_loi = tao_loi_sai_ky_tu_trong_tu(tu, ty_le_loi)
        cau_loi.append(tu_loi)

    cau_loi = ' '.join(cau_loi)
    return cau_loi

cau_goc = "tả."
cau_loi_sai_ky_tu = tao_loi_sai_ky_tu_trong_cau(cau_goc, ty_le_loi=0.5)
print("Câu gốc: ", cau_goc)
print("Câu với lỗi sai ký tự trong từ: ", cau_loi_sai_ky_tu)
