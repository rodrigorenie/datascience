# TEXT ANALYSIS(Apostila)Parte 1.docx
# Exercitando 1
# Execute o que se pede.
# Imprima as palavras dos documentos neg/cv002_tok-3321.txt e
# pos/cv003_tok-8338.txt

from nltk.corpus import CategorizedPlaintextCorpusReader

corpus_reader = CategorizedPlaintextCorpusReader(
    '../Dados/mix20_rand700_tokens_cleaned/tokens/',
    '.*.txt', cat_pattern=r'(\w+)/*')

words = {
    'neg/cv002_tok-3321.txt': [],
    'pos/cv003_tok-8338.txt': []
}

# Verificar o que foi carregado
# print(corpus_reader.categories())
# print(corpus_reader.fileids())
# print(corpus_reader.words(fileids=['neg/cv002_tok-3321.txt']))

for file in words:
    words[file] = corpus_reader.words(fileids=file)
    print('Palavras no arquivo {}: {}'.format(file, words[file]))
