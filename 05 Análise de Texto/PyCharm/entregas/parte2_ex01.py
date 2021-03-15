# Rodrigo Renie de Braga Pinto
# TEXT ANALYSIS(Apostila)Parte 2.docx
# Exercitando 1
# Execute o que se pede.
# Utilize o arquivo com a obra Memórias Póstumas de Bras Cubas e compare os
# stemms obtidos a partir do 6º e 7º parágrafos do texto. Utilize Porter,
# Lancaster e RSPL.

from nltk.corpus import machado
from nltk import PorterStemmer, LancasterStemmer, RSLPStemmer
from nltk.corpus import stopwords
import string

#
# Carrega os parágrafos de Memórias Póstumas de Brás Cubas
#

book_fileid = 'romance/marm05.txt'

# Carrega todos os parágrafos do livro, já tokenizados
book_paras = machado.paras(book_fileid)

# A posição 17 é o primeiro parágrafo do primeiro capítulo, portanto:
book_tokens = book_paras[17][0] + book_paras[18][0]

book_stopwords = stopwords.words('portuguese')
book_stopwords += [p for p in string.punctuation]
book_tokens = [t.lower() for t in book_tokens
               if t.lower() not in book_stopwords]

#
# Executa os Stemmers
#
porter = PorterStemmer()
stems_porter = [porter.stem(t) for t in book_tokens]

lancaster = LancasterStemmer()
stems_lancaster = [lancaster.stem(t) for t in book_tokens]

rslp = RSLPStemmer()
stems_rslp = [rslp.stem(t) for t in book_tokens]

print('{:18s} {:18s} {:18s} {}'.format('Tokens', 'Porter', 'Lancaster', 'RSLP'))
for t, p, l, r in zip(book_tokens, stems_porter, stems_lancaster, stems_rslp):
    print('{:18s} {:18s} {:18s} {}'.format(t, p, l, r))
