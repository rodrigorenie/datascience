from gensim.summarization.summarizer import summarize
# from gensim.summarization import keywords
import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

import dsitaipu.utils


# Get wiki content.
wikipedia.set_lang('pt')
wikicontent = wikipedia.page('Usina Hidrelétrica de Itaipu').content
wikisummary = summarize(wikicontent, word_count=250)  # ratio=0.05)

# palavras chave
wikitokens = dsitaipu.utils.tokenizer(wikisummary)
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
