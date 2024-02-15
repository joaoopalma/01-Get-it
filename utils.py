import json

def extract_route(requisicao):
    rota = requisicao.split()[1][1:]

    return rota

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()
    
def load_data(arquivo):
    with open("data/" + arquivo, 'r') as arquivo_json:
        texto = arquivo_json.read()
        dicionario =json.loads(texto)
        
        return dicionario
    
def load_template(arquivo):
    with open("template/" + arquivo, 'r') as arquivo_json:
        texto = arquivo_json.read()
    
