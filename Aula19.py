#Foor loops, essa função percorre uma lista e executa uma ação para cada item da lista

palavra = "Nicolas"

for letra in palavra:
    print(f"{letra} Está dentro do meu nome") 

#Teste com o usuario que ira realizar uma compra e recebe um e-mail 
compra = True
detalhes_compra = "Detalhes da compra: Produto Nike Air Force 1, Quantidade: 1, Preço: R$650.00"

for enviar in range(3):
    if compra:
        print("Sua compra foi realizada com sucesso!, enviaremos um e-mail para confirmação")
        print (detalhes_compra)
        break
    else:
        print("Compra não realizada verifique se os dados estão corretos e tente novamente")

#For loop nested, ele é utilizado para percorrer listas dentro de listas
#Existem dois tipos de for loop nested. o Outher loop e o Inner loop que no caso seria dentro e fora

for numero1 in range(1, 6):
    print( "Produto " + str(numero1))
    for numero2 in range(11):
        print ( numero1 , numero2)

""" Ele tem um uso bem interessante em casos de armazenar valores em uma lista dentro de outra lista
que já foi criada, e é necessario adicionar alguns valores ou produtos por exemplo."""

# For loop criando espaços entre as letras de uma palavra
#Exemplo 1 Nesse caso ele irá exibir de forma vertical cada letra da palavra
palavra = "Python"
for espaco in palavra:
    print(espaco)

#Exemplo 2 Nesse caso ele irá exibir de forma horizontal cada letra da palavra
palavra = "Python"
for espaco in palavra:
    print(f"{espaco},", end=" ")  

#Pedindo ao usuário para digitar uma palavra e exibindo cada letra com um espaço
palavra_usuario = input(" Por favor digite uma palavra: ")

for espaco in palavra_usuario:
    print(f"{espaco},", end="")

# Whilw loop, ele é utilizado para executar um bloco de código enquanto uma condição for verdadeira


