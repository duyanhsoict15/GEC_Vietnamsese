import random
import string 
acronym = {"không": ["ko", "k"], "anh": ["a"], "em": ["e"], "biết": ["bít", "bt"], "giờ": ["h"], "gì": ["j"], "muốn": ["mún"],
           "học": ["hc", "hok"], "làm": ["lm"], "yêu": ["iu"], "chồng": ["ck"], "vợ": ["vk"], "ông": ["ô"], "được": ["đc", "dc"],
           "tôi": ["t"], "bạn": ["b","bn", "pạn"], "nước": ["nc"], "không liên quan": ["klq"], "không hiểu sao": ["khs"], "chả hiểu sao": ["chs"],
           "rồi": ["òy", "oy", "r"], "vậy": ["v", "z"], "mới": ["ms"], "vẫn": ["vx"], "Không": ["Ko", "K"], "Anh": ["A"], "Em": ["E"],
           "Biết": ["Bít", "Bt"], "Giờ": ["H"], "Gì": ["J"], "Muốn": ["Mún"], "Học": ["Hc", "Hok"], "Làm": ["Lm"], "Yêu": ["Iu"], "Chồng": ["Ck"],
           "Vợ": ["Vk"], "Ông": ["Ô"], "Được": ["Đc", "Dc"], "Tôi": ["T"], "Bạn": ["B","Bn", "Pạn"], "Nước": ["Nc"], "Không Liên Quan": ["Klq"],
           "Không Hiểu Sao": ["Khs"], "Chả Hiểu Sao": ["Chs"], "Rồi": ["Òy", "Oy", "R"], "Vậy": ["V", "Z"], "Mới": ["Ms"], "Vẫn": ["Vx"], "Yếu": ["Íu"],
           "yếu": ["íu"], "Chiều": ["chìu"], "chiều": ["chìu"], "Tiêu": ["Tiu"], "tiêu": ["tiu"], "Tuổi": ["Tủi"], "tuổi": ["tủi"]}

teen = {"ch": "ck", "ph": "f", "th": "tk", "nh": "nk", "v": "d", "b": "p", "Ch": "Ck", "Ph": "F", "Th": "Tk", "Nh": "Nk", "V": "D", "B": "P","d": "z", "D":"Z"}



telex_dict = {"ă":"aw","â":"aa","á":"as","à":"af","ả":"ar","ã":"ax","ạ":"aj","ắ":"aws","ổ":"oor","ỗ":"oox","ộ":"ooj","ơ":"ow",
"ằ":"awf","ẳ":"awr","ẵ":"awx","ặ":"awj","ó":"os","ò":"of","ỏ":"or","õ":"ox","ọ":"oj","ô":"oo","ố":"oos","ồ":"oof",
"ớ":"ows","ờ":"owf","ở":"owr","ỡ":"owx","ợ":"owj","é":"es","è":"ef","ẻ":"er","ẽ":"ex","ẹ":"ej","ê":"ee","ế":"ees","ề":"eef",
"ể":"eer","ễ":"eex","ệ":"eej","ú":"us","ù":"uf","ủ":"ur","ũ":"ux","ụ":"uj","ư":"uw","ứ":"uws","ừ":"uwf","ử":"uwr","ữ":"uwx",
"ự":"uwj","í":"is","ì":"if","ỉ":"ir","ị":"ij","ĩ":"ix","ý":"ys","ỳ":"yf","ỷ":"yr","ỵ":"yj","đ":"dd",
"Ă":"Aw","Â":"Aa","Á":"As","À":"Af","Ả":"Ar","Ã":"Ax","Ạ":"Aj","Ắ":"Aws","Ổ":"Oor","Ỗ":"Oox","Ộ":"Ooj","Ơ":"Ow",
"Ằ":"AWF","Ẳ":"Awr","Ẵ":"Awx","Ặ":"Awj","Ó":"Os","Ò":"Of","Ỏ":"Or","Õ":"Ox","Ọ":"Oj","Ô":"Oo","Ố":"Oos","Ồ":"Oof",
"Ớ":"Ows","Ờ":"Owf","Ở":"Owr","Ỡ":"Owx","Ợ":"Owj","É":"Es","È":"Ef","Ẻ":"Er","Ẽ":"Ex","Ẹ":"Ej","Ê":"Ee","Ế":"Ees","Ề":"Eef",
"Ể":"Eer","Ễ":"Eex","Ệ":"Eej","Ú":"Us","Ù":"Uf","Ủ":"Ur","Ũ":"Ux","Ụ":"Uj","Ư":"Uw","Ứ":"Uws","Ừ":"Uwf","Ử":"Uwr","Ữ":"Uwx",
"Ự":"Uwj","Í":"Is","Ì":"If","Ỉ":"Ir","Ị":"Ij","Ĩ":"Ix","Ý":"Ys","Ỳ":"Yf","Ỷ":"Yr","Ỵ":"Yj","Đ":"Dd"}

