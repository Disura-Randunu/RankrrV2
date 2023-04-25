import pickle
import re
import utils.text as text_util

with open('../model_v9.pkl', 'rb') as file:
    model = pickle.load(file)


def predict_actual_word(emphasized_word):
    return model.predict([emphasized_word])[0]


def get_ml_preprocessed_text(text):
    words = text_util.get_words(text)
    for index, word in enumerate(words):
        if text_util.is_valid_emphasized_word(word):
            words[index] = predict_actual_word(word)
    return " ".join(words)


def get_advanced_preprocessed_text(text):
    words = text_util.get_words(text)
    pattern = r'(\w)\1+'
    for index, word in enumerate(words):
        if text_util.is_valid_emphasized_word(word):  
            corrected = re.sub(pattern, r'\1\1', word)
            if(text_util.is_word_exist(corrected)):
                words[index] = corrected
            else:
                suggestions = text_util.get_word_suggestions(corrected)
                words[index] = suggestions[0] if len(suggestions) > 0 else corrected
    
    return " ".join(words)


            
def get_basic_preprocessed_text(text):
    words = text_util.get_words(text)
    pattern = r'(\w)\1+'
    for index, word in enumerate(words):
        if text_util.is_valid_emphasized_word(word):  
            corrected = re.sub(pattern, r'\1\1', word)
            if(text_util.is_word_exist(corrected)):
                words[index] = corrected
            else:
                words[index] = re.sub(pattern, r'\1', word)
    
    return  " ".join(words)

   

    
    # if retain_emojis:
    #     emojis = emoji_util.extract_emojis(text)
    #     text = emoji_util.remove_emojis(text)
    # else:
    #     text = emoji_util.remove_emojis(text)
    
    # if clean_emphasized_words:
    #     words = text_util.get_words(text)

    #     for index, word in enumerate(words):
    #         if is_word(word):
    #             print(predict_actual_word(word))
    #             words[index] = predict_actual_word(word)
        
    #     return " ".join(words)
    #     # text = re.sub(r'(\w)\1{2,}', r'\1', text)


        # features = vectorizer.transform([emphasized_word])
    # return model.predict(features)[0]