from matplotlib import pyplot as plt

anos = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Cria um gráfico de linhas com os anos no eixo x e o pib no eixo y.
# PIB = Produto interno bruto nominal
plt.plot(anos, pib, color="blue", marker="o", linestyle="solid")

# Adiciona um título ao gráfico.
plt.title("PIB")

# Adiciona um nome no eixo y.
plt.ylabel("Bilhões de Dólares.")

# Adiciona um nome no eixo x.
plt.xlabel("Anos")

plt.savefig("imagens/1_pib.png")
plt.gca().clear()
# plt.show()

filmes = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Plote as barras com coordenadas x à esquerda [0, 1, 2, 3, 4]
# alturas [num_oscars]

plt.bar(range(len(filmes)), num_oscars)

plt.title("Meus filmes favoritos")
plt.ylabel("# de Prêmios da Academia")

# Rotula o eixo x com os nomes dos filmes nos centros das barras.
plt.xticks(range(len(filmes)), filmes)

plt.savefig("imagens/2_filmes.png")
plt.gca().clear()
# plt.show()

from collections import Counter

notas = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Agrupe as notas por decil, mas coloque o 100 com o 90.

histograma = Counter(min(nota // 10 * 10, 90) for nota in notas)

plt.bar(
    [x + 5 for x in histograma.keys()], histograma.values(), 10, edgecolor=(0, 0, 0)
)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# de estudantes")
plt.title("Distribuição de notas do Exame 1")
# plt.show()

plt.savefig("imagens/3_estudantes.png")
plt.gca().clear()


# Gráfico Malandro.

mencoes = [500, 505]
anos = [2017, 2018]

plt.bar(anos, mencoes, 0.8)
plt.xticks(anos)
plt.ylabel("# Número de vezes eu ouvi uma pessoa falar Data Science")

plt.axis([2016.5, 2018.5, 499, 506])
plt.title("Olhe o 'tamanho' desse aumento")
# plt.axis([2016.5, 2018.5, 0, 550])
# plt.title("Agora condiz com a realidade.")
plt.savefig("imagens/4_grafico_malandro.png")
plt.gca().clear()
# plt.show()

# Gráfico de Linhas ajuda a mostrar tendências.
variancia = [1, 2, 4, 8, 16, 32, 64, 128, 256]
vies_quadrado = [256, 128, 64, 32, 16, 8, 4, 2, 1]
erro_total = [x + y for x, y in zip(variancia, vies_quadrado)] # [(1, 256), (2, 128) ... (256, 1)]

xs = [i for i, _ in enumerate(variancia)] # Coloco números de 0 a 1 na variância e pego cada um deles criando um array. 

# Dá pra fazer múltiplas chamadas com o plt.plot
#  para mostrar séries múltiplas no mesmo gráfico.

plt.plot(xs, variancia, 'g-', label="Variância") # Linha sólida do Verde.
plt.plot(xs, vies_quadrado, 'r-.', label = "Viês^2") # Linha com pontos Vermelha.
plt.plot(xs, erro_total, 'b:', label = 'Erro Total') # Linha azul pontilhada.

# Como colocamos nomes em cada série, 
# é fácil ter as legendas.
plt.legend(loc=9) # Topo, Centro.
plt.xlabel("Complexidade do Modelo.")
plt.xticks([]) # Tira os ticks embaixo
plt.title("A troca de viés-variância")
# plt.show()
plt.savefig("imagens/5_graficos_de_linhas.png")
plt.gca().clear()


# Gráfico de Dispersão. 
# Opção para representar as relações entre pares de conjuntos 
# de dados.

# Relação entre o número de amigos dos usuários e o número 
# de minutos que eles passam no site por dia.

amigos = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(amigos, minutos) # Scatter = Espalhar.

# Colocar uma label em cada ponto.

for label, amigo, minuto in zip(labels, amigos, minutos):
    plt.annotate(
                label, 
                xy = (amigo, minuto), #Coloca essa label nesse ponto aqui.
                xytext = (5, -5), # Mudar um pouquinho a posição do texto.
                textcoords = 'offset points'
                )

plt.title("Minutos diários X Número de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("Minutos diários gastos no site.")
# plt.show()
plt.savefig("imagens/6_grafico_de_dispersao.png")
plt.gca().clear()
