string = 'Ainda que falasse as línguas dos homens e falasse a língua dos anjos,' \
      'sem amor eu nada seria.'

for c in string:
    print(c)

string_list = string.split()
print(string_list)
print('Palavras na string: {}'.format(len(string_list)))

for p in string_list:
    print(p)

string = string.replace('dos homens', 'do mundo')
print(string)

print('Do 21º ao 30º caracter: {}'.format(string[21:31]))
print('Os últimos 15 caracteres: {}'.format(string[-15:]))

with open('string.txt', 'w') as f:
    f.write(string+'\n')
