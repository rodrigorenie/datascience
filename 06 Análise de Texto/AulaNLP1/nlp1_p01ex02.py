import docx
import nltk
from nltk import ngrams

docpath = '../Dados/Noticia_1.docx'
doc = docx.Document(docpath)

words = [w for p in doc.paragraphs for w in p.text.split()]

fb2 = nltk.FreqDist(ngrams(words, 2))
fb3 = nltk.FreqDist(ngrams(words, 3))

for b, f in fb2.most_common(20):
    print('Bigrama: {:>40s} - Freq: {:02}'.format(str(b), f))

for b, f in fb3.most_common(20):
    print('Trigrama: {:>40s} - Freq: {:02}'.format(str(b), f))
