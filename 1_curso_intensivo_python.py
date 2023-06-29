# Módulos
import re
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
my_regex = re.compile("[0-9]+", re.I)
print(my_regex)

import re as regex

my_regex = regex.compile("[0-9]+", re.I)

from collections import defaultdict, Counter

lookup = defaultdict(int)
my_counter = Counter()


match = 10
# print(match)
from re import *

# print(match)


# Funções
def double(x):
    """
    Essa função multiplica a entrada por 2.
    """
    return x * 2


def apply_to_one(f):
    """
    Essa função chama a função f usando 2 como argumento.
    """
    return f(2)


# print(apply_to_one(double))
# Funções anônimas
y = apply_to_one(lambda x: x + 4)
print(y)

# Strings
tab_string = "\t"
not_tab_string = r"\t"
multiline_string = """
Oi.
Oi.
Oi.
"""
first_name = "Carlos"
last_name = "Eduardo"
# print(f"{first_name} {last_name}")

# print(tab_string, not_tab_string, multiline_string)

# Exceções
try:
    print(0 / 0)
except ZeroDivisionError:
    print("Não dá pra dividir por 0.")

# Listas

integer_list = [1, 2, 3, 4, 5]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)
list_sum = sum(integer_list)

print(integer_list, heterogeneous_list, list_of_lists, list_length, list_sum)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# A fatia i:j tem o i incluíod e j não incluído
first_three = x[:3]
three_to_end = x[3:]
four_to_seven = x[4:8]
without_first_and_last = x[1:-1]
print(without_first_and_last)

# Operador in.
# print(10 in x)
y = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x.extend(y)
print(x)
x.append(-1)
print(x)

x, y = [99, 98]
_, h = [99, 98]

# print(h)

# Tuplas
my_tuple = (1, 2)
other_tuple = 1, 2
print(my_tuple, other_tuple)

try:
    my_tuple[1] = 1
except TypeError:
    print("Não posso modificar uma tupla.")


def sum_and_product(x, y):
    """
    Tuplas são uma forma eficaz de retornar múltiplos valores.
    """
    return (x + y), (x * y)


# print(sum_and_product(1, 2))

(
    x,
    y,
) = (
    1,
    2,
)
# print(x, y)
x, y = y, x  # Trocar variáveis.
# print(x, y)

# Dicionários
# empty_dict = {}

# print(empty_dict)
dicionario_literal = {"name": "Carlos Eduardo", "age": 21}
# print(dicionario_literal['age'])
# print("na1me" in dicionario_literal)
# print(dicionario_literal.get("oi"))
# print(dicionario_literal["oi"])

postagem = {"user": "Carlos Eduardo", "text": "Eu amo você", "hashtag": "#amor"}

# print(postagem.keys())
# print(postagem.values())


for key in postagem.keys():
    print(key)

for value in postagem.values():
    print(value)

# print("user" in postagem)

# defaultdict
# Quando procuramos uma chave que não está nele,
# ele adiciona um valora pra ela utilziando
# a função de argumento zero que indicamos ao criá-lo.
from collections import defaultdict

word_counts = defaultdict(int)

# Contadores.
# Conta ocorrências, que legal.
# from collections import Counter
c = Counter(
    [
        0,
        1,
        2,
        0,
        1,
        2,
        3,
        4,
        5,
        132,
        23,
        1,
        2,
    ]
)
# print(c.most_common(2))

# Conjunto
primes_below_10 = {2, 3, 4, 7}
# print(primes_below_10)
s = set()
s.add(1)
s.add(2)
s.add(3)

# print(s)
# print(3 in s) # in é uma operação muito rápida em conjuntos.
# Outra coisa bacana é que dentro dele você tem itens distintos.

# Fluxo de Controle
x = 2
eh_par = "par" if x % 2 == 0 else "impar"
# print(eh_par)

# Veracidade

um_menor_que_dois = 1 < 2
# print(um_menor_que_dois)
x = None
assert x is None

# Trem maluco. Se tiver, retorna o segundo valor, se não tiver retorna o primeiro.
s = ["lista"]
primeiro_char = s and s[0]

# print(primeiro_char)
# mais comprensível
n = None
eh_numero = n if n is not None else 0
print(eh_numero)
# Muito mais maneiro de ler.

print(all([True, 1, {}]))
print(any([False, 1]))
# Classificação
x = [5, 4, 3, 2, 1]
x.sort()
y = sorted(x)
print(x, y)

x = sorted([-5, 1, -2, 3], key=abs, reverse=True)
print(x)

# Compreensões de Listas
numeros_pares = [x for x in range(5) if x % 2 == 0]
print(numeros_pares)

quadrados = [x * x for x in range(5)]
print(quadrados)

quadrados_pares = [x * x for x in numeros_pares]
print(quadrados_pares)

dict_quadrado = {x: x * x for x in range(16)}
print(dict_quadrado)

conjunto_quadrado = {x * x for x in [1, -1]}
print(conjunto_quadrado)