vowel_variants = {
    'a': ['à', 'á', 'ã', 'ạ'],
    'à': ['a', 'á', 'ã', 'ạ'],
    'á': ['à', 'a', 'ã', 'ạ'],
    'ã': ['à', 'á', 'a', 'ạ'],
    'ạ': ['à', 'á', 'ã', 'a'],
    'ă': ['ắ', 'ằ', 'ẵ', 'ặ'],
    'ắ': ['ă', 'ằ', 'ẵ', 'ặ'],
    'ằ': ['ă', 'ắ', 'ẵ', 'ặ'],
    'ẵ': ['ă', 'ắ', 'ằ', 'ặ'],
    'ặ': ['ă', 'ắ', 'ằ', 'ẵ'],
    'â': ['ấ', 'ầ', 'ẫ', 'ậ', 'ẩ'],
    'ấ': ['â', 'ầ', 'ẫ', 'ậ', 'ẩ'],
    'ầ': ['â', 'ấ', 'ẫ', 'ậ', 'ẩ'],
    'ẫ': ['â', 'ấ', 'ầ', 'ậ', 'ẩ'],
    'ậ': ['â', 'ấ', 'ầ', 'ẫ', 'ẩ'],
    'ẩ': ['â', 'ấ', 'ầ', 'ẫ', 'ậ'],
    'e': ['è', 'é', 'ẽ', 'ẹ'],
    'è': ['e', 'é', 'ẽ', 'ẹ'],
    'é': ['è', 'e', 'ẽ', 'ẹ'],
    'ẽ': ['è', 'e', 'é', 'ẹ'],
    'ẹ': ['è', 'e', 'é', 'ẽ'],
    'ê': ['ề', 'ế', 'ễ', 'ệ', 'ể'],
    'ề': ['ê', 'ế', 'ễ', 'ệ', 'ể'],
    'ế': ['ê', 'ê', 'ễ', 'ệ', 'ể'],
    'ễ': ['ê', 'ê', 'ễ', 'ệ', 'ể'],
    'ệ': ['ê', 'ê', 'ễ', 'ệ', 'ể'],
    'ể': ['ê', 'ê', 'ễ', 'ệ', 'ể'],
    'i': ['ì', 'í', 'ĩ', 'ị'],
    'ì': ['i', 'í', 'ĩ', 'ị'],
    'í': ['ì', 'i', 'ĩ', 'ị'],
    'ĩ': ['ì', 'i', 'í', 'ị'],
    'ị': ['ì', 'i', 'í', 'ĩ'],
    'o': ['ò', 'ó', 'õ', 'ọ'],
    'ò': ['o', 'ó', 'õ', 'ọ'],
    'ó': ['o', 'ò', 'õ', 'ọ'],
    'õ': ['o', 'ò', 'ó', 'ọ'],
    'ọ': ['o', 'ò', 'ó', 'õ'],
    'ô': ['ồ', 'ố', 'ỗ', 'ộ', 'ổ'],
    'ồ': ['ô', 'ố', 'ỗ', 'ộ', 'ổ'],
    'ố': ['ô', 'ô', 'ỗ', 'ộ', 'ổ'],
    'ỗ': ['ô', 'ô', 'ồ', 'ộ', 'ổ'],
    'ộ': ['ô', 'ô', 'ồ', 'ố', 'ổ'],
    'ổ': ['ô', 'ô', 'ồ', 'ố', 'ỗ'],
    'ơ': ['ờ', 'ớ', 'ỡ', 'ợ', 'ở'],
    'ờ': ['ơ', 'ớ', 'ỡ', 'ợ', 'ở'],
    'ớ': ['ơ', 'ơ', 'ỡ', 'ợ', 'ở'],
    'ỡ': ['ơ', 'ơ', 'ờ', 'ợ', 'ở'],
    'ợ': ['ơ', 'ơ', 'ờ', 'ớ', 'ở'],
    'ở': ['ơ', 'ơ', 'ờ', 'ớ', 'ỡ'],
    'u': ['ù', 'ú', 'ũ', 'ụ'],
    'ù': ['u', 'ú', 'ũ', 'ụ'],
    'ú': ['u', 'ù', 'ũ', 'ụ'],
    'ũ': ['u', 'ù', 'ú', 'ụ'],
    'ụ': ['u', 'ù', 'ú', 'ũ'],
    'ư': ['ừ', 'ứ', 'ữ', 'ự', 'ử'],
    'ừ': ['ư', 'ứ', 'ữ', 'ự', 'ử'],
    'ứ': ['ư', 'ư', 'ữ', 'ự', 'ử'],
    'ữ': ['ư', 'ư', 'ừ', 'ự', 'ử'],
    'ự': ['ư', 'ư', 'ừ', 'ứ', 'ử'],
    'ử': ['ư', 'ư', 'ừ', 'ứ', 'ữ'],
    'y': ['ỳ', 'ý', 'ỹ', 'ỵ'],
    'ỳ': ['y', 'ý', 'ỹ', 'ỵ'],
    'ý': ['y', 'ỳ', 'ỹ', 'ỵ'],
    'ỹ': ['y', 'ỳ', 'ý', 'ỵ'],
    'ỵ': ['y', 'ỳ', 'ý', 'ỹ']
}
region={"s":"x","l":"n","n":"l","x":"s","d":"gi","S":"X","L":"N","N":"L","X":"S","Gi":"D","D":"Gi"}
def text_to_telex(input_text):
    result = ""
    for char in input_text:
        if char in telex_dict:
            result += telex_dict[char]
        else:
            result += char
    return result
