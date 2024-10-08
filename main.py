import os
import shutil
import tempfile
import zipfile

TEMP_DIR = tempfile.mkdtemp()
PROTHEUS_DIR = r'\\192.168.100.30\Instalaveis\smartclient 03.06\smartclient.zip'
DESTINATION_COPY_FILE = os.path.join(TEMP_DIR, 'smartclient.zip')
DESTINATION_FOLDER = r'C:\\'
TARGET_LINK_PATH = r'C:\smartclient\Protheus.lnk'
PUBLIC_DESKTOP_PATH = r'C:\Users\Public\Desktop\Protheus.lnk'


def copy_file_with_progress(source: str, destination: str):
    print("Copiando arquivo do servidor ...")
    # Tamanho total do arquivo
    total_size = os.path.getsize(source)
    copied_size = 0
    block_size = 1024 * 1024  # 1MB

    with open(source, 'rb') as fsrc, open(destination, 'wb') as fdst:
        while True:
            # Lê o arquivo em blocos
            buffer = fsrc.read(block_size)
            if not buffer:
                break
            # Escreve o bloco no arquivo de destino
            fdst.write(buffer)
            copied_size += len(buffer)
            # Calcula e exibe o progresso
            progress = (copied_size / total_size) * 100
            print(f'\rConcluído: {progress:.2f}% ({copied_size} de {total_size} bytes)', end='')

    print("\nCópia concluída!")


# Função para descompactar com progresso
def unzip_file_with_progress(zip_file: str, destination_dir: str):
    print("Iniciando descompactação do arquivo copiado ...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # Obtém a lista de todos os arquivos no .zip
        total_files = len(zip_ref.infolist())
        for idx, file in enumerate(zip_ref.infolist(), start=1):
            zip_ref.extract(file, destination_dir)
            # Calcula e exibe o progresso
            progress = (idx / total_files) * 100
            print(f'\rConcluído: {progress:.2f}% ({idx}/{total_files})', end='')

    print("\nDescompactação concluída!")


# Função para criar atalho na área de trabalho pública
def create_shortcut():
    shutil.move(TARGET_LINK_PATH, PUBLIC_DESKTOP_PATH)


if __name__ == '__main__':
    copy_file_with_progress(PROTHEUS_DIR, DESTINATION_COPY_FILE)
    unzip_file_with_progress(DESTINATION_COPY_FILE, DESTINATION_FOLDER)
    create_shortcut()
    print("Limpando arquivos desnecessários ...")
    os.remove(DESTINATION_COPY_FILE)
    print("Instalação realizada com sucesso!")
    input("Aperte ENTER para sair ...")
