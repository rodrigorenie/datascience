# Exercicio 1

## 1) criar um namespace com nome hospital.

> create_namespace 'hospital'

## 2) criar uma estrutura de dados para armazenas os seguintes dados.

paciente (nome,cpf,rg, endereco residencia[rua,numero,bairro], endereco comercial[rua,numero,bairro])
leito (numeroleito,data_entrada)
cid ( codigo_da_cid , data_incidencia)

> create 'hospital:hospital', 'paciente', 'end', 'com', 'leito', 'cid'

## 3) inserir 4 registro.

> put 'hospital:hospital', '00001', 'paciente:nome', 'Fulano Silva'
> put 'hospital:hospital', '00001', 'paciente:cpf', '03231323-21'
> put 'hospital:hospital', '00001', 'paciente:rg', '03323-1'
> put 'hospital:hospital', '00001', 'end:rua', 'Rua Saturnino de Brito'
> put 'hospital:hospital', '00001', 'end:num', '71'
> put 'hospital:hospital', '00001', 'end:bairro', 'Jd Botanico'
> put 'hospital:hospital', '00001', 'com:rua', 'Rua Saturnino de Brito'
> put 'hospital:hospital', '00001', 'com:num', '71'
> put 'hospital:hospital', '00001', 'com:bairro', 'Jd Botanico'
> put 'hospital:hospital', '00001', 'leito:leitonum', '001'
> put 'hospital:hospital', '00001', 'leito:entrada', '29/02/1995'
> put 'hospital:hospital', '00001', 'cid:cid', '130-3'
> put 'hospital:hospital', '00001', 'cid:incidencia', '25/02/1995'

> put 'hospital:hospital', '00002', 'paciente:nome', 'Akira Kurosawa'
> put 'hospital:hospital', '00002', 'paciente:cpf', '053393832-14'
> put 'hospital:hospital', '00002', 'paciente:rg', '08632323-7'
> put 'hospital:hospital', '00002', 'end:rua', 'Av. Das Nações Unidas'
> put 'hospital:hospital', '00002', 'end:num', '1441'
> put 'hospital:hospital', '00002', 'end:bairro', 'Jardins'
> put 'hospital:hospital', '00002', 'com:rua', 'Av. Águas espraiadas'
> put 'hospital:hospital', '00002', 'com:num', '156'
> put 'hospital:hospital', '00002', 'com:bairro', 'Canteiras'
> put 'hospital:hospital', '00002', 'leito:leitonum', '002'
> put 'hospital:hospital', '00002', 'leito:entrada', '19/07/1999'
> put 'hospital:hospital', '00002', 'cid:cid', '185-0'
> put 'hospital:hospital', '00002', 'cid:incidencia', '09/02/1999'

> put 'hospital:hospital', '00003', 'paciente:nome', 'Ciclano da Gomes'
> put 'hospital:hospital', '00003', 'paciente:cpf', '98432932-85'
> put 'hospital:hospital', '00003', 'paciente:rg', '09438812-9'
> put 'hospital:hospital', '00003', 'end:rua', 'Av. Brasil'
> put 'hospital:hospital', '00003', 'end:num', '1888'
> put 'hospital:hospital', '00003', 'end:bairro', 'Centro'
> put 'hospital:hospital', '00003', 'leito:leitonum', '003'
> put 'hospital:hospital', '00003', 'leito:entrada', '19/07/2002'
> put 'hospital:hospital', '00003', 'cid:cid', '10-1'
> put 'hospital:hospital', '00003', 'cid:incidencia', '19/07/2002'

> put 'hospital:hospital', '00004', 'paciente:nome', 'Alexei Tarkovsky'
> put 'hospital:hospital', '00004', 'paciente:cpf', '485726389-43'
> put 'hospital:hospital', '00004', 'paciente:rg', '875544292-4'
> put 'hospital:hospital', '00004', 'end:rua', 'Av. Juscelino Kubitscheck'
> put 'hospital:hospital', '00004', 'end:num', '1950'
> put 'hospital:hospital', '00004', 'end:bairro', 'Centro'
> put 'hospital:hospital', '00004', 'leito:leitonum', '004'
> put 'hospital:hospital', '00004', 'leito:entrada', '19/10/2011'
> put 'hospital:hospital', '00004', 'cid:cid', '10-1'
> put 'hospital:hospital', '00004', 'cid:incidencia', '12/10/2011'

## 4) atualizar o endereco comercial.

> put 'hospital:hospital', '00001', 'com:rua', 'Av. Rio Branco'
> put 'hospital:hospital', '00001', 'com:num', '87'
> put 'hospital:hospital', '00001', 'com:bairro', 'Centro'

## 5) listar/mostrar os dados de 1 registro 

> get 'hospital:hospital', '00001'

## 6) deletar a familia de endereco residencial de um registro.

> delete 'hospital:hospital', '00004', 'end:rua'
> delete 'hospital:hospital', '00004', 'end:num'
> delete 'hospital:hospital', '00004', 'end:bairro'

## 7) deletar um registro total.

> deleteall 'hospital:hospital', '00003'