#ký tự lân cận và sai vị trí ký tự
def create_spelling_error(telex_text, error_rate=0.2, error_type="position"):
    telex_list = list(telex_text)
    
    if error_type == "position":
        for i in range(len(telex_list) - 1):
            if telex_list[i] != ' ' and telex_list[i + 1] != ' ':
                if random.random() < error_rate:
                    telex_list[i], telex_list[i + 1] = telex_list[i + 1], telex_list[i]
    elif error_type == "keyboard":
        adjacent_keys = {
            'a': ['q', 'w', 's', 'z'],
            'b': ['v', 'g', 'h', 'n'],
            'c': ['x', 'd', 'f', 'v'],
            'd': ['s', 'e', 'r', 'f', 'c', 'x'],
            'e': ['w', 's', 'd', 'r'],
            'f': ['d', 'r', 't', 'g', 'v', 'c'],
            'g': ['f', 't', 'y', 'h', 'b', 'v'],
            'h': ['g', 'y', 'u', 'j', 'n', 'b'],
            'i': ['u', 'h', 'j', 'k', 'o'],
            'j': ['h', 'u', 'i', 'k', 'm', 'n'],
            'k': ['j', 'i', 'o', 'l', 'm'],
            'l': ['k', 'o', 'p'],
            'm': ['n', 'j', 'k'],
            'n': ['b', 'h', 'j', 'm'],
            'o': ['i', 'k', 'l', 'p'],
            'p': ['o', 'l'],
            'q': ['a', 'w', '1', '2'],
            'r': ['e', 'd', 'f', 't', '4','5'],
            's': ['a', 'w', 'e', 'd', 'f', 'x', 'z'],
            't': ['r', 'f', 'g', 'y'],
            'u': ['y', 'h', 'j', 'i'],
            'v': ['c', 'f', 'g', 'b'],
            'w': ['q', 'a', 's', 'e', 'd'],
            'x': ['z', 's', 'd', 'c'],
            'y': ['t', 'g', 'h', 'u'],
            'z': ['a', 's', 'x']
        }
        
        for i in range(len(telex_list)):
            if telex_list[i] != ' ':
                if random.random() < error_rate:
                    original_char = telex_list[i]
                    nearby_chars = adjacent_keys.get(original_char, [])
                    if nearby_chars:
                        replacement_char = random.choice(nearby_chars)
                        telex_list[i] = replacement_char
    
    misspelled_telex = "".join(telex_list)
    return misspelled_telex
