import matplotlib.pyplot


class ProjetoFinal():

    def __init__(self, text):
        self.text = text

        self._sentences = None
        self._sentences_len = None

        self._tokens = None
        self._tokens_len = None
        self._tokens_frequency = None
        self._tokens_pron_verb_frequency = None

        self._trigrams_frequency = None
        self._vocabulary = None

        self._pos = None
        self._ner = None
        self._ner_len = None
        self._ner_person_len = None
        self._ner_person_frequency = None
        self._ner_location_len = None
        self._ner_location_frequency = None

        self._wordcloud = None
        self._summary = None
        self._summary_tokens = None

    @staticmethod
    def plot(counter, limit=None, xlimit=None, title=None, filename=None):
        matplotlib.pyplot.rcParams['figure.figsize'] = (16.0, 10.0)
        matplotlib.pyplot.style.use('ggplot')

        barx, bary = [], []
        for x, y in counter.most_common(limit):
            barx.append(str(x))
            bary.append(y)
        _, ax = matplotlib.pyplot.subplots()
        ax.barh(barx, bary, align='center')

        for xi, xv in enumerate(bary):
            ax.text(xv + 1, xi - 0.20, str(xv), color='black')

        if xlimit:
            ax.set_xlim(0, xlimit)

        if title:
            ax.title.set_text(title)

        if filename:
            matplotlib.pyplot.savefig(filename, dpi=300, format='png', bbox_inches='tight')
        else:
            matplotlib.pyplot.show()
