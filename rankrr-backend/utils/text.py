import re
import enchant
word_dict = enchant.Dict("en_US")

def get_words(text):
    return text.split()

def remove_numerical_text(text):
    return re.sub(r'\d+', '', text)

def is_word_exist(word):
    if word_dict.check(word):
        return True
    else:
        return False
    
def get_word_suggestions(word):
    return word_dict.suggest(word)
    
def is_repeating_letters(word):
    # r'\w*(\w)\1\w*'
    # r'(\w)\1+'
    # r'.*(.).*\1.*'
    pattern = r'\b\w*(\w)\1{2,}\w*\b' #'\b\w*(\w)(\W*\1){2,}\w*\b' #r'\b\w*(\w)\1{2,}\w*\b' 
    # r'.*(.).*\1.*'
    # r'\b\w*(\w)\1{2,}\w*\b'
    if re.match(pattern, word):
        return True
    else:
        return False

# remove puncuations
def remove_puncuations(text):
    return re.sub(r'[^\w\s]','',text)

def is_valid_emphasized_word(word):
    # word = remove_numerical_text(word)
    # word = remove_puncuations(word)
    if (is_repeating_letters(word)) and (not is_word_exist(word)):
        return True
    else:
        return False
    

    
