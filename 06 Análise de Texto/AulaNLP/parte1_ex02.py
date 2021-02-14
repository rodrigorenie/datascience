# TEXT ANALYSIS(Apostila)Parte 1.docx
# Exercitando 2
# Execute o que se pede.
# Utilize o arquivo Noticia_1 disponível na pasta de dados da turma e liste os
# 50 bigramas e trigramas mais frequentes obtidos do texto.

import docx
import nltk
from nltk import ngrams

docpath = '../Dados/Noticia_1.docx'
doc = docx.Document(docpath)

words = [w for p in doc.paragraphs for w in p.text.split()]

fb2 = nltk.FreqDist(ngrams(words, 2))
fb3 = nltk.FreqDist(ngrams(words, 3))

print('{:>30s} : {:4} {:>40s} : {:4}'.format(
    'Bigrama', 'Freq', 'Trigrama', 'Freq'))

for ((bw, bf), (tw, tf)) in zip(fb2.most_common(20), fb3.most_common(20)):
    print('{:>30s} : {:<4} {:>40s} : {:<4}'.format(str(bw), bf, str(tw), tf))