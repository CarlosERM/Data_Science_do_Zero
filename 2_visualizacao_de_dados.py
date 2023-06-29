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


