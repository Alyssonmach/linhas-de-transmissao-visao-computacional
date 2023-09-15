import shutil, os, json
def copy_archives(source_path, images_files, destination_path):
    '''
    Copia arquivos de uma pasta para outra.

    Args:
        source_path (str) --> Caminho relativo da pasta fonte onde estão os arquivos.
        images_files (list) --> Lista com o nome das imagens contidas no diretório fonte.
        destination_path (str) --> Caminho relativo da paste onde os arquivos serão destinados.
    '''

    try:
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
    
        for image in images_files:
            source_ref = os.path.join(source_path, image)
            destination_ref = os.path.join(destination_path, image)
            shutil.copy(source_ref, destination_ref)
        
        print("Arquivos copiados com sucesso!")
    except Exception as e:
        print("Ocorreu um erro:", str(e))

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

    category_counts['imagePath'] = data['imagePath']

    return category_counts

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
    Adquirindo os IDs das imagens a partir do dicionário com os rótulos do STN-PLAD.

    Args:
        data (dict) --> dicionário com as informações de rotulagem do conjunto de imagem.
    
    Returns:
        count_ids (dict) --> dicionário vazio com as chaves de IDs das imagens.
    '''

    count_ids = dict()
    for info in data['images']:
        count_ids[info['id']] = list()
    
    return count_ids

def image_path_search(id_verify, data):
    '''
    Pesquisa na lista de dicionários o caminho relativo da imagem a partir do ID.

    Args:
        id_verify (int) --> id relativo para pesquisar a imagem na lista de dicionário.
        data (list) --> lista de dicionários para pesquisa.
    
    Returns:
        image_path (str) --> caminho relativo da imagem.
    '''

    for image_data in data['images']:
        if image_data['id'] == id_verify:
            return image_data['file_name']
