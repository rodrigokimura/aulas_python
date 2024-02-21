def obter_montante(saldo_inicial, meses, rendimento, tipo_juros):
    """Obter montante após aplicação de juros em determinado tempo, exemplo:

    >>> obter_montante(100, 1, 0.01, 'simples')
    101.0

    >>> obter_montante(100, 5, 0.01, 'simples')
    105.0

    >>> obter_montante(100, 1, 0.01, 'composto')
    101.0

    >>> obter_montante(100, 2, 0.5, 'composto')
    225.0

    >>> obter_montante(100, 2, 1.0, 'composto')
    400.0
    """
    pass


def obter_montante_rendimento_simples(saldo_inicial, meses, rendimento):
    """Obtém montante após x meses usando juros simples, exemplo:

    >>> obter_montante_rendimento_simples(100, 1, 0.01)
    101.0

    >>> obter_montante_rendimento_simples(100, 5, 0.01)
    105.0
    """
    pass


def obter_montante_rendimento_composto(saldo_inicial, meses, rendimento):
    """Obtém montante após x meses usando juros simples, exemplo:

    >>> obter_montante_rendimento_composto(100, 2, 0.5)
    225.0

    >>> obter_montante_rendimento_composto(100, 2, 1.0)
    400.0
    """
    pass
