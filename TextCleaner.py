import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class TextCleaner:
    @staticmethod
    def remove_stopwords(text):
        stop_words = set(stopwords.words('english'))
        return ' '.join([word for word in text.split() if word.lower() not in stop_words])

    @staticmethod
    def to_lowercase(text):
        return text.lower()

    @staticmethod
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    @staticmethod
    def lemmatize(text):
        lemmatizer = WordNetLemmatizer()
        return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
