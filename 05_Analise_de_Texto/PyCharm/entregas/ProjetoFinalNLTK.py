from ProjetoFinal import ProjetoFinal

import string
import logging

import wordcloud
import nltk

from gensim.summarization.summarizer import summarize


def nltk_tree_find(tree, label='PERSON'):
    if tree.label() == label:
        yield tree

    for subtree in tree:
        if type(subtree) == nltk.Tree:
            for match in nltk_tree_find(subtree, label):
                yield match


class ProjetoFinalNLTK(ProjetoFinal):

    def __init__(self, text):
        super().__init__(text)
        self._stopwords = [punct for punct in string.punctuation]
        self._stopwords += ["''", '``', '--', '...', '... ...', "'", '-', '\n']
        self._stopwords += ["n't", "'re", "'m", "oh", "hey", "'ll", "'ve", "'s"]
        self._stopwords += nltk.corpus.stopwords.words('english')

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, str):
            self._text = text

        elif isinstance(text, list):
            self._text = '\n\n'.join(text)

        else:
            raise TypeError("'text' must be string or a list of strings")

    def token_isstop(self, token):
        return token.lower() in self._stopwords

    @property
    def sentences(self):
        if self._sentences is None:
            logging.debug('[NLTK] Gerando sentenças e tokens')
            self._sentences = []
            sentences = [sent.replace('\n', ' ') for sent in nltk.sent_tokenize(self._text)]

            for sent in sentences:
                tokens = nltk.word_tokenize(sent)
                if len(tokens) > 0:
                    self._sentences.append(tokens)

        return self._sentences

    @property
    def sentences_len(self):
        if self._sentences_len is None:
            self._sentences_len = len(self.sentences)

        return self._sentences_len

    @property
    def tokens(self):
        if self._tokens is None:
            logging.debug('[NLTK] Gerando tokens')
            self._tokens = [token for sent in self.sentences for token in sent]

        return self._tokens

    @property
    def tokens_len(self):
        if self._tokens_len is None:
            self._tokens_len = len(self.tokens)

        return self._tokens_len

    @property
    def tokens_frequency(self):
        if self._tokens_frequency is None:
            logging.debug('[NLTK] Gerando frequência dos tokens')
            self._tokens_frequency = nltk.FreqDist([t for t in self.tokens if not self.token_isstop(t)])

        return self._tokens_frequency

    @property
    def trigrams(self):
        logging.debug('[NLTK] Gerando trigramas')
        for index, token in enumerate(self.tokens):
            if not self.token_isstop(token) and index >= 2:
                t0 = self.tokens[index - 2]
                t1 = self.tokens[index - 1]
                if not self.token_isstop(t0) and not self.token_isstop(t1):
                    yield t0, t1, token

    @property
    def trigrams_frequency(self):
        if self._trigrams_frequency is None:
            logging.debug('[NLTK] Gerando frequência dos trigramas')
            self._trigrams_frequency = nltk.FreqDist([t for t in self.trigrams])

        return self._trigrams_frequency

    @property
    def vocabulary(self):
        if self._vocabulary is None:
            logging.debug('[NLTK] Gerando vocabulário')
            self._vocabulary = sorted(set([t.lower() for t in self.tokens if not self.token_isstop(t)]))

        return self._vocabulary

    @property
    def pos(self):
        if self._pos is None:
            logging.debug('[NLTK] Gerando POS')
            self._pos = [nltk.pos_tag(sent) for sent in self.sentences]

        return self._pos

    @property
    def ner(self):
        if self._ner is None:
            logging.debug('[NLTK] Gerando NER')
            self._ner = [nltk.ne_chunk(sent) for sent in self.pos]

        return self._ner

    @property
    def ner_len(self):
        if self._ner_len is None:
            self._ner_len = len(self.ner)

        return self._ner_len

    @property
    def ner_person(self):
        for ner in self.ner:
            for person in nltk_tree_find(ner, 'PERSON'):
                yield person

    @property
    def ner_person_len(self):
        if self._ner_person_len is None:
            self._ner_person_len = sum([1 for _ in self.ner_person])

        return self._ner_person_len

    @property
    def ner_person_frequency(self):
        if self._ner_person_frequency is None:
            logging.debug('[NLTK] Gerando frequência de PERSON')
            textlist = [' '.join([text for text, _ in token.leaves()]) for token in self.ner_person]
            self._ner_person_frequency = nltk.FreqDist(textlist)

        return self._ner_person_frequency

    @property
    def ner_location(self):
        for ner in self.ner:
            for gpe in nltk_tree_find(ner, 'GPE'):
                yield gpe
            for location in nltk_tree_find(ner, 'LOCATION'):
                yield location

    @property
    def ner_location_len(self):
        if self._ner_location_len is None:
            self._ner_location_len = sum([1 for _ in self.ner_location])

        return self._ner_location_len

    @property
    def ner_location_frequency(self):
        if self._ner_location_frequency is None:
            logging.debug('[NLTK] Gerando frequência de GPE')
            textlist = [' '.join([text for text, _ in token.leaves()]) for token in self.ner_location]
            self._ner_location_frequency = nltk.FreqDist(textlist)

        return self._ner_location_frequency

    @property
    def wordcloud(self):
        if self._wordcloud is None:
            logging.debug('[NLTK] Gerando Wordcloud')
            frequency = {}
            for token in self.tokens:
                if not self.token_isstop(token):
                    if token.lower() in frequency:
                        frequency[token.lower()] += 1
                    else:
                        frequency[token.lower()] = 1
            self._wordcloud = wordcloud.WordCloud(width=800, height=400,
                                                  relative_scaling=1.0).generate_from_frequencies(frequency)

        return self._wordcloud

    @property
    def tokens_pron_verb(self):
        check_next = False
        previous_token = None

        for pos_sent in self.pos:
            for token, tag in pos_sent:
                if check_next:
                    if tag in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'):
                        yield previous_token, token

                    check_next = False
                    previous_token = None

                if tag in ('PRP', 'PRP$'):
                    previous_token = token
                    check_next = True

    @property
    def tokens_pron_verb_frequency(self):
        if self._tokens_pron_verb_frequency is None:
            logging.debug('[NLTK] Gerando frequência de PRON-VERB')
            textlist = [t for t in self.tokens_pron_verb]
            self._tokens_pron_verb_frequency = nltk.FreqDist(textlist)

        return self._tokens_pron_verb_frequency

    @property
    def summary(self):
        if not self._summary:
            self._summary = summarize(self.text, word_count=300)

        return self._summary

    @property
    def summary_tokens(self):
        if self._summary_tokens is None:
            logging.debug('[NLTK] Gerando sentenças e tokens do resumo')
            self._summary_tokens = []
            sentences = [sent.replace('\n', ' ') for sent in nltk.sent_tokenize(self.summary)]

            for sent in sentences:
                tokens = nltk.word_tokenize(sent)
                if len(tokens) > 0:
                    self._summary_tokens.append(tokens)

        return self._summary_tokens

    @property
    def summary_keywords(self):
        stemmer = nltk.RSLPStemmer()

        for sent in self.summary_tokens:
            for token in sent:
                yield stemmer.stem(token)
