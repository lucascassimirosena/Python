
#Programa para verificar a idade do usuario e realizar compra caso maior de 18 anos.
#Atividade da universidade Anhembi Morumbi

# Os cantores de uma antiga dupla pretendem voltar a cantar juntos depois de muitos anos separados
# Para isso, contrataram uma empresa para realizar a confecção e a venda dos ingressos. 
# Também, foi desenvolvida uma página especial para o show, mas só será permitida a compra do ingresso para maiores de 18 anos.

# Com base nesse contexto, apresente a importância de se fazer a análise de um problema por meio da lógica de programação e do conceito aplicado na prática
# para verificar se a pessoa pode comprar um ingresso, de acordo com a idade.
# O algoritmo deve receber a idade da pessoa e efetuar uma avaliação, verificando se a idade é maior ou igual a 18 anos,
# para que o usuário possa comprar o ingresso. Se a idade for menor do que 18, será informado que sua entrada não é permitida.



idade = int(input("Insira a sua idade "))
if idade >= 18:
    print("Compra realizada com sucesso")
else:
    print("Entrada não permitida para menores de 18 anos")