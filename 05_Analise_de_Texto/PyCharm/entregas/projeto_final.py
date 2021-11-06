# Rodrigo Renie de Braga Pinto
# Tarefa: Analisar textos.
# Os textos baixados podem estar relacionados com um interesse da equipe, mas
# devem ser baixadas, no mínimo, 50.000 (cinquenta mil sentenças). Para a
# análise, deve-se produzir:

# import re
import logging
# import time

import itertools

from Subtitles import Subtitles
from ProjetoFinalNLTK import ProjetoFinalNLTK
from ProjetoFinalSpacy import ProjetoFinalSpacy

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='dados/debug.log',
    filemode='w'
)


# def parse_filename(filename):
#     rex = re.search(r"[sS]([0-9]{2})[eE]([0-9]{2})", filename)
#     try:
#         season, episode = rex.group(1, 2)
#     except Exception as e:
#         logging.error('Erro ao detectar a temporada/episódio' +
#                        ' do arquivo "{}" ({})'.format(filename, e))
#         season = episode = None
#     return season, episode


# def nltk_tree_find(tree, label='PERSON'):
#     if tree.label() == label:
#         yield tree

#     for subtree in tree:
#         if type(subtree) == nltk.Tree:
#             for match in nltk_tree_find(subtree, label):
#                 yield match


