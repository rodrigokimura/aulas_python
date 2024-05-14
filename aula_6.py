# PARTE 0: Usando a IDE
#
# o que diferencia uma IDE de um editor de texto?
# - capacidade de reconhecer código
# - capacidade de debugar código
# além disso, deve proporcionar velocidade/praticidade editar texto
# outras características desejáveis:
# - integração com git
# - integração com terminal
# - integração com navegador de arquivos

# comandos essenciais:
# de código:
# - inspecionar objeto (variável/função/classe)
# - navegar pelas definições/referências
# - renomear objeto
# de edição:
# - inserir linha nova
# - mover linha(s)
# - indentar/deindentar linha(s)
# - encontrar arquivo
# - encontrar texto nos arquivos
# - substituir texto


# PARTE 1: type hints


def asdf(a):
    return a.split(" ")


def test_asdf():
    result = asdf("asdf qwer")
    assert result == ["asfd", "qwer"]


def asdf2(a: str) -> list[str]:
    return a.split(" ")


def test_asdf2():
    result = asdf2("asdf qwer")
    assert result == ["asdf", "qwer"]


def get_timestamp(register):
    return register.get("timestamp")
