# Rodrigo Renie de Braga Pinto
# TEXT ANALYSIS(Apostila)Parte 0.docx
# Exercitando 2
# Abra o arquivo Romance.docx e faça o que se pede

import docx

romance_path = 'dados/ROMANCE.docx'
romance_doc = docx.Document(romance_path)

# Crie uma lista com os parágrafos do documento
plist = [p.text for p in romance_doc.paragraphs]

# Quantos parágrafos o documento possui?
print('Quantos parágrafos o documento possui? R: {}'.format(len(plist)))

# Imprima o conteúdo do 1º parágrafo  do texto
print('1º Parágrafo: {}'.format(plist[0]))

# Imprima os parágrafos 3 a 6, inclusive
for n in range(3, 7):
    print('{}º Parágrafo: {}'.format(n, plist[n]))

# O termo ‘Machado’ está no documento?
termo = 'Sim' if 'Machado' in '\n'.join(plist) else 'Não'
print('O termo ‘Machado’ está no documento? R: {}'.format(termo))

# Crie um  texto corrido a partir dos parágrafos lidos
ptext = '\n'.join(plist)

# Substitua o termo ‘Batista’ por ‘João Batista’
ptext = ptext.replace('Batista', 'João Batista')
