from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer as Text_SIA
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as Emoji_SIA
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

import utils.emoji as emoji_util
import utils.text as text_util

text_sia = Text_SIA()
emoji_sia = Emoji_SIA()

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    
    text = text.lower()

    # remove puncuations
    # text = re.sub(r'[^\w\s]', '', text)

    tokens = word_tokenize(text)

    tokens = [token for token in tokens if token not in stop_words]
    
    # tokens = [lemmatizer.lemmatize(token) for token in tokens]

    preprocessed_text = " ".join(tokens)

    return preprocessed_text


def get_sentiment_scores(text, consider_emoji = True):
    if consider_emoji:
        return emoji_sia.polarity_scores(preprocess_text(text))
    else:
        return text_sia.polarity_scores(preprocess_text(text))


def get_emoji_sia():
    return emoji_sia


def get_text_sia():
    return text_sia


