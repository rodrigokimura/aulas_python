from .investimentos import (
    obter_montante_rendimento_composto,
    obter_montante_rendimento_simples,
)


def test_obter_montante_rendimento_simples():
    assert obter_montante_rendimento_simples(100, 1, 0.01) == 101


def test_obter_montante_rendimento_composto():
    assert obter_montante_rendimento_composto(100, 2, 0.5) == 225
