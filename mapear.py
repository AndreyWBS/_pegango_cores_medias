import os

def mapear_pasta(caminho):
    arquivos_ = []
    for raiz, diretorios, arquivos in os.walk(caminho):
        print(f'Raiz: {raiz}')
        for diretorio in diretorios:
            print(f'Diretório: {diretorio}')
        for arquivo in arquivos:
            print(f'Arquivo: {arquivo}')
            arquivos_.append(arquivo)
        print()
    print(arquivos_)


caminho_da_pasta = r".\imgs"
mapear_pasta(caminho_da_pasta)
