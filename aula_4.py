from collections import deque


# ----------------------- PARTE 1 ----------------------- #
# Mais sobre funções
#
# valor padrão dos argumentos
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


# chamando por argumendo nomeado (keywork argument)
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=" ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")  # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)  # 2 keyword arguments
parrot("a million", "bereft of life", "jump")  # 3 positional arguments
parrot("a thousand", state="pushing up the daisies")  # 1 positional, 1 keyword


# variadic arguments
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# parâmetros especiais (pouco usados)
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
"""


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# ----------------------- PARTE 2 ----------------------- #
# Estrutura de dados

a_bunch_of_things = [1, 2, 3, "asdf"]

a_bunch_of_things.append("qwer")

print(a_bunch_of_things)  # [1, 2, 3, "asdf", "qwer"]

numbers = [2, 3, 4]

a_bunch_of_things.extend(numbers)

a_bunch_of_things.insert(0, "i'm the first")

a_bunch_of_things.remove("asdf")

last_thing = a_bunch_of_things.pop()
first_thing = a_bunch_of_things.pop(0)

a_bunch_of_things.clear()

a_bunch_of_things.extend(numbers)

a_bunch_of_things.index(2)

a_bunch_of_things.count(2)

a_bunch_of_things.sort()

# lista como pilhas
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

stack.pop()
stack.pop()
stack.pop()

# lista como filas
stack = [3, 4, 5]
stack.append(6)
stack.append(7)

stack.pop(0)
stack.pop(0)
stack.pop(0)

# ou usando deque (mais eficiente)

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
queue.popleft()  # The first to arrive now leaves

queue.popleft()  # The second to arrive now leaves

# list comprehension

squares = []

for x in range(10):
    squares.append(x**2)

# o mesmo que:
squares = list(map(lambda x: x**2, range(10)))

# e agora usando comprehension:
squares = [x**2 for x in range(10)]

# excluindo partes da lista
del a_bunch_of_things[2]
del a_bunch_of_things[1:3]

# ----------------------- PARTE 3 ----------------------- #
# mais sobre outras estruturas:
tuplas = "https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences"
conjuntos = "https://docs.python.org/3/tutorial/datastructures.html#sets"
dicionarios = "https://docs.python.org/3/tutorial/datastructures.html#sets"
