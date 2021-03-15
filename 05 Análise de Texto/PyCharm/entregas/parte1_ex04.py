# Rodrigo Renie de Braga Pinto
# TEXT ANALYSIS(Apostila)Parte 1.docx
# Exercitando 4
# Execute o que se pede.

import nltk
import string
from nltk import ngrams
from nltk import tokenize
from nltk.corpus import machado
from nltk.corpus import stopwords

# Execute print(machado.readme()) para conhecer melhor o corpus
print(machado.readme())

# Utilizando o corpus machado, elabore um programa que atenda aos requisitos:

# a. Quais são as categorias presentes no corpus?
print('Categorias: {}'.format(machado.categories()))

# b. Quais são os documentos dentro desse corpus?
print('Documentos: {}'.format(machado.fileids()))

# c. Imprima o conteúdo do arquivo do documento que contem a obra
#    Memórias Postumas de Braz Cubas
book_fileid = 'romance/marm05.txt'
print(machado.raw(book_fileid))

# d. Analise a frequência das palavras [‘olhos’,’estado’] em
#    Memórias Postumas de Bras Cubas
book_text = machado.raw(book_fileid)
book_tokens = tokenize.word_tokenize(book_text)
book_freq = nltk.FreqDist(book_tokens)

for w in ['olhos', 'estado']:
    print('Frequência da palavra {:>8s} : {:03}'.format(w, book_freq[w]))

# e. Quantas palavras há no texto? Use len(texto)
print('Total de palavras: {}'.format(len(book_text)))

# f. Quantas palavras distintas há na obra?
print('Total de palavras distintas: {}'.format(len(book_freq)))

# g. Qual é o vocabulário (palavras) presentes na obra?
print('Vocabulário: {}'.format(book_freq.keys()))

# h. Quais são os 15 termos mais repetidos no texto de Machado de Assis?
print('\n{:25s} {}'.format('Top 15', 'Frequência'))
for w, f in book_freq.most_common(15):
    print('{:25s} {:03}'.format(w, f))

# i. Tabular a frequência de palavras
print('\n')
book_freq.tabulate(15, cumulative=False)

# j. Gerar um gráfico com os 15 termos mais repetidos
book_freq.plot(15, title='Top 15 words', cumulative=False)

# k. Remova os termos indesejados  e repita as questões 'h' a 'j'
book_stopwords = stopwords.words('portuguese')
book_stopwords += ['\x97', '...', 'd.']
book_stopwords += [p for p in string.punctuation]
book_tokens = [t.lower() for t in book_tokens
               if t.lower() not in book_stopwords]
book_freq = nltk.FreqDist(book_tokens)

print('\n{:25s} {}'.format('Top 15', 'Frequência'))
for w, f in book_freq.most_common(15):
    print('{:25s} {:03}'.format(w, f))

print('\n')
book_freq.tabulate(15, cumulative=False)

book_freq.plot(15, title='Top 15 words', cumulative=False)

# l. Obter a lista de todos os trigramas do texto
for trigram in ngrams(book_tokens, 3):
    print('{:35s}'.format(str(trigram)))

# m. Obter a lista dos 15 bigramas que contenham a palavra 'olhos'
olhos_bigram = [ng for ng in ngrams(book_tokens, 2) if 'olhos' in ng]
olhos_freq = nltk.FreqDist(olhos_bigram)
print('\n{:30s} {}'.format('Top 15 Olhos', 'Frequência'))
for b, f in olhos_freq.most_common(15):
    print('{:30s} {:03}'.format(str(b), f))

# n. Gerar o gráfico dos bigramas com a palavra 'olhos'
olhos_freq.plot(15, cumulative=True)
