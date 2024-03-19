import json
import os

dados_amostra = {
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

def converter_dicionario_de_dados_para_string_json(dados):
    return json.dumps(dados)

def converter_string_json_para_dicionario(dados):
    return json.loads(dados)

def armazenar_dicionario_de_dados_como_arquivo_json(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        json.dump(dados, file, indent=2)
   
    # with open(nome_arquivo, 'r') as file:
    #     json_carregado = json.load(file)
    #     if json_carregado == dados:
    #         return "Success"
    #     else:
    #         return "No success"

def ler_arquivo_json_como_dicionario(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return json.load(file)      

# if __name__ == "__main__":
#     dict_para_str_json = converter_dicionario_de_dados_para_string_json(dados_amostra)
#     str_json_para_dict = converter_string_json_para_dicionario(dict_para_str_json)
#     armazenar_dicionario_de_dados_como_arquivo_json(str_json_para_dict, "arquivo.json")
#     json_para_dict = ler_arquivo_json_como_dicionario("arquivo.json")
#     print(json_para_dict)

#     file_path = "arquivo.json"
#     if os.path.exists(file_path):
#         os.remove(file_path)
    