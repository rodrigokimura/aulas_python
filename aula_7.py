# Sobre classes

# armazenam dados
# executam ações


# sem usar classes, como ficaria um exemplo de cálculo de rentabilidade média de uma carteira de investimentos:

investimento_x = {"nome": "asdf", "rentabilidade": 0.1}
investimento_y = {"nome": "qwer", "rentabilidade": 0.2}

carteira = [
    {"investimento": investimento_x, "alocacao": 0.5},
    {"investimento": investimento_y, "alocacao": 0.5},
]


def obter_rentabilidade(carteira):
    return sum(
        i.get("investimento").get("rentabilidade") * i.get("alocacao") for i in carteira
    )


rentabilidade_da_carteira = obter_rentabilidade(carteira)

# como poderia ficar usando classes:


class Investimento:
    def __init__(self, nome: str, rentabilidade: float) -> None:
        self.nome = nome
        self.rentabilidade = rentabilidade


class Alocacao:
    def __init__(self, investimento: Investimento, percentual: float) -> None:
        self.investimento = investimento
        self.percentual = percentual


class Carteira:
    def __init__(self, composicao: list[Alocacao]) -> None:
        self.composicao = composicao

    def obter_rentabilidade(self):
        return sum(i.investimento.rentabilidade * i.percentual for i in self.composicao)


investimento_x = Investimento("asdf", 0.1)
investimento_y = Investimento("qewr", 0.2)

carteira = Carteira([Alocacao(investimento_x, 0.5), Alocacao(investimento_y, 0.5)])
rentabilidade_da_carteira = carteira.obter_rentabilidade()


# se for preciso validar que a carteira possui 100% de alocação, como ficaria?
