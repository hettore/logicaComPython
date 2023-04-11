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

