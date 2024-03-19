import json


def converter_dicionario_de_dados_para_string_json(dados):
    return json.dumps(dados, indent=2)


def converter_string_json_para_dicionario(dados):
    return json.loads(dados)


def armazenar_dicionario_de_dados_como_arquivo_json(dados, nome_arquivo):
    with open(nome_arquivo, "w") as file:
        json.dump(dados, file, indent=2)


def ler_arquivo_json_como_dicionario(nome_arquivo):
    with open(nome_arquivo, "r") as file:
        return json.load(file)

