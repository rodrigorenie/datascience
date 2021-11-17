from ProjetoFinal import ProjetoFinal

import logging
import time
import collections

import wordcloud
import spacy
from spacy.symbols import PRON, VERB
from gensim.summarization.summarizer import summarize


class ProjetoFinalSpacy(ProjetoFinal):

    def __init__(self, text, selectfor="efficiency"):
        super().__init__(text)
        self._doc = None
        self._nlp = None
        self._summary_doc = None

        if selectfor == 'efficiency':
            self._model = 'en_core_web_sm'
        elif selectfor == 'accuracy':
            self._model = 'en_core_web_trf'
        else:
            raise ValueError("'selectfor' should be 'accuracy' or 'efficiency'")

        self._bigram_pron_verb_frequency = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if isinstance(text, str) or isinstance(text, list):
            self._text = text
        else:
            raise TypeError("'text' must be string or a list of strings")

    @property
    def nlp(self):
        if self._nlp is None:
            logging.debug('[SPACY] Gerando NLP')
            self._nlp = spacy.load(self._model)

        return self._nlp

    @property
    def doc(self):
        if self._doc is None:
            logging.debug('[SPACY] Gerando DOC')
            start = time.time()

            if isinstance(self.text, str):
                self._doc = [self.nlp(self.text)]

            if isinstance(self.text, list):
                self._doc = list(self.nlp.pipe(self.text))

            logging.debug('[SPACY] Gerando DOC levou {:.2f}s'.format(time.time() - start))

        return self._doc

    @property
    def sentences(self):
        for doc in self.doc:
            for sent in doc.sents:
                yield sent

    @property
    def sentences_len(self):
        if self._sentences_len is None:
            logging.debug('[SPACY] Contabilizando sentenças')
            self._sentences_len = sum([1 for doc in self.doc for _ in doc.sents])

        return self._sentences_len

    @staticmethod
    def token_isstop(token):
        # return token.is_punct or token.is_space
        return token.is_stop or token.is_punct or token.is_space

    @property
    def tokens(self):
        for doc in self.doc:
            for token in doc:
                yield token

    @property
    def tokens_len(self):
        if self._tokens_len is None:
            logging.debug('[SPACY] Contabilizando tokens')
            self._tokens_len = sum([1 for _ in self.tokens])

        return self._tokens_len

    @property
    def tokens_frequency(self):
        if self._tokens_frequency is None:
            self._tokens_frequency = collections.Counter(
                [token.text for token in self.tokens if not self.token_isstop(token)])

        return self._tokens_frequency

    @property
    def trigrams(self):
        for token in self.tokens:
            if token.i >= 2 and not self.token_isstop(token):
                t0 = token.doc[token.i-2]
                t1 = token.doc[token.i-1]
                if not self.token_isstop(t0) and not self.token_isstop(t1):
                    yield t0, t1, token

    @property
    def trigrams_frequency(self):
        if self._trigrams_frequency is None:
            self._trigrams_frequency = collections.Counter(
                [(t1.text, t2.text, t3.text) for t1, t2, t3 in self.trigrams])

        return self._trigrams_frequency

    @property
    def vocabulary(self):
        if self._vocabulary is None:
            self._vocabulary = sorted(set(
                [token.text.lower() for token in self.tokens if not self.token_isstop(token)]))

        return self._vocabulary

    @property
    def pos(self):
        raise NotImplementedError

    @property
    def ner(self):
        for doc in self.doc:
            for ner in doc.ents:
                yield ner

    @property
    def ner_len(self):
        if self._ner_len is None:
            self._ner_len = sum([1 for _ in self.ner])

        return self._ner_len

    @property
    def ner_person(self):
        for ner in self.ner:
            if ner.label_ == 'PERSON':
                yield ner

    @property
    def ner_person_len(self):
        if self._ner_person_len is None:
            self._ner_person_len = sum([1 for _ in self.ner_person])

        return self._ner_person_len

    @property
    def ner_person_frequency(self):
        if self._ner_person_frequency is None:
            self._ner_person_frequency = collections.Counter([token.text for token in self.ner_person])

        return self._ner_person_frequency

    @property
    def ner_location(self):
        for ner in self.ner:
            if ner.label_ in ('GPE', 'LOC'):
                yield ner

    @property
    def ner_location_len(self):
        if self._ner_location_len is None:
            self._ner_location_len = sum([1 for _ in self.ner_location])

        return self._ner_location_len

    @property
    def ner_location_frequency(self):
        if self._ner_location_frequency is None:
            self._ner_location_frequency = collections.Counter([token.text for token in self.ner_location])

        return self._ner_location_frequency

    @property
    def wordcloud(self):
        if self._wordcloud is None:
            frequency = {}
            for token in self.tokens:
                if not self.token_isstop(token):
                    if token.text.lower() in frequency:
                        frequency[token.text.lower()] += 1
                    else:
                        frequency[token.text.lower()] = 1
            self._wordcloud = wordcloud.WordCloud(width=800,
                                                  height=400,
                                                  relative_scaling=1.0).generate_from_frequencies(frequency)

        return self._wordcloud

    @property
    def tokens_pron_verb(self):
        for token in self.tokens:
            if token.i >= 1:
                left = token.doc[token.i - 1]
                if left.pos == PRON and token.pos == VERB:
                    yield left, token

    @property
    def tokens_pron_verb_frequency(self):
        if self._bigram_pron_verb_frequency is None:
            self._bigram_pron_verb_frequency = collections.Counter(
                [(t1.text, t2.text) for t1, t2 in self.tokens_pron_verb])

        return self._bigram_pron_verb_frequency

    @property
    def summary(self):
        if not self._summary:
            self._summary = summarize('\n'.join([t for t in self.text]), word_count=300)

        return self._summary

    @property
    def summary_doc(self):
        if not self._summary_doc:
            self._summary_doc = self.nlp(self.summary)

        return self._summary_doc

    @property
    def summary_tokens(self):
        for token in self.summary_doc:
            yield token

    @property
    def summary_keywords(self):
        for token in self.summary_tokens:
            yield token.lemma_
