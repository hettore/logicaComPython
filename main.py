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

#Calcule o valor do produto com imposto que é o valor bruto mais 10% (imposto)
preco_com_imposto = preco * 1.1
print(f"Preço total (com imposto): {preco_com_imposto}")

