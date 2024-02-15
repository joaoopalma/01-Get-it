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
    with open("templates/" + arquivo, 'r') as arquivo_json:
        texto = arquivo_json.read()
    
    return texto

def save_note(params):
    with open('data/notes.json', 'r') as notes_read:
        texto = notes_read.read()
        list = json.loads(texto)
        list.append(params)
        novo_json = json.dumps(list)

    with open('data/notes.json', 'w') as notes_arq:
        notes_arq.write(novo_json)

    
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        resposta = f'HTTP/1.1 {code} {reason}\n\n {body}'
    else:
        resposta = f'HTTP/1.1 {code} {reason}\n {headers}\n\n {body}'
    
    return resposta.encode()