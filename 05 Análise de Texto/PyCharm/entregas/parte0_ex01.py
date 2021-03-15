# Rodrigo Renie de Braga Pinto
# TEXT ANALYSIS(Apostila)Parte 0.docx
# Exercitando 1
# Execute o que se pede.

# Crie uma string com o conteúdo abaixo
string = 'Ainda que falasse as línguas dos homens e falasse a língua dos ' \
         'anjos, sem amor eu nada seria.'

# Imprima cada caractere da string
for c in string:
    print(c)

# Segmente a string em uma lista
string_list = string.split()
print(string_list)

# Quantas palavras há na lista?
print('Palavras na string: {}'.format(len(string_list)))

# Imprima cada palavra da string
for p in string_list:
    print(p)

# Substitua o termo 'dos homens' por  'do mundo'
string = string.replace('dos homens', 'do mundo')
print(string)

# Imprima o fragmento que vai do 21º até o 30º caracteres
print('Do 21º ao 30º caracter: {}'.format(string[21:31]))

# Imprima os últimos 15 caracteres
print('Os últimos 15 caracteres: {}'.format(string[-15:]))

# Salve a sentença em um arquivo do tipo txt
with open('parte0_ex01.txt', 'w') as f:
    f.write(string+'\n')
