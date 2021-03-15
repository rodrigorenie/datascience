import string
import nltk
from nltk.corpus import stopwords


def tokenizer(text,
              lang='english',
              remove_stopwords=False,
              remove_punctuations=False):
    sw = stopwords.words(lang)
    for c in string.punctuation:
        sw += [c]

    text = nltk.sent_tokenize(text)
    text = [nltk.word_tokenize(s) for s in text]
    return text

def generate_wordcloud(text):
    pass