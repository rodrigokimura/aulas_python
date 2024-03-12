# ----------------------- PARTE 1 ----------------------- #
# Erros e exceções
# https://docs.python.org/3/tutorial/errors.html

# Erros de sintaxe
# Acontecem quando há algo de errado na sintaxe da linguagem
# Uma IDE bem configurada deve alertar esses erros antes mesmos de rodar o código

"""
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
"""

# Exceções

# Mesmo que o código esteja sintaticamente correto, erros podem acontecer:

"""
>>> 10 * (1/0)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> 4 + spam*3

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

>>> '2' + 2

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
"""

# Lista de exceções built-in:
builtin_exceptions = (
    "https://docs.python.org/3/library/exceptions.html#bltin-exceptions"
)

# ----------------------- PARTE 2 ----------------------- #
# Tratando exceções


# Tratamos as exceções usando try-except:
def ask_for_number():
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


# é possível capturar múltiplas exceções para a mesma tratativa:
data = {"asdf": [0, 1, 2]}


def get_first_element_of_list_in_asdf(data):
    try:
        return data["asdf"][0]
    except (KeyError, IndexError):
        print("Formato errado!")


# Como funciona a ordem das tratativas para subclasses:


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


def raise_exceptions():
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")


# BaseException: superclasse comum a todas as exceções
# Exception: superclasse comum das exceções não-fatais
# Exceções que não são subclasse de Exception geramente não são tratadas!
#
# Exception pode ser usada para capturar exceções genericamente, mas é uma boa prática fazer tratativas específicas
# O uso mais comum de Exception é para print/log acrescido de raise


def open_database():
    try:
        f = open("myfile.txt")
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error:", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


# Tratativas de exceções tratam também as exceções de dentro de chamadas de funções


def this_fails():
    x = 1 / 0


def catch_inner_exception():
    try:
        this_fails()
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)


# ----------------------- PARTE 3 ----------------------- #
# Levantando exceções

# o statement raise força uma exceção a acontecer


def raise_an_error():
    raise NameError("HiThere")


"""
>>> raise_an_error()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
"""

# Pode ser usado com a classe da exceção ou uma instância da exceção:
"""

raise ValueError
raise ValueError()
raise ValueError("Valor errado")

"""

# Quando usado para levantar uma exceção sendo capturada (re-raise), pode se usado sozinho

try:
    raise_an_error()
except NameError:
    print("An exception flew by!")
    raise
