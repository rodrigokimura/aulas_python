import json
import pytest
from  unittest.mock import mock_open, patch

from .storage import (
    converter_dicionario_de_dados_para_string_json,
    converter_string_json_para_dicionario,
    armazenar_dicionario_de_dados_como_arquivo_json,
    ler_arquivo_json_como_dicionario
)

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
      "country": "Exampleland"
      }
  }
  

@pytest.fixture
def json_dados_amostra():
  return '''{
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
}'''
  
  # teste = json.dumps(
  #   {
  #     "name": "John Doe",
  #     "age": 30,
  #     "city": "Example City",
  #     "isStudent": False,
  #     "grades": [85, 90, 78],
  #     "address": {
  #       "street": "123 Main Street",
  #       "zipCode": "12345",
  #       "country": "Exampleland"
  #     }
  #   },
  #   indent = 2)
  # print(teste)
  

def test_converter_dicionario_de_dados_para_string_json(dict_dados_amostra, json_dados_amostra):
  # assim fica no estilo triple a: arrange, act, assert
  resultado = converter_dicionario_de_dados_para_string_json(dict_dados_amostra)
                                                             
  assert resultado  == json_dados_amostra

def test_converter_string_json_para_dicionario(dict_dados_amostra, json_dados_amostra):
  
  resultado = converter_string_json_para_dicionario(json_dados_amostra)

  assert resultado == dict_dados_amostra

def test_armazenar_dicionario_de_dados_como_arquivo_json():
  
  with patch('builtins.open', mock_open()) as mock_file:
    filename = 'test.json'
    data = {'key': 'value'}

    armazenar_dicionario_de_dados_como_arquivo_json(data, filename)
    
    mock_file.assert_called_once_with(filename, 'w')
    mock_file().write.assert_called_once_with(json.dumps(data, indent=2))
  

def test_ler_arquivo_json_como_dicionario():
  # assert ler_arquivo_json_como_dicionario("teste.json") == dict_dados_amostra    
  pass