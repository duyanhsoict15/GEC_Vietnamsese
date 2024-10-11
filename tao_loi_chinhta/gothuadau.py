import random

def generate_spelling_error(input_text):
    error_mapping = {
        'â': ['aa', 'aw', 'ax', 'af'],
        'ă': ['aw'],
        'ê': ['ee', 'er', 'ew', 'ef'],
        'ô': ['oo', 'ow', 'ox', 'of'],
        'ơ': ['ow'],
        'ư': ['uw', 'uow'],
        'á': ['as'],
        'à': ['af'],
        'ả': ['ar'],
        'ã': ['ax'],
        'ạ': ['aj'],
        'ắ': ['as'],
        'ằ': ['af'],
        'ẳ': ['ar'],
        'ẵ': ['ax'],
        'ặ': ['aj'],
        'é': ['ee', 'er'],
        'è': ['ee', 'ef'],
        'ẻ': ['ew', 'er'],
        'ẽ': ['ex', 'ew'],
        'ẹ': ['ej', 'ef'],
        'ế': ['ee', 'ef'],
        'ề': ['ee', 'ef'],
        'ể': ['er'],
        'ễ': ['ew', 'ex'],
        'ệ': ['ej', 'ef'],
    }

    error_probability = 0.1  

    output_text = []
    for char in input_text:
        if char in error_mapping and random.random() < error_probability:
            #thay the cac loi tren error mapping
            error_variants = error_mapping[char]
            random_error = random.choice(error_variants)
            output_text.append(random_error)
        else:
            output_text.append(char)

    return ''.join(output_text)

original_text = "Để viết đúng, bạn nên sử dụng các dấu tương ứng với nguyên âm và âm ghép."
spelling_error_text = generate_spelling_error(original_text)
print(spelling_error_text)
