import os
import shutil

PROTHEUS_DIR = r'\\192.168.100.30\Instalaveis\smartclient 03.06\smartclient.zip'
DESTINATION_DIR = r'C:\Users\douglas.oliveira\Desktop\smartclient.zip'

def copy_file_with_progress(source: str, destination: str):
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
            print(f'\rProgresso: {progress:.2f}% ({copied_size} de {total_size} bytes)', end='')

    print("\nCópia concluída!")

# Chamar a função para copiar o arquivo
copy_file_with_progress(PROTHEUS_DIR, DESTINATION_DIR)
