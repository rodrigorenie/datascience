CREATE KEYSPACE "Escola" WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1 } ;

USE "Escola";

CREATE TABLE aluno (id int, nome text, materia text, nota float, emails set<text>, PRIMARY KEY ((materia, id)) ;

INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (1, 'Friedrich Wilhelm Nietzsche', 'Filosofia com Martelo', 9.9, {'Übermensch@zaratustra.org'});

INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (2, 'Immanuel Kant', 'Critica da Razão', 9.9, {'imperativo@reinenbernunft.org'});

INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (3, 'Fiódor Mikhailovitch Dostoiévski', 'Análise de livre-arbitro', 9.9, {'jogador@Karamazov.org'});

INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (4, 'Arthur Schopenhauer', 'Representação', 9.9, {'vontade@representacao.org'});

INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (5, 'Martin Heidegger', 'Ontologia', 9.9, {'principio@metafisica.org'});



 UPDATE aluno SET emails = emails + {'martinho@metafisica.org'} WHERE id = 5 and materia = 'Ontologia';


UPDATE aluno SET emails = emails - {'martinho@metafisica.org'} WHERE id = 5 and materia = 'Ontologia';


INSERT INTO aluno (id, nome, materia, nota, emails) VALUES (6, 'Jean-Paul Charles Aymard Sartre', 'Nada', 9.9, {'lemouche@existencia.org'}) USING TTL 3600;


copy aluno (id, materia, nome, nota, emails) to 'pensa0.csv' ;
copy aluno (id, materia, nome, nota, emails) from 'pensa1.csv'  ;


select materia, id, nome, TTL(nome) from aluno;



Pensa1.csv:
7,Existencialismo,Simone Lucie-Ernestine-Marie Bertrand de Beauvoir,9.9,{'Deuxième@sexe.org'}
8,Totalitarismo,Hannah Arendt,9.7,{'condition@totalitarism.org'}
9,Dialetica,Slavoj Žižek,8.8,{'zizek@laibach.org'}
10,Lógica,Karl Raimund Popper,10.0,{'intolerant@tolerance.org'}

Pensa0.csv
1,Filosofia com Martelo,Friedrich Wilhelm Nietzsche,9.9,{'Übermensch@zaratustra.org'}
5,Ontologia,Martin Heidegger,9.9,{'principio@metafisica.org'}
6,Nada,Jean-Paul Charles Aymard Sartre,9.9,{'lemouche@existencia.org'}
4,Representação,Arthur Schopenhauer,9.9,{'vontade@representacao.org'}
3,Análise de livre-arbitro,Fiódor Mikhailovitch Dostoiévski,9.9,{'jogador@Karamazov.org'}
2,Critica da Razão,Immanuel Kant,9.9,{'imperativo@reinenbernunft.org'}

