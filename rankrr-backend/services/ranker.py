import pandas as pd
import numpy as np
import services.sentiment_analyzer as sentiment_analyzer
import services.text_analyzer as text_analyzer
import utils.emoji as emoji_util
import utils.text as text_util
import utils.files as file_util

emoji_sia = sentiment_analyzer.get_emoji_sia()
text_sia = sentiment_analyzer.get_text_sia()

file_util.get_demo_data_file_path()

demo_df = pd.read_csv(file_util.get_demo_data_file_path())


def rank_custom_csv(file_path, product_id_col, review_text_col, max_products_amount, consider_emoji, consider_emph_text):
    df = pd.read_csv(file_path,  on_bad_lines='skip')
    return get_ranked_products(df, product_id_col, review_text_col, max_products_amount, consider_emoji, consider_emph_text)


def custom_csv_reviews_sentiments(file_path, product_id, product_id_col, review_text_col, max_products_amount):
    df = pd.read_csv(file_path)
    return get_reviews_sentiments_by_product_id(df, product_id, product_id_col, review_text_col, max_products_amount)


def get_unique_products_and_counts(df: pd.DataFrame, product_id_col, max_products_amount):
    counts_dict = df[product_id_col].value_counts().to_dict()
    uniques_and_counts = dict(sorted(counts_dict.items(), key=lambda x: x[1], reverse=True))
    return dict(list(uniques_and_counts.items())[:max_products_amount])


def get_top_records(df: pd.DataFrame, product_id, product_id_col, max_count):
    return df[df[product_id_col] == product_id].head(max_count)


def get_ranked_products( df: pd.DataFrame, product_id_col, review_text_col, max_products_amount, consider_emoji = False, consider_emph_text = False):
    
    sentiments = {}

    if consider_emoji:
        sia = emoji_sia
    else:
        sia = text_sia

    uniques_and_counts = get_unique_products_and_counts(df, product_id_col, max_products_amount)
    max_reviews_amount = min(uniques_and_counts.values())

    for product_id in uniques_and_counts.keys():

        records = get_top_records(df, product_id, product_id_col, max_reviews_amount)
        
        for i, record in records.iterrows():
            
            record[review_text_col] = record[review_text_col].lower()
            
            if consider_emoji:
                emojis = emoji_util.extract_emojis(record[review_text_col])
            
            record[review_text_col] = emoji_util.remove_emojis(record[review_text_col])
            
            if consider_emph_text:
                record[review_text_col] = text_analyzer.get_ml_preprocessed_text(record[review_text_col])

            record[review_text_col] = sentiment_analyzer.preprocess_text(record[review_text_col])
            
            if consider_emoji:
                record[review_text_col] = record[review_text_col] + " " + " ".join(emojis)

            if product_id in sentiments:
                sentiments[product_id].append(sia.polarity_scores(record[review_text_col])['pos'])
            else:
                sentiments[product_id] = [sia.polarity_scores(record[review_text_col])['pos']]

    for key, value in sentiments.items():
        sentiments[key] = np.mean(value)

    sorted_data = sorted(sentiments.items(), key=lambda x: x[1], reverse=True)
    return [{'product_id': key, 'sentiment_score': val, 'rank': rank} for rank, (key, val) in enumerate(sorted_data, start=1)]


def get_reviews_sentiments_by_product_id(df: pd.DataFrame, product_id, product_id_col, review_text_col, max_products_amount):
    
    uniques_and_counts = get_unique_products_and_counts(df, product_id_col, max_products_amount)
    max_reviews_amount = min(uniques_and_counts.values())

    df = get_top_records(df, product_id, product_id_col, max_reviews_amount)

    sentiments = []

    reviews = df[df[product_id_col] == product_id][review_text_col].tolist()
   
    for i, review in enumerate(reviews):
        
        review = review.lower()
        
        emojis = emoji_util.extract_emojis(review)
        review = emoji_util.remove_emojis(review)
        
        review_sentiments = { 'review': reviews[i], 'sentiment_without_extra': text_sia.polarity_scores(review)}

        words = text_util.get_words(review)
        for index, word in enumerate(words):
            if text_util.is_valid_emphasized_word(word):
                words[index] = text_analyzer.predict_actual_word(word)
        review = " ".join(words)

        review = sentiment_analyzer.preprocess_text(review)
        
        review = review + " " + " ".join(emojis)
    
        review_sentiments['sentiment_with_extra'] = emoji_sia.polarity_scores(review)
        sentiments.append(review_sentiments)
  
    return sentiments


def demo(product_id_col, review_text_col, max_products_amount, consider_emoji, consider_emphasized_text):
    return get_ranked_products(demo_df, product_id_col, review_text_col, max_products_amount, consider_emoji, consider_emphasized_text)


def demo_reviews_sentiments(product_id, product_id_col, review_text_col, max_products_amount):
    return get_reviews_sentiments_by_product_id(demo_df, product_id, product_id_col, review_text_col, max_products_amount)






  
    # if consider_emoji, clean text with ml model
    # if consider_emph_words:
    #     for i, review in enumerate(reviews):
    #         words = text_util.get_words(review)
    #         for index, word in enumerate(words):
    #             if text_util.is_valid_emphasized_word(word):
    #                 print("--------------------")
    #                 print(word)
    #                 words[index] = text_analyzer.predict_actual_word(word)
    #         reviews[i] = " ".join(words)

    # sentiments = []
    # for review in reviews:
    #     sentiments.append({'review': review, 'sentiment_with_extra': emoji_sia.polarity_scores(review), 'sentiment_without_extra': text_sia.polarity_scores(review), })
   




        # sentiments[product_id] = np.mean([sia.polarity_scores(record[review_text_col])['pos'] for index, record in records.iterrows()])
    
    # for index, row in df.iterrows():
    #     if row[product_id_col] in uniques_and_counts.keys():

    #         row[review_text_col] = row[review_text_col].lower()

    #         if consider_emoji:
    #             emojis = emoji_util.extract_emojis(row[review_text_col])
            
    #         row[review_text_col] = emoji_util.remove_emojis(row[review_text_col])

    #         if consider_emph_text:
    #             row[review_text_col] = text_analyzer.get_ml_preprocessed_text(row[review_text_col])
                      
    #         if consider_emoji:
    #             row[review_text_col] = row[review_text_col] + " " + " ".join(emojis)

    #         if row[product_id_col] in sentiments and len(sentiments[row[product_id_col]]['sentiment']) < max_reviews_amount:
    #             if 'sentiment' in sentiments[row[product_id_col]]:
    #                 sentiments[row[product_id_col]]['sentiment'].append(sia.polarity_scores(row[review_text_col])['pos'])
    #             else:
    #                 sentiments[row[product_id_col]]['sentiment'] = [sia.polarity_scores(row[review_text_col])['pos']]
    #         else:
    #             sentiments[row[product_id_col]] = {'sentiment' : [sia.polarity_scores(row[review_text_col])['pos']]}

    # for key, value in sentiments.items():
    #     sentiments[key] = np.mean(value['sentiment'])
    
    # sorted_data = sorted(sentiments.items(), key=lambda x: x[1], reverse=True)
    # return [{'product_id': key, 'sentiment_score': val, 'rank': rank} for rank, (key, val) in enumerate(sorted_data, start=1)]
