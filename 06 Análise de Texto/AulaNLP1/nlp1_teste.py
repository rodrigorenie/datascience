import nltk
from nltk.corpus import CategorizedPlaintextCorpusReader
from nltk.corpus import brown

# Abrir os documentos dentro do caminho específico
# Argumentos
# 1. Caminho absoluto para os documentos
# 2. tipo / extensão dos documentos (*.txt)
# 3. indicativo das pastas que formarão as categorias
# todos os argumentos são expressões regulares

leitor = CategorizedPlaintextCorpusReader(
    '../Dados/mix20_rand700_tokens_cleaned/tokens/',
    '.*.txt',
    cat_pattern=r'(\w+)/*')

# Verificar o que foi carregado
print(leitor.categories())
print(leitor.fileids())

# Separar o corpus de acordo com as categorias
posFiles = leitor.fileids(categories='pos')
negFiles = leitor.fileids(categories='neg')
print('Arquivos pos:', posFiles)
print('Arquivos neg:', negFiles)

# Carregar os primeiros arquivos das categorias
arqP = posFiles[0]
arqN = negFiles[1]

print("ArqP: ", arqP)
print("ArqN: ", arqN)

# Imprimir as sentenças dos arquivos
print('Palavras nos arquivos selecionados')
for p in leitor.words(arqP):
    print(p + ' ', end='')

print('---')

for p in leitor.words(arqN):
    print(p + ' ', end='')

#
#
#
#

print(brown.categories())

# Selecionar três categorias livremente
categorias = ['fiction', 'humor', 'romance']

# montar uma lista de palavras para a contagem.
# neste caso, serão palavras da lingua inglesa que possuam 'wh'
wh_words = ['what', 'whitch', 'how', 'why', 'when', 'where', 'who']

# percorre a lista de categorias
for cat in categorias:
    print('\nAnalisando palavras na categoria {}'.format(cat))
    cat_texto = brown.words(categories=cat)
    print(cat_texto)
    # o objeto fdist tem a frequencia de cada palavra dentro da lista cat_texto
    fdist = nltk.FreqDist(cat_texto)

    # agora, basta percorrer o objeto fdist e imprimir o resultado relativo a
    # cada palavra na lista wh_words
    total = fdist.N()
    for word in wh_words:
        print('Frequência da palavra {:>10s} : {:3} (total {})'.format(
            word, fdist[word], total))
