from io import StringIO
from textwrap import dedent
from unittest.mock import mock_open, patch

import pytest

from .storage import (
    armazenar_dicionario_de_dados_como_arquivo_json,
    converter_dicionario_de_dados_para_string_json,
    converter_string_json_para_dicionario,
    ler_arquivo_json_como_dicionario,
)


@pytest.fixture
def buffer():
    return StringIO()


@pytest.fixture
def dict_dados_amostra():
    yield {
        "name": "John Doe",
        "age": 30,
        "city": "Example City",
        "isStudent": False,
        "grades": [85, 90, 78],
        "address": {
            "street": "123 Main Street",
            "zipCode": "12345",
            "country": "Exampleland",
        },
    }


@pytest.fixture
def json_dados_amostra():
    return dedent(
        """\
        {
          "name": "John Doe",
          "age": 30,
          "city": "Example City",
          "isStudent": false,
          "grades": [
            85,
            90,
            78
          ],
          "address": {
            "street": "123 Main Street",
            "zipCode": "12345",
            "country": "Exampleland"
          }
        }"""
    )


def test_converter_dicionario_de_dados_para_string_json(
    dict_dados_amostra, json_dados_amostra
):
    # assim fica no estilo triple a: arrange, act, assert
    resultado = converter_dicionario_de_dados_para_string_json(dict_dados_amostra)

    assert isinstance(resultado, str)
    assert resultado == json_dados_amostra


def test_converter_string_json_para_dicionario(dict_dados_amostra, json_dados_amostra):

    resultado = converter_string_json_para_dicionario(json_dados_amostra)

    assert isinstance(resultado, dict)
    assert resultado == dict_dados_amostra


def test_armazenar_dicionario_de_dados_como_arquivo_json(
    tmp_path, dict_dados_amostra, json_dados_amostra
):
    # sobre a fixture tmp_path: https://docs.pytest.org/en/6.2.x/tmpdir.html

    conteudo_esperado = json_dados_amostra
    filename = tmp_path / "test.json"

    armazenar_dicionario_de_dados_como_arquivo_json(dict_dados_amostra, filename)

    with open(filename, "r") as file:
        conteudo_que_foi_escrito = file.read()

    assert conteudo_que_foi_escrito == conteudo_esperado


def test_armazenar_dicionario_de_dados_como_arquivo_json_de_outra_forma():
    m = mock_open()
    with patch("builtins.open", m):
        filename = "test.json"
        data = {"key": "value"}

        armazenar_dicionario_de_dados_como_arquivo_json(data, filename)

    handle = m()

    # TODO: precisamos fazer a asserção das chamadas
    print(handle.write.mock_calls)


def test_ler_arquivo_json_como_dicionario(
    tmp_path, dict_dados_amostra, json_dados_amostra
):
    with open(tmp_path / "asdf.json", "w") as file:
        file.write(json_dados_amostra)

    resultado = ler_arquivo_json_como_dicionario(tmp_path / "asdf.json")

    assert isinstance(resultado, dict)
    assert resultado == dict_dados_amostra
