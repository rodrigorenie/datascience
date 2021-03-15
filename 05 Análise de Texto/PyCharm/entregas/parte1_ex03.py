# Rodrigo Renie de Braga Pinto
# TEXT ANALYSIS(Apostila)Parte 1.docx
# Exercitando 3
# Execute o que se pede.
# Analise a frequência das palavras ['the', 'that'] no arquivo singles.txt e,
# depois, no arquivo pirates.txt.
# Inclua a geração do gráfico de frequência.
# Gere a lista dos 15 bigramas mais frequentes do texto.
# Gere a lista dos 20 quadrigramas gramas mais frequentes que possuam a
# palavra 'life'

import nltk
from nltk import ngrams
from nltk import tokenize
from nltk.corpus import webtext
from nltk.corpus import stopwords

data = {
    'singles.txt': {
        'tokens': [],
        'freq_tokens': None,
        'freq_tokens_top15': [],
        'freq_bigrams': None,
        'freq_bigrams_top15': [],
        'freq_quadrigrams_life': []
    },
    'pirates.txt': {
        'tokens': [],
        'freq_tokens': None,
        'freq_tokens_top15': [],
        'freq_bigrams': None,
        'freq_bigrams_top15': [],
        'freq_quadrigrams_life': []
    }
}

# Gera os stopwords e inclui palavras personalizadas
stopwords = stopwords.words('english') + [
    "[", "]", ".",  ",",  "?", "*",   ":",   "...", "!",   "'", "'s",
    "#", "(", ")",  "'m", "-", "'ve", "ft.", "n't", "y.o", "&", "..",
    "n/s", "s/d", "n/d", "s/s", "s/e", "''"
]

for file in data:
    text = webtext.raw(file)

    # Gera e filtra os tokens de cada arquivo
    data[file]['tokens'] = tokenize.word_tokenize(text)
    data[file]['tokens'] = [t.lower() for t in data[file]['tokens']
                            if t.lower() not in stopwords]

    # Gera os dados de frequência dos tokens
    data[file]['freq_tokens'] = nltk.FreqDist(data[file]['tokens'])

    # Gera os dados dos 15 tokens mais frequentes
    top15 = data[file]['freq_tokens'].most_common(15)
    data[file]['freq_tokens_top15'] = top15

    # Gera os dados de frequência dos bigramas
    bigram = ngrams(data[file]['tokens'], 2)
    data[file]['freq_bigrams'] = nltk.FreqDist(bigram)

    # Gera os dados dos 15 bigramas mais frequentes
    top15 = data[file]['freq_bigrams'].most_common(15)
    data[file]['freq_bigrams_top15'] = top15

    # Gera os dados de frequência dos quadrigramas com palavra "life"
    quadrigram = [ng for ng in ngrams(data[file]['tokens'], 4) if 'life' in ng]
    data[file]['freq_quadrigrams_life'] = nltk.FreqDist(quadrigram)

    # Imprime frequência das palavras 'the' e 'that'
    print('\n{:20s} {:35s} {}'.format('Arquivo', 'Token', 'Frequência'))
    for word in ['the', 'that']:
        freq = data[file]['freq_tokens'][word]
        print('{:20s} {:35s} {:03}'.format(file, word, freq))

    # Imprime Top 15 Tokens
    print('\n{:20s} {:35s} {}'.format('Arquivo', 'Top 15 Tokens', 'Frequência'))
    for token, freq in data[file]['freq_tokens_top15']:
        print('{:20s} {:35s} {:03}'.format(file, token, freq))

    # Imprime Top 15 Bigramas
    print('\n{:20s} {:35s} {}'.format(
        'Arquivo', 'Top 15 Bigrama', 'Frequência'))
    for bigram, freq in data[file]['freq_bigrams_top15']:
        print('{:20s} {:35s} {:03}'.format(file, str(bigram), freq))

    # Imprime Top 20 Quadrigramas com palavra "life"
    print('\n{:20s} {:50s} {}'.format(
        'Arquivo', 'Top 20 Quadrigrama', 'Frequência'))
    top20 = data[file]['freq_quadrigrams_life'].most_common(20)
    for quadrigram, freq in top20:
        print('{:20s} {:50s} {:03}'.format(file, str(quadrigram), freq))

data['singles.txt']['freq_tokens'].plot(cumulative=False)
data['pirates.txt']['freq_tokens'].plot(cumulative=True)
