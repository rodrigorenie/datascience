# Rodrigo Renie de Braga Pinto
# Tarefa: Analisar textos.
# Os textos baixados podem estar relacionados com um interesse da equipe, mas
# devem ser baixadas, no mínimo, 50.000 (cinquenta mil sentenças). Para a
# análise, deve-se produzir:

import nltk
import wordcloud
import os
import logging
import re
import string

from pysubparser import parser
from pysubparser.cleaners import brackets, formatting
from nltk.corpus import stopwords

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')


class TheSimpsonsSubtitles:

    def __init__(self, rootdir, encoding='latin-1'):
        self.subtitle = []

        for dirpath, dirnames, filelist in os.walk(rootdir):
            logging.debug('Escaneando pasta {}'.format(dirpath))
            filelist.sort()
            dirnames.sort()

            for filename in filelist:
                logging.debug('Carregando legenda {}'.format(filename))
                filename = os.path.join(dirpath, filename)
                season, episode = self.parse_filename(filename)

                text = parser.parse(filename, encoding=encoding)
                text = brackets.clean(text)
                text = formatting.clean(text)
                text = ' '.join([lines.text for lines in text])

                if season and episode:
                    self.subtitle.append((season, episode, text))

    def __iter__(self):
        return iter(self._subtitle)

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        if not hasattr(self, 'subtitle'):
            self._subtitle = subtitle

    def parse_filename(self, filename):
        rex = re.search(r"[sS]([0-9]{2})[eE]([0-9]{2})", filename)
        try:
            season, episode = rex.group(1, 2)
        except Exception as e:
            logging.error(
                'Erro ao detectar a temporada/episódio do '
                'arquivo "{}" ({})'.format(filename, e)
            )
            season = episode = None
        return season, episode


# Contagem de sentenças
# print('\n** Número de sentenças: {}'.format(len(sentences)))

# Vocabulário
# Frequência de palavras relevantes (com gráfico de colunas ou barras)
# Trigramas relevantes (com gráfico de colunas ou barras)
# Quais locais (entidades da classe LOCAL) são citados no texto processado?
# Quantas vezes cada local é  citado?
# Qual é a proporção de pronomes frente aos verbos do texto?
# Nuvem de palavras
# Obtenha um resumo dos textos utilizados, acompanhados das palavras-chave


if __name__ == '__main__':
    sw = [p for p in string.punctuation]
    sw += stopwords.words('english')
    print(sw)

    s = TheSimpsonsSubtitles('dados/subtitles')
    data = '\n'.join([text for _, _, text in s])
    data = nltk.sent_tokenize(data)
    data = [nltk.word_tokenize(s) for s in data]
    data = [[w for w in s if w.lower() not in sw] for s in data]
    #print(data)