#teencode
def teencode(sentence):
    words = sentence.split()
    num_errors = int(0.5 * len(words))

    for _ in range(num_errors):
        word_index = random.randint(0, len(words) - 1)
        word = words[word_index]

        if word == "bạn":
            replace_with = random.choice(["b", "bn", "pạn"])
        elif word in acronym:
            replace_with = random.choice(acronym[word])
        else:
            replace_with = word  # Replace with the word itself, not a list
        if word == "Bạn":
            replace_with = random.choice(["B", "Bn", "Pạn"])
        elif word in acronym:
            replace_with = random.choice(acronym[word])
        else:
            replace_with = word  # Replace with the word itself, not a list
        words[word_index] = replace_with

    # Apply teen slang substitutions after all other replacements
    for key, value in teen.items():
        words = [w.replace(key, value) for w in words]

    # Check for "pn" and replace it with "bn"
    for i, word in enumerate(words):
        if word == "pn":
            words[i] = "bn"
        elif word == "p":
            words[i] = "b"
    for i, word in enumerate(words):
        if word == "Pn":
            words[i] = "Bn"
        elif word == "P":
            words[i] = "B"
    return ' '.join(words)
#lỗi sai vị trí từ trong câu tỉ lệ lỗi 0,1 
def tao_loi_doi_vi_tri_tu_trong_cau(input_text, ti_le_loi):

    cac_tu = input_text.split()
    tu_loi_doi_vi_tri = list(cac_tu)
    so_tu_loi = int(len(cac_tu) * ti_le_loi)
    cac_vi_tri = list(range(len(cac_tu)))
    vi_tri_loi = random.sample(cac_vi_tri, so_tu_loi)
    for i in vi_tri_loi:
        j = random.choice([x for x in cac_vi_tri if x != i])
        tu_loi_doi_vi_tri[i], tu_loi_doi_vi_tri[j] = tu_loi_doi_vi_tri[j], tu_loi_doi_vi_tri[i]
    cu_loi_doi_vi_tri = ' '.join(tu_loi_doi_vi_tri)

    return cu_loi_doi_vi_tri
#Lỗi lặp từ 
def tao_loi_lap_lai_tu_trong_cau(input_text):
    # Tách câu thành các từ riêng lẻ
    cac_tu = input_text.split()

    # Tạo danh sách các từ bị lặp lại
    tu_loi_lap_lai = list(cac_tu)

    # Lặp lại mỗi từ trong câu
    for i in range(len(cac_tu)):
        if random.random() < 0.2:  # Sử dụng tỷ lệ lỗi 0.2 trong ví dụ này
            tu_loi_lap_lai[i] = tu_loi_lap_lai[i] + " " + tu_loi_lap_lai[i]

    # Ghép lại các từ để tạo câu mới
    cu_loi_lap_lai = ' '.join(tu_loi_lap_lai)

    return cu_loi_lap_lai

#tạo lỗi sai thanh dấu

def tao_loi_thay_doi_thanh_trong_tu(input_text, ti_le_loi):
    # Tách câu thành các từ riêng lẻ
    cac_tu = input_text.split()

    # Tạo danh sách các từ với thanh đau bị thay đổi
    tu_loi_thay_doi_thanh = []

    for tu in cac_tu:
        tu_moi = tu
        if random.random() < ti_le_loi:
            # Kiểm tra xem nguyên âm cuối cùng có nằm ở vị trí cuối cùng trong từ không
            if tu_moi[-1] not in vowel_variants:
                for nguyen_am, bien_te in vowel_variants.items():
                    for bien_te_moi in bien_te:
                        tu_moi = tu_moi.replace(nguyen_am, bien_te_moi)
        tu_loi_thay_doi_thanh.append(tu_moi)

    # Ghép lại các từ để tạo câu mới
    cu_loi_thay_doi_thanh = ' '.join(tu_loi_thay_doi_thanh)

    return cu_loi_thay_doi_thanh

def tao_loi_dau_cau(input_text, ti_le_loi):
    # Tách câu thành các từ và dấu câu riêng lẻ
    cac_tu_va_dau_cau = input_text.split()
    
    # Tạo danh sách các từ và dấu câu với lỗi đặt dấu sai vị trí
    loi_dau_cau = []
    
    for tu_hoac_dau_cau in cac_tu_va_dau_cau:
        tu_dau_moi = tu_hoac_dau_cau
        if random.random() < ti_le_loi:
            # Kiểm tra nếu từ hoặc dấu câu là ',' hoặc '.', thì bỏ qua
            if tu_hoac_dau_cau not in [',', '.']:
                vi_tri_loi = random.randint(0, len(tu_hoac_dau_cau) - 1)
                tu_dau_moi = tu_hoac_dau_cau[:vi_tri_loi] + random.choice([',', '.']) + tu_hoac_dau_cau[vi_tri_loi:]
        loi_dau_cau.append(tu_dau_moi)
    
    # Ghép lại các từ và dấu câu để tạo câu mới
    cu_loi_dau_cau = ' '.join(loi_dau_cau)
    
    return cu_loi_dau_cau

