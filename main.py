# Primeiro exemplo em Python

print("Olá Mundo!")

# comando de entrada armazenando na variavel
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

# dira ola informando o nome do usuario
print(f"Olá, {nome}, sua idade é: {idade}")


# começa perguntando o nome do produto
nomeP = input("Informe o nome do produto: ")
qtde = int(input("Digite a quantidade desse produto no estoque: "))
preco = float(input("Digite o preço desse produto: "))

print(f"Nome do produto: {nomeP}")
print(f"Quantidade disponivel: {qtde}")
print(f"Preço por unidade: {preco}")

# Se o estoque do produto estiver abaixo de 50,
# exiba a frase "Estoque do (produto) está muito baixo! providencie mais"

if qtde < 50:
    print(f"Estoque do produto {nomeP} está muito baixo! Providencie mais!")

# Calcule o valor do produto com imposto que é o valor bruto mais 10% (imposto)
preco_com_imposto = preco * 1.1
print(f"Preço total (com imposto): {preco_com_imposto}")

# terceiro exemplo com python arrays
# unico item
fruta = "morango"
print(fruta)

# iniciar arrays frutas informando o nome das frutas selecionadas
frutas = ["laranja", "maçã", "banana", "pêra"]

# Exibir um conteudo do array inteiro
print(frutas)

# Exiba o nome da segunda fruta armazenada no array frutas
print(frutas[1])

# Quantas frutas temos no array frutas
qtde_frutas = len(frutas)
print(qtde_frutas)

# função append() adicionamos mais itens
frutas.append("abacate")
frutas.append("abacate")

# quantas frutas temos?
print(len(frutas))
print(frutas)

# quero apagar a quarta frutas (abacate) remove pelo indice
frutas.pop(4)
print(frutas)

# adiciona romã a lista de frutas
frutas.append("romã")

# remove banana da lista de frutas remove pelo nome
frutas.remove("banana")

frutas.insert(1, "morango")

# exibir na tela fruta a fruta percorrendo a lista com for each
numerador = 1

for fruta in frutas:
    print(f"{numerador}a. fruta: {fruta}")
    numerador += 1

# ordenar em ordem alfabetica
frutas_ordenadas = frutas.copy()
frutas_ordenadas.sort()

print(frutas_ordenadas)
print(frutas)

# quarto exemplo em python
# usuário digita o valor de três produtos
precos = []

numerador = 1
while(numerador <= 5):
    precos.append(float(input(f"Digite o preço do {numerador}o. produtos: ")))
    numerador += 1

print(precos)

# Percorrer a lista de preços de produtos
total = 0
for preco in precos:
    print(preco)
    total = total + preco

print(total)
print(total / len(precos))

# quinto exemplo python
# criar um dicionário de dados para guardar informações do produto
produto = {
    "nome": "Smart tv LG",
    "qtde": 10,
    "preco": 3999.90
}

print(produto)

# se eu quiser saber a quantidade do produto presente no dicionario "produto"
print(produto['qtde'])

# Sexto exemplo em python
# lista de produtos
produtos = []

# Usuário vai digitar três produtos de sua escolha, informando nome, qtde e preço
num = 1
while (num <=3):
    nome = input(f"Informe o nome do {num}o. produto: ")
    gtde = int(input(f"Digite a quantidade do {num}o. produto: "))
    preco = float(input(f"Digite o preço do {num}o. produto: "))
    produto = {
        "nome": nome,
        "qtde": qtde,
        "preco": preco
    }
    produtos.append(produto)
    num += 1

print(produtos)

# quero saber o preço do terceiro produto (laptop)
print(produtos[2]['preco'])

# quero saber o nome do primeiro produto (tv)
print(produtos[0]['nome'])

# somar todos os produtos em estoque
total_estoque = 0
total_preco = 0
for produto in produtos:
    total_estoque = total_estoque + produto['qtde']
    total_preco = total_preco + produto['preco']

print(f"Total em estoque: {total_estoque}")
print(f"Preço total: {total_preco}")

# comprar produtos
compras = []

continuar_comprando = True

while(continuar_comprando == True):
    print("Qual produto vc quer comprar? Sendo: ")
    num = 0
    for produto in produtos:
        print(f"{num} : {produto['nome']}")
        num += 1

    codigo = int(input("Digite a opção desejada: "))

    print(f"Produto escolhido: {produtos[codigo]['nome']}, preço: {produtos[codigo]['preco']}")

    qtde_desejada = int(input(f"Quantos {produtos[codigo]['nome']} você quer comprar? "))

    compra = {
        "codigo": codigo,
        "qtde_desejada": qtde_desejada
    }
    compras.append(compra)

    # Dar baixa no estoque
    produtos[codigo]['qtde'] = produtos[codigo][qtde] - qtde_desejada

    continuar_comprando = False

print(produtos)

# Total da compra
codigo = compras[0]['codigo']
total = compras[0]['qtde_desejada'] * produtos[codigo]['preco']
print(total)

# revisão de loops
i = 1

while (i <= 10):
  print(i)
  i += 1

i = 10

while (i>=1):
  print(i)
  i -= 1

# Validação de entrada
numero = int(input("Digite um número de 1 até 10: "))
while(numero < 1 or (numero > 10)):
  print("Número inválido!")
  numero = int(input("digite um número de 1 até 10: "))

print(f"O número informado foi {numero}")

# for each
numeros = [10, 15, 12, 52, 3, 2]

for numero in numeros:
  print(numero)

# Calcular 4 ao cubo...
print(4*4*4)
print(pow(4,3))

print(5+4)

# Declarar a função soma() que recebe dois números inteiros e retorna a soma entre eles
def soma(num1, num2):
  total = num1 + num2
  return total

soma1 = soma(5,4)
print(soma1)

soma2 = soma(15, -5)
print(soma2)

print(soma(1,3))

total = soma(soma(5,6), soma(8,2))
soma3 = soma(total, 20)
print(soma3)

#Criar uma função que calcula o fatorial de um determinado número
def fatorial(numero):
  total = 1
  contador = numero
  while(contador >= 1):
    total = total * contador
    contador -= 1
  return total

print(fatorial(5))