def main():
    """  topn: int

    Variável que define a quantidade de itens (TOP N) que serão demonstrados
     ao longo da execução do programa, tanto na saída texto quanto nos
     gráficos. Aumentar ou diminuir este valor não altera
     significativamente o tempo de processamento, visto que o mais
     demorado é o processamentos do texto em si, não a contabilização
     do TOP N.
    """
    topn = 50

    """ s: Subtitles

    Classe que extrai o texto de todas as legendas encontradas na pasta
          passada como parâmetro. Possui duas principais funcionalidades:
        s.subtitles_text: lista onde cada item é o texto de uma das
                          legendas encontradas na pasta
        str(s): retorna um único objeto de texto contendo todas as legendas
                da lista acima concatenadas, separadas por duas linhas em
                branco (\n\n).
    """

    # s = Subtitles('dados/Breaking.Bad')
    # s = Subtitles('dados/The.Simpsons')
    s = Subtitles('dados/Friends')

    """ ps: ProjetoFinalSpacy()
        pn: ProjetoFinalNLTK()

    Armazenam o objeto principal contendo toda a lógica de cada um dos
     algoritmos de análise de texto: Spacy e NLTK. As duas classes
     possuem os seguintes atributos:

        .tokens: lista com todos os tokens detectados pelo algoritmo
        .tokens_pron_verb: lista de bigramas que são pares de pronomes
                           seguidos por um verbo
        .trigrams: lista de todos os trigramas
        .vocabulary: lista de palavras únicas

        .ner: lista contendo todos os tokens detectadas como NER
        .ner_person: lista de tokens NER especificamente da classe "PESSOAS"
        .ner_location: lista de tokens NER especificamente da classe "LOCAIS"

        .wordcloud: armazena a nuvem de palavras de todos os
                    tokens (sem os stopwords)
        .summary: armazena o texto resumido de todo o texto carregado
                  pela classe
        .summary_keywords: palavras chaves (apenas as raízes) do texto resumido

        atributos "<nome>_len": armazena o tamanho da lista retornada
                                pelo atributo <nome>
        atributos "<nome>_frequency": armazena o objeto Counter do
                                      atributo <nome> (para fazer seu TOP N)

    Cada classe pode ser criada com os seguintes parâmetros:

        Spacy(text, selectfor)
            text: texto (string) para realizar a separação em sentenças e
                  tokenização. Pode ser também uma lista de strings. Se o
                  tamanho do texto passar de nlp.max_length, é
                  obrigatório dividí-lo antes, podendo passar então como
                  uma lista de strings.

            selectfor: pode ser "accuracy", onde será selecionado um pipile
                       de treinamento mais veloz, porém mais lento. Ou
                       "efficiency", onde será selecionado um pipeline de
                       treinamento bem mais lento, porém mais preciso.

        NLTK(text)
            text: texto (string) para realizar a separação em sentenças e
                  tokenização.
    """

    ps = ProjetoFinalSpacy(text=s.subtitles_text, selectfor="accuracy")
    pn = ProjetoFinalNLTK(text=str(s))

    """
    A partir daqui, todo o código trata puramente de formatar corretamente o
      conteúdo dos atributos acima citados, para apresentar o resultado do
      NLTK e SPACY lado a lado permitindo, visualmente, analisar a diferença
      dos algoritimos.
    """

    t_fmtstr = '\n\n{:24} {:>22} {:>46}'
    d_fmtstr = '{:02} {:>40} : {:<4} {:>40} : {:<4}'

    #
    # Contagem de sentenças
    #

    print('\n\n{:25} {:>30} | {:<}'.format('Contagem', 'SPACY', 'NLTK'))
    print('{:25} {:>30} | {:<}'.format('Tokens', ps.tokens_len, pn.tokens_len))
    print('{:25} {:>30} | {:<}'.format('Sentenças', ps.sentences_len,
                                       pn.sentences_len))
    print('{:25} {:>30} | {:<}'.format('Vocabulário', len(ps.vocabulary),
                                       len(pn.vocabulary)))
    print('{:25} {:>30} | {:<}'.format('Entidades NER', ps.ner_len,
                                       pn.ner_len))
    print('{:25} {:>30} | {:<}'.format('Entidades NER Pessoas',
                                       ps.ner_person_len,
                                       pn.ner_person_len))
    print('{:25} {:>30} | {:<}'.format('Entidades NER Locais',
                                       ps.ner_location_len,
                                       pn.ner_location_len))

    #
    # Vocabulário
    #

    zipped = itertools.zip_longest([ps.vocabulary[s - 5:s] for s in range(5,
                                   len(ps.vocabulary) + 5, 5)],
                                   [pn.vocabulary[s - 5:s] for s in range(5,
                                    len(pn.vocabulary) + 5, 5)],
                                   fillvalue='-')
    print('\n\n{:20} {:>74} | {:<}'.format('Vocabulário', 'SPACY', 'NLTK'))
    for i, (spacy_v, nltk_v) in enumerate(zipped):
        print('{:04} {:>90} | {:<90}'.format(i + 1, str(', '.join(spacy_v)),
              str(', '.join(nltk_v))))

    #
    # Frequência de palavras relevantes (com gráfico de colunas ou barras)
    #

    zipped = itertools.zip_longest(ps.tokens_frequency.most_common(topn),
                                   pn.tokens_frequency.most_common(topn),
                                   fillvalue=('-', 0))
    highest_v = 0
    print(t_fmtstr.format('Top Tokens', 'SPACY', 'NLTK'))
    for i, ((spacy_v, spacy_n), (nltk_v, nltk_n)) in enumerate(zipped):
        if spacy_n > highest_v:
            highest_v = spacy_n
        if nltk_n > highest_v:
            highest_v = nltk_n
        print(d_fmtstr.format(i + 1, str(spacy_v), spacy_n, str(nltk_v),
              nltk_n))

    highest_v = ((highest_v - (highest_v % 100)) + 100)
    ps.plot(ps.tokens_frequency, title=f"TOP {topn} Tokens: SPACY",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_tokens_spacy.png")
    pn.plot(pn.tokens_frequency, title=f"TOP {topn} Tokens: NLTK",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_tokens_nltk.png")

    #
    # Trigramas relevantes (com gráfico de colunas ou barras)
    #

    zipped = itertools.zip_longest(ps.trigrams_frequency.most_common(topn),
                                   pn.trigrams_frequency.most_common(topn),
                                   fillvalue=('-', 0))
    highest_v = 0
    print(t_fmtstr.format('Top Trigramas', 'SPACY', 'NLTK'))
    for i, ((spacy_v, spacy_n), (nltk_v, nltk_n)) in enumerate(zipped):
        if spacy_n > highest_v:
            highest_v = spacy_n
        if nltk_n > highest_v:
            highest_v = nltk_n
        print(d_fmtstr.format(i + 1, str(spacy_v), spacy_n, str(nltk_v),
              nltk_n))

    highest_v = ((highest_v - (highest_v % 100)) + 100)
    ps.plot(ps.trigrams_frequency, title=f"TOP {topn} Trigramas: SPACY",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_trigrams_spacy.png")
    pn.plot(pn.trigrams_frequency, title=f"TOP {topn} Trigramas: NLTK",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_trigrams_nltk.png")

    #
    # Quais locais (entidades da classe LOCAL) são citados no texto processado?
    # Quantas vezes cada local é citado?
    #
    zipped = itertools.zip_longest(ps.ner_person_frequency.most_common(topn),
                                   pn.ner_person_frequency.most_common(topn),
                                   fillvalue=('-', 0))
    highest_v = 0
    print(t_fmtstr.format('Top Pessoas', 'SPACY', 'NLTK'))
    for i, ((spacy_v, spacy_n), (nltk_v, nltk_n)) in enumerate(zipped):
        if spacy_n > highest_v:
            highest_v = spacy_n
        if nltk_n > highest_v:
            highest_v = nltk_n
        print(d_fmtstr.format(i + 1, str(spacy_v), spacy_n, str(nltk_v),
              nltk_n))

    highest_v = ((highest_v - (highest_v % 100)) + 100)
    ps.plot(ps.ner_person_frequency, title=f"TOP {topn} Pessoas: SPACY",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_person_spacy.png")
    pn.plot(pn.ner_person_frequency, title=f"TOP {topn} Pessoas: NLTK",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_person_nltk.png")

    zipped = itertools.zip_longest(ps.ner_location_frequency.most_common(topn),
                                   pn.ner_location_frequency.most_common(topn),
                                   fillvalue=('-', 0))
    highest_v = 0
    print(t_fmtstr.format('Top Locais', 'SPACY', 'NLTK'))
    for i, ((spacy_v, spacy_n), (nltk_v, nltk_n)) in enumerate(zipped):
        if spacy_n > highest_v:
            highest_v = spacy_n
        if nltk_n > highest_v:
            highest_v = nltk_n
        print(d_fmtstr.format(i + 1, str(spacy_v), spacy_n, str(nltk_v),
              nltk_n))

    highest_v = ((highest_v - (highest_v % 100)) + 100)
    ps.plot(ps.ner_location_frequency, title=f"TOP {topn} Locais: SPACY",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_location_spacy.png")
    pn.plot(pn.ner_location_frequency, title=f"TOP {topn} Locais: NLTK",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_location_nltk.png")

    #
    # Qual é a proporção de pronomes frente aos verbos do texto?
    #

    zipped = itertools.zip_longest(ps.tokens_pron_verb_frequency.most_common(
                                   topn),
                                   pn.tokens_pron_verb_frequency.most_common(
                                   topn),
                                   fillvalue=('-', 0))
    highest_v = 0
    print(t_fmtstr.format('Top Pron-Verb', 'SPACY', 'NLTK'))
    for i, ((spacy_v, spacy_n), (nltk_v, nltk_n)) in enumerate(zipped):
        if spacy_n > highest_v:
            highest_v = spacy_n
        if nltk_n > highest_v:
            highest_v = nltk_n
        print(d_fmtstr.format(i + 1, str(spacy_v), spacy_n, str(nltk_v),
              nltk_n))

    highest_v = ((highest_v - (highest_v % 100)) + 100)
    ps.plot(ps.tokens_pron_verb_frequency,
            title=f"TOP {topn} Pron-Verb: SPACY",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_pron_verb_spacy.png")
    pn.plot(pn.tokens_pron_verb_frequency, title=f"TOP {topn} Pron-Verb: NLTK",
            limit=topn, xlimit=highest_v,
            filename="dados/g_top_pron_verb_nltk.png")

    #
    # Nuvem de palavras
    #

    ps.wordcloud.to_file('dados/g_wordcloud_spacy.png')
    pn.wordcloud.to_file('dados/g_wordcloud_nltk.png')

    #
    # Obtenha um resumo dos textos utilizados, acompanhados das palavras-chave
    #

    ps_summary = ps.summary.replace('\n', ' ').split(' ')
    pn_summary = pn.summary.replace('\n', ' ').split(' ')
    zipped = itertools.zip_longest([ps_summary[s - 10:s] for s in range(10,
                                   len(ps_summary)+10, 10)],
                                   [pn_summary[s - 10:s] for s in range(10,
                                    len(pn_summary)+10, 10)],
                                   fillvalue='-')
    print('\n\n{:20} {:>74} | {:<}'.format('Resumo', 'SPACY', 'NLTK'))
    for i, (spacy_v, nltk_v) in enumerate(zipped):
        print('{:04} {:>90} | {:<90}'.format(i + 1, str(' '.join(spacy_v)),
              str(' '.join(nltk_v))))

    ps_keywords = list(sorted(set([kw for kw in ps.summary_keywords if kw !=
                                  '\n'])))
    pn_keywords = list(sorted(set([kw for kw in pn.summary_keywords if kw !=
                                  '\n'])))
    zipped = itertools.zip_longest([ps_keywords[s - 5:s] for s in range(10,
                                   len(ps_keywords) + 10, 10)],
                                   [pn_keywords[s - 5:s] for s in range(10,
                                    len(pn_keywords) + 10, 10)],
                                   fillvalue='-')
    print('\n\n{:20} {:>74} | {:<}'.format('Resumo Tokens', 'SPACY', 'NLTK'))
    for i, (spacy_v, nltk_v) in enumerate(zipped):
        print('{:04} {:>90} | {:<90}'.format(i + 1, str(', '.join(spacy_v)),
              str(', '.join(nltk_v))))


if __name__ == '__main__':
    main()