def tao_loi_xoa_ky_tu_trong_tu(input_text, ti_le_loi):

    # Tách câu thành các từ riêng lẻ
    cac_tu = input_text.split()

    # Tạo danh sách các từ với lỗi xóa ký tự ngẫu nhiên
    tu_loi_xoa_ky_tu = []

    for tu in cac_tu:
        tu_moi = tu
        if random.random() < ti_le_loi:
            # Xác định số ký tự bị xóa dựa trên tỷ lệ lỗi và độ dài của từ
            so_ky_tu_loi = max(1, int(len(tu_moi) * ti_le_loi))
            for _ in range(so_ky_tu_loi):
                vi_tri_loi = random.randint(0, len(tu_moi) - 1)
                tu_moi = tu_moi[:vi_tri_loi] + tu_moi[vi_tri_loi + 1:]
        tu_loi_xoa_ky_tu.append(tu_moi)

    # Ghép lại các từ để tạo câu mới
    cu_loi_xoa_ky_tu = ' '.join(tu_loi_xoa_ky_tu)

    return cu_loi_xoa_ky_tu


def remove_random_spaces(input_text, error_rate=0.5):
    words = input_text.split()
    output_words = []

    remove_space = False
    for word in words:
        if remove_space:
            output_words[-1] += word
        else:
            output_words.append(word)
        remove_space = not remove_space if random.random() < error_rate else False

    return " ".join(output_words)

def region_loi(text, region, error_prob=0.5):
    # Tạo một chuỗi rỗng để lưu trữ kết quả
    result = ""

    # Duyệt qua từng ký tự trong câu đầu vào
    for char in text:
        # Kiểm tra xác suất thay thế ngẫu nhiên
        if random.random() < error_prob and char in region:
            # Nếu xác suất thỏa mãn và ký tự có trong từ điển, thay thế ký tự
            result += region[char]
        else:
            # Nếu không, giữ nguyên ký tự
            result += char

    return result

input_text = "Xin chào các bạn, tên tôi là Duy Anh, tôi sinh năm 2003"
telex_text = text_to_telex(input_text)

#tỷ lệ lỗi 0.2 (20%)
loi_region = region_loi(input_text, region)
loi_dinh_tu = remove_random_spaces(telex_text, error_rate=0.5)
xoa_ky_tu = tao_loi_xoa_ky_tu_trong_tu(input_text, 0.3)
dau_cham_phay = tao_loi_dau_cau(input_text, 0.3)
thanh_dau = tao_loi_thay_doi_thanh_trong_tu(input_text, 0.5)
cu_loi_lap_lai = tao_loi_lap_lai_tu_trong_cau(input_text)
cu_loi_doi_vi_tri = tao_loi_doi_vi_tri_tu_trong_cau(input_text, 0.2)
misspelled_telex_text_position = create_spelling_error(telex_text, error_rate=0.15, error_type="position")
misspelled_telex_text_keyboard = create_spelling_error(telex_text, error_rate=0.1, error_type="keyboard")
misspelled_telex_teencode = teencode(input_text)
print("Câu gốc:")
print(input_text)
print("Câu lỗi vị trí các từ: ")
print(cu_loi_doi_vi_tri)
print("Câu lỗi vị trí các ký tự:")
print(misspelled_telex_text_position)
print("Câu lỗi lặp từ trong câu: ")
print(cu_loi_lap_lai)
print("Câu lỗi ký tự lân cận:")
print(misspelled_telex_text_keyboard)
print("Câu lỗi teen code: ")
print(misspelled_telex_teencode)

print("Câu lỗi thanh dấu: ")
print(thanh_dau)
print("Câu lỗi vị trí dấu câu: ")
print(dau_cham_phay)
print("Câu lỗi thiếu ký tự trong từ: ")
print(xoa_ky_tu)
print("Câu lỗi dính từ: ")
print(loi_dinh_tu)
print("Câu lỗi nói ngọng địa phương: ")
print(loi_region)