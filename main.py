#>>>>>>>>>>>>>>>>>>>>>>>>> INTRODUCAO A PYTHON <<<<<<<<<<<<<<<<<<<<<<<<<#

#>>> 1. Commentarios <<<<

#>>> 2. Representacao de Strings<<<

#>>> 3. Hello World<<<
#print ('Hello World')<<<

#>>> 4. Possiveis erros
#>>> 4.1. Faltando parantese
#>>> 4.2. P em vez de p
#>>> 4.3. Faltando aspa
#>>> 4.4. Erro ortogrfico?

#>>> 5. Saida c/ varias linhas
#print ('Primeira Linha\nSegunda Linha')
#print ('''Primeira Linha
#Segunda Linha''')

#>>> 6. Execucao passo-a-passo
#print ('Primeira Linha')
#print ('Segunda Linha')

#>>> 7. Historico de Versoes


#>>>>>>>>>>>>>>>>>>>> PRIMEIROS PROGRAMAS EM PYTHON <<<<<<<<<<<<<<<<<<<<#

#PARTE 1

# 1. Como definir identificadores de variavies
#num_pessoas

# 2. Como criar variaveis
#num_pessoas = 20000
#personagem = 'Mario'
#vidas = 6
#moedas = 20
#pontos = 10000
#tempo = 246.57

# 3. Como uysar o valor de uma variavel
#print (num_pessoas)
#print (personagem)
#print (vidas)
#print (moedas)
#print (pontos)
#print (tempo)

# 4. Exemplo: "Hello World" personalizado
#nome = 'Patrick Perovano'
#print ('Ola,', nome)
#print (f'Ola, {nome}')



#PARTE 2

# 1. Como alterar o valor de uma variavel
#nome = 'Patrick'
#nome = 'Dani'


# 2. Analisar variaveis usando debugger
#nome = 'Patrick'
#nome = 'Dani'
#idade = 36
#peso = 99.9
#print (nome)
#print (idade)
#print (peso)


#>>>>>>>>>>>>>>>>>>>>>>>> OPERADORES MATEMATICOS <<<<<<<<<<<<<<<<<<<<<<<#

#PARTE 1

# 1. Soma (+)
#print (2 + 2)
#print (2.0 + 2)
#print (2.0 + 3.0)

# 2. Subtracao (-)
#print (2 - 2)
#print (2.0 - 2)
#print (2.0 - 3.0)

# 3. Multiplicacao (*) - Ex: tabuada
#print ('2x1 = ',2 * 1)
#print ('2x2 = ',2 * 2)
#print ('2x3 = ',2 * 3)
#print ('2x4 = ',2 * 4)
#print ('2x5 = ',2 * 5)
#print ('2x6 = ',2 * 6)
#print ('2x7 = ',2.0 * 7)
#print ('2x8 = ',2 * 8)
#print ('2x9 = ',2 * 9)
#print ('2x10 = ',2 * 10)

# 4. Divisao (/, //)
#print (6 / 2)
#print (7.0 / 2.0)
#print (7.0 // 2.0)
#print (2 // 3)


# 5. Exponenciacao (**) - Ex: Quadrados de 1 a 5
#print( 3 ** 2)
#print( 3.0 ** 2)
#print( 1 ** 2)
#print( 2 ** 2)
#print( 3 ** 2)
#print( 4 ** 2)
#print( 5 ** 2)



#PARTE 2

# 1. Calculos simples com variaveis
#numero1 = 3
#numero2 = 5
#resultado = (numero1 + numero2)
#print(resultado)
#resultado = (numero1 - numero2)
#print(resultado)
#resultado = (numero1 * numero2)
#print(resultado)
#resultado = (numero1 / numero2)
#print(resultado)
#resultado = (numero1 // numero2)
#print(resultado)
#resultado = (numero1 ** numero2)
#print(resultado)

# 2. Precedencias: () > ** > *, /, // > +, -
#print (5 + 2 * 3 - 2 ** 3 + 3 / 2)
#print ((5 + 2) * 3 - 2 ** 3 + 3 / 2)

# 3. Exemplo: conta de restaurante
#item1 = 20.90
#item2 = 36.99
#item3 = 17.50
#gorjeta = 0.15

#total = (item1 + item2 + item3)
#total = total + gorjeta * total

#print ('Total da conta é: ', total)


# 4. Exemplo: conversao Mb/s -> MB/s
#conexao = 500
#taxa = conexao / 8
#print (f'Com {conexao} Mb/s voce consegue uma taxa de {taxa} MB+/s')

# 5. Atualizacao de variaveis (+=, -= etc.)
#pontos = 0
#print(pontos)

#pontos = pontos + 10
#pontos += 10
#print(pontos)

#pontos = pontos + 15
#pontos += 15
#print(pontos)

#pontos = pontos - 5
#pontos += -5
#print(pontos)