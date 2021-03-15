import nltk
from nltk import PorterStemmer, LancasterStemmer, RSLPStemmer
from nltk import word_tokenize

texto_e = 'My name is Maximus Decimus Meridius, commander of the armies of ' \
          'the north, General of the Felix legions and loyal servant to the ' \
          'true emperor, Marcus Aurelius. Father to a murdered son, husband ' \
          'to a murdered wife. And I will have my vengeance, in this life or ' \
          'the next (Gladiator, the movie).'

texto_p = 'Meu nome é Maximus Decimus Meridius, comandante dos exércitos do ' \
          'norte, general das legiões de Félix e servo leal ao verdadeiro ' \
          'imperador, Marcus Aurelius. Pai de um filho assassinado, marido ' \
          'de uma esposa assassinada. E eu terei minha vingança, nesta vida ' \
          'ou na próxima (Gladiador, o filme).'

tokens = word_tokenize(texto_e)
tokens = word_tokenize(texto_p)
tokens = ['amor', 'amora', 'amoroso']

porter = PorterStemmer()
stems_porter = [porter.stem(t) for t in tokens]

lancaster = LancasterStemmer()
stems_lancaster = [lancaster.stem(t) for t in tokens]

rslp = RSLPStemmer()
stems_rslp = [rslp.stem(t) for t in tokens]

print('{:12s} {:12s} {:12s} {}'.format('Tokens', 'Porter', 'Lancaster', 'RSLP'))
for t, p, l, r in zip(tokens, stems_porter, stems_lancaster, stems_rslp):
    print('{:12s} {:12s} {:12s} {}'.format(t, p, l, r))
