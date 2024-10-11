import re
import random
typo = {"ă":"aw","â":"aa","á":"as","à":"af","ả":"ar","ã":"ax","ạ":"aj","ắ":"aws","ổ":"oor","ỗ":"oox","ộ":"ooj","ơ":"ow",
"ằ":"awf","ẳ":"awr","ẵ":"awx","ặ":"awj","ó":"os","ò":"of","ỏ":"or","õ":"ox","ọ":"oj","ô":"oo","ố":"oos","ồ":"oof",
"ớ":"ows","ờ":"owf","ở":"owr","ỡ":"owx","ợ":"owj","é":"es","è":"ef","ẻ":"er","ẽ":"ex","ẹ":"ej","ê":"ee","ế":"ees","ề":"eef",
"ể":"eer","ễ":"eex","ệ":"eej","ú":"us","ù":"uf","ủ":"ur","ũ":"ux","ụ":"uj","ư":"uw","ứ":"uws","ừ":"uwf","ử":"uwr","ữ":"uwx",
"ự":"uwj","í":"is","ì":"if","ỉ":"ir","ị":"ij","ĩ":"ix","ý":"ys","ỳ":"yf","ỷ":"yr","ỵ":"yj","đ":"dd",
"Ă":"Aw","Â":"Aa","Á":"As","À":"Af","Ả":"Ar","Ã":"Ax","Ạ":"Aj","Ắ":"Aws","Ổ":"Oor","Ỗ":"Oox","Ộ":"Ooj","Ơ":"Ow",
"Ằ":"AWF","Ẳ":"Awr","Ẵ":"Awx","Ặ":"Awj","Ó":"Os","Ò":"Of","Ỏ":"Or","Õ":"Ox","Ọ":"Oj","Ô":"Oo","Ố":"Oos","Ồ":"Oof",
"Ớ":"Ows","Ờ":"Owf","Ở":"Owr","Ỡ":"Owx","Ợ":"Owj","É":"Es","È":"Ef","Ẻ":"Er","Ẽ":"Ex","Ẹ":"Ej","Ê":"Ee","Ế":"Ees","Ề":"Eef",
"Ể":"Eer","Ễ":"Eex","Ệ":"Eej","Ú":"Us","Ù":"Uf","Ủ":"Ur","Ũ":"Ux","Ụ":"Uj","Ư":"Uw","Ứ":"Uws","Ừ":"Uwf","Ử":"Uwr","Ữ":"Uwx",
"Ự":"Uwj","Í":"Is","Ì":"If","Ỉ":"Ir","Ị":"Ij","Ĩ":"Ix","Ý":"Ys","Ỳ":"Yf","Ỷ":"Yr","Ỵ":"Yj","Đ":"Dd"}

import re
import random
def create_spelling_error(sentence, typo_dict, probability):
    # Chia câu thành các từ
    words = sentence.split()
    
    # Xác định số lượng từ cần thay đổi
    num_words_to_change = int(len(words) * probability)
    
    # Chọn ngẫu nhiên các vị trí của từ cần thay đổi
    words_to_change_indices = random.sample(range(len(words)), num_words_to_change)
    
    # Thực hiện thay đổi chỉ trên các từ được chọn
    for index in words_to_change_indices:
        # Kiểm tra nếu từ hiện tại và từ sau nó không là từ cuối cùng
        if index < len(words) - 1:
            # Thay đổi từ hiện tại và từ sau nó
            words[index] = convert_word_to_telex(words[index], typo_dict)
            words[index + 1] = convert_word_to_telex(words[index + 1], typo_dict)
            
            # Xóa ký tự "space" giữa 2 từ đã được thay đổi
            words[index] += words[index + 1]
            words[index + 1] = ''
    
    # Kết hợp các từ thành câu mới
    new_sentence = ' '.join(words)
    
    return new_sentence

def convert_word_to_telex(word, typo_dict):
    # Chuyển đổi từ về dạng telex từ từ điển typo
    telex_word = ''
    for char in word:
        if char in typo_dict:
            telex_word += typo_dict[char]
        else:
            telex_word += char
    return telex_word

# Ví dụ sử dụng với xác suất thay đổi là 0.3 (30%)
sentence = "Chúc mừng năm mới, hạnh phúc và thành công!"
spelling_error = create_spelling_error(sentence, typo, probability=0.3)
print(spelling_error)