zeros = [0 for _ in numeros_pares]
print(zeros)

pares = [(x, y) for x in range(10) for y in range(10)]
# print(pares)

pares_aumentam = [(x, y) for x in range(10) for y in range(x + 1, 10)]
# print(pares_aumentam)

# Testes Automatizados e Asserção
# Assert, verifica se a condição é verdadeira.
# Caso não seja ele vai dar um AssertionError

assert 1 + 1 == 1
assert 1 + 1 == 2, "1 + 1 deveria ser igual a 2, mas não é."


def item_menor(xs):
    return min(xs)


assert item_menor([1, 2, 3, 4, 5]) == 1, "O menor valor deveria ser 1"
assert item_menor([1, 0, -1, 2]) == -1

# Programação Orientada a Objetos


class CountingClicker:
    """Toda classe deve ter um docstring."""

    # Self refere-se à instância da classe específica.
    def __init__(self, count=0):
        """
        Toda a classe tem um cosntrtor chamado init que recebe os parametros necessários para construir uma isntância da classe.
        __ __ dunder, double underscore é um método especial.
        metodos de classes que começam com sublinhado são considerados rivados.

        """
        self.count = count

    def __repr__(self):
        """Representação de String de uma instânia de classe."""
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """Clique no contador"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker1 = CountingClicker()  # Count 0.
clicker2 = CountingClicker(100)  # Count 100
clicker3 = CountingClicker(count=1000)  # Countr 1000

# # Testes
clicker = CountingClicker()
assert clicker.read() == 0, "O clicador deve começar em 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "Depois de dois cliques o clicador deve ter count igual a 2"
clicker.reset()
assert clicker.read() == 0, "Depois do reset, o clicador deve retornar a 0."


class NoResetClicker(CountingClicker):
    """
    Essa classe herdou todos os métodos de Counting Clicker,
    mas o seu método reset não faz nada.
    """

    def reset(self):
        pass


clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "O reset não deve fazer nada."

# Iteráveis e Geradores


def generate_range(n):
    i = 0
    while i < n:
        yield i  # Cada chamada para yield produz um valor do gerador
        i += 1


for i in generate_range(10):
    print(f"i:{i}")


def natural_numbers():
    "retorna vlaores infinitos."
    n = 1

    while True:
        yield n
        n += 1


for i in natural_numbers():
    print(f"i:{i}")


names = ["Alice", "Bob", "Charlie", "Debbie"]

for i, name in enumerate(names):
    print(f"nome {i} é {name}")

# Aleatoriedade

from ast import List
import random

random.seed(10)

four_uniform_randoms = [random.random() for _ in range(4)]
# print(four_uniform_randoms)

random.seed(10)

# print(random.random())

random.seed(10)

# print(random.random())


meu_melhor_amigo = random.choice(["Bruno Fagner", "Bruno Batista"])
# print(meu_melhor_amigo)

# print(random.randrange(10))

ate_dez = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(ate_dez)
# print(ate_dez)

numeros_loterias = range(100)
numeros_vencedores = random.sample(numeros_loterias, 10)

# print(numeros_vencedores)

quatro_com_substituicao = [random.choice(range(10)) for _ in range(4)]
print(quatro_com_substituicao)

import re

re_examples = [
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3 == len(re.split("[ab]", "carbs")),
    "R-D-" == re.sub("[0-9]", "-", "R2D2"),
]

# assert all(re_examples), "Todos os exemplos da regex devem ser True"

lista_1 = ["a", "b", "c"]
lista_2 = [1, 2, 3]

zipado = [pair for pair in zip(lista_1, lista_2)]

# print(zipado)
# Numa lista maior que a outra, o zip para no final da primeira.
lista_1 = ["a", "b", "c", "d"]
lista_2 = [1, 2, 3]

zipado = [pair for pair in zip(lista_1, lista_2)]

# print(zipado)

# Extrair listas.
# Descompactar listas.
pares = [("a", 1), ("b", 2), ("c", 3)]
letras, numeros = zip(*pares)
# print(letras)
# print(numeros)
# print([1, 2, 3])
# print(*[1, 2, 3])
# Descompact listas * maneiro.


# args e kwargs
def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


g = doubler(f1)

# print(g(3))
# print(g(-1))

assert g(3) == 8, "(3 + 1) * 2 é deveria ser igual a 8"
assert g(-1) == 0, "(-1 + 1) * 2 é deveria ser igual a 0"


# Mágica
def magica(x, y, z):
    return x + y + z


x_y_lista = [1, 2]
z_dict = {"z": 3}

assert magica(*x_y_lista, **z_dict) == 6, "1 + 2 + 3 deve ser 6"

# print(*x_y_lista)
# print(**z_dict)

from typing import List, Optional


def f(xs: List[int]) -> None:
    xs.append()


def total(xs: List[float]) -> float:
    return sum(total)


melhor: Optional[float] = None  # pode ser none ou float.
