# sintaxe básica do python

# a partir de agora, seguiremos esse tutorial do próprio Python:
# https://docs.python.org/3/tutorial/index.html
# (com leves alterações)

# criação/atribuição de variáveis
i = 0  # um int
i = 1.0  # um float
i = 1_000_000  # um int, o mesmo que 1000000, mas mais fácil de ler
i = 1e6  # um float

nome = "Rodrigo Eiti Kimura"
# comentários são escritos após a cerquilha

# operações matemáticas:

# exemplos de operações matemáticas
"""
2 + 2

50 - 5 * 6

(50 - 5 * 6) / 4

8 / 5  # division always returns a floating point number
"""

# importante:
i = 1  # type(i) == "<class 'int'>"
i = 1.0  # type(i) == "<class 'float'>"
i = 1 / 2  # i == 0.5 and type(i) == "<class 'float'>"
i = 1 // 2  # i == 0 and type(i) == "<class 'int'>"

# strings (texto):
"""
'spam eggs'  # single quotes

"Paris rabbit got your back :)! Yay!"  # double quotes

'1975'  # digits and numerals enclosed in quotes are also strings

'doesn\'t'  # use \' to escape the single quote...

"doesn't"  # ...or use double quotes instead

'"Yes," they said.'

"\"Yes,\" they said."

'"Isn\'t," they said.'

"""

# ou podemos usar triple-quotes, como acima

# concatenar strings
a_string = "Py"
a_string = a_string + "thon"

# ou
a_string = "Py" "thon"

# ou
a_string = (
    "Py"  # primeira parte
    "thon"  # segunda parte
)


# Slicing
a_string[0]  # "P"
a_string[1]  # "y"
a_string[0:2]  # "Py"
a_string[:2]  # "Py"
a_string[-1]  # "n"
a_string[-2]  # "o"
a_string[2:]  # "thon"
a_string[:]  # "Python"

# interpolação de strings
f"{a_string} é a melhor linguagem de programação!"

# lists:
# coleção ordenada e mutável de valores
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

anything = [1, "2", 3.0]

# tuples:
# coleção ordenada e imutável de valores
numbers = (1, 2, 3, 1, 4)
print(numbers.count(1))

# dicts:
# são mapeamentos, mapeam uma chave para um valor (o famoso "de-para")
parentescos = {
    "pai/mãe": "filho/a",
    "avô/ó": "neto/a",
    "tio/a": "sobrinho/a",
    "primo/a": "primo/a",
    "sogro/a": "genro/nora",
}
# os itens à esquerda do ":" são as chaves e precisam ser únicas
# os itens à direita do ":" são os valores

d = {
    1: "Rodrigo",
    2: "Andre",
    3: "Cleber",
}

# sets:
# armazenam valores únicos e não ordenados
um_set = {1, 2, 3}
outro_set = {2, 3, 4, 5}

# possui métodos anaálogos aos conjuntos matemáticos
um_set.intersection(outro_set)
um_set.union(outro_set)


# estruturas de controle
# if-else
if a_string == "Python":
    print("Python is nice")
elif len(a_string) > 2:
    print(a_string)
else:
    print("Whatever...")

# while-loop:
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

# for-loop
for numero in [1, 2, 3]:
    print("Número: ", numero)
    print("O dobro é:", numero * 2)

for letra in "abcde":
    print(letra)
    if letra == "d":
        break

for x in [1, 2, 3, "4", 5, "6"]:
    if isinstance(x, int):
        continue
    else:
        print(x, " não é um int")

# o padrão abaixo é bastante usado:
for chave, valor in parentescos.items():
    print(f"Se eu sou seu/sua {chave}, vc é meu/minha {valor}")


# definindo funções
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


# Now call the function we just defined:
fib(2000)
