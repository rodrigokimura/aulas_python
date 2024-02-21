# ----------------------- PARTE 1 ----------------------- #
# FUNÇÕES PYTHON
#
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# assistir o vídeo sobre funções em python

# clonar o repositorio
repo = "https://github.com/rodrigokimura/manimations"

# entrar no repo e instalar as dependências
comando = "pipenv install"

# com o ambiente ativado, rodar o comando abaixo
comando = "manim -pql src/python_tutorial/functions.py"


# ----------------------- PARTE 2 ----------------------- #
# RODANDO AS FUNÇÕES (INTRO A TESTES)


# para "rodar" uma função, basta chamá-la
def isto_eh_uma_funcao():
    print('vc "rodou" a função!')


isto_eh_uma_funcao()  # importante adicionar os parênteses!

# para ver ela rodando, é só usar o comando python no terminal
comando = "python aula_3.py"

# mas ao invés de colocar a chamada na raiz do módulo (arquivo),
# o mais adequado é usar o padrão abaixo:
#
# if __name__ == "__main__":
#     isto_eh_uma_funcao()

# além do terminal, as IDEs tbm possuem opções para rodar arquivos python

# outra forma de executar código python é por meio dos testes automatizados
# o python possui duas libs de teste "padrão" (parte do Python standard library):
import unittest
import doctest

libs = {
    unittest: "https://docs.python.org/3/library/unittest.html",
    doctest: "https://docs.python.org/3/library/doctest.html",
}

# além dessas libs "standard", temos libs third-party, por exemplo:
third_party_test_libs = {
    "pytest": "https://docs.pytest.org/en/8.0.x/",
    "behave": "https://behave.readthedocs.io/en/latest/",
    "locust": "https://locust.io/",
}

# ----------------------- PARTE 3 ----------------------- #
# TESTANDO SEUS CONHECIMENTOS

# abra o arquivo exercicios/investimentos.py
# e implemente a lógica de cada uma das funções
# em seguida, rode o pytest para conferir se a implementação está correta
# abra o arquivo exercicios/test_investimentos.py e complemente os testes
