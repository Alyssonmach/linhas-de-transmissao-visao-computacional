import json, os

def load_json_file(json_path):
    '''
    Carrega um arquivo json em um dicionário.

    Args:
        json_path (str) --> caminho relativo de acesso ao arquivo json no diretório.

    Returns:
        data (dict) --> dicionário contendo todas as informações do arquivo json.
    '''

    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    
    return data

def initialize_images_ids_with_dict(data):
    '''
    Adquirindo os IDs das imagens a partir do dicionário com os rótulos.

    Args:
        data (dict) --> dicionário com as informações de rotulagem do conjunto de imagem.
    
    Returns:
        count_ids (dict) --> dicionário vazio com as chaves de IDs das imagens.
    '''

    count_ids = dict()
    for info in data['images']:
        count_ids[info['id']] = list()
    
    return count_ids

def list_json_files(folder_path):
    '''
    Separa uma lista com o nome dos arquivos .json localizados em um diretório.
    
    Args:
        folder_path (str) --> caminho relativo do diretório a ser analisado.
    
    Returns:
        json_files (list) --> lista contendo o nome de todos os arquivos .json selecionados.
    
    '''

    json_files = []

    for file in os.listdir(folder_path):
        if file.endswith('.json'):
            json_files.append(file)
            
    return json_files

def extract_number(filename):
    '''
    Função utilitária para organizar a ordem alfabética dos arquivos .json salvos em uma lista.

    Args:
        filename (list) --> nome dos arquivos .json salvos na string.

    Returns:
        filename_sorted (list) --> string com o nome dos arquivos .json em ordem alfabética.
    '''

    start = filename.find('_') + 1
    end = filename.find('_', start)

    if end == -1: end = filename.find('.', start)
        
    return int(filename[start:end])

def count_categories(json_path):
    '''
    Conta a quantidade de objetos instanciados em um arquivo .json.

    Args:
        json_path (list) --> lista contendo o caminho relativo para acessar os arquivos .json.
    
    Returns:
        category_counts (dict) --> dicionário contendo a contagem de objetos instanciados na
                                   imagem.
    '''
    
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

    category_counts = dict()

    for shape in data['shapes']:
        category = shape['label']
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    return category_counts
