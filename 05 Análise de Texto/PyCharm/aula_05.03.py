import nltk
import string
from nltk.corpus import stopwords
import spacy



from gensim.summarization.summarizer import summarize
# from gensim.summarization import keywords
import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def preprocess(sentence, lang='portuguese', filter=True):
    sentence_raw = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    sentence = "".join([i for i in sentence_raw if i not in string.punctuation])
    tokens = tokenizer.tokenize(sentence)
    if filter:
        filtered_words = [w for w in tokens if w not in stopwords.words(lang)]
        return " ".join(filtered_words)
    else:
        return " ".join(tokens)

text = "Apple adquire Zoom na China na quinta-feira 6 de maio de 2020. "
"Essa notícia fez as ações da Apple e da Google subirem 5% nos Estados Unidos."

text = "Pushing the boundaries of math requires great minds to pose "
"fascinating problems: what if a machine could do it?"

# spacy_nlp = spacy.load("pt_core_news_sm")
spacy_nlp = spacy.load("en_core_web_sm")

text_nlp_spacy = spacy_nlp(text)
text_nlp_nltk = nltk.pos_tag(nltk.word_tokenize(text))

print('{:20} {:20} {:20} {:20}'
      .format('Palavra NLTK', 'Palavra Spacy', 'Token NLTK', 'Token Spacy'))

for t_nltk, t_spacy in zip(text_nlp_nltk, text_nlp_spacy):
    print('{:20} {:20} {:20} {:20}'
          .format(t_nltk[0], t_spacy.text, t_nltk[1], t_spacy.pos_))







# Get wiki content.
wikipedia.set_lang('pt')
wikicontent = wikipedia.page('Usina Hidrelétrica de Itaipu').content
wikisummary = summarize(wikicontent, word_count=250)  # ratio=0.05)

# palavras chave
wikitokens = nltk.sent_tokenize(wikisummary)
wikitokens = [nltk.word_tokenize(s) for s in wikitokens]
print(wikitokens)

exit(0)

stemmer = nltk.RSLPStemmer()
stems_rslp = [rslp.stem(t) for t in book_tokens]




stem_text = [rs.stem(p) for p in tokens]
key_words = keywords(" ".join(stem_text), ratio=0.05, pos_filter=('NN'),
                     words=5)
print(key_words)
wordcloud = WordCloud(width = 800, height = 400,  relative_scaling = 1.0,   stopwords = {'to', 'of', 'us'}).generate(text)
plt.axis('off')
