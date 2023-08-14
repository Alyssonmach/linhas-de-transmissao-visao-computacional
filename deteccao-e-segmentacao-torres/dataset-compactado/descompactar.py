import zipfile
import os

def unzip_file(zip_path, extract_to):
    '''
    Descompacta um arquivo .zip em uma pasta específica.

    Args:
        zip_path (str) --> Caminho relativo de localização do arquivo .zip.
        extract_to (str) --> Caminho relation do local de destino dos arquivos descompactados. 
    '''

    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print(f'Arquivo {zip_path}.zip descompactado com sucesso!')

    return 