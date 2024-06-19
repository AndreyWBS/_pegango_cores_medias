from PIL import Image, ImageStat
import math


def criar_arquivo_texto(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f'Arquivo "{nome_arquivo}" criado com sucesso.')


def format_rgb_matriz(matrix):
    contador = 0
    result = []
    for row in matrix:
        for rgb in row:
            r, g, b = rgb
            result.append(f"leds.setPixelColor({contador}, leds.Color({r}, {g}, {b}));")
            contador = contador+1
    return ' \n'.join(result)

def dividir_imagem_em_pixels(caminho_imagem, num_linhas, num_colunas):

    imagem = Image.open(caminho_imagem)

    largura, altura = imagem.size

    largura_celula = largura // num_colunas
    altura_celula = altura // num_linhas

    matriz_media_cores = []

    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):

            x0 = j * largura_celula
            y0 = i * altura_celula

            x1 = x0 + largura_celula
            y1 = y0 + altura_celula

            celula = imagem.crop((x0, y0, x1, y1))

            estatisticas = ImageStat.Stat(celula)
            media_cores = [math.ceil(valor) for valor in estatisticas.mean]  # Arredonda os valores para cima
            linha.append(media_cores)
        matriz_media_cores.append(linha)

    return matriz_media_cores

num_linhas = 11
num_colunas = 16
caminho_imagem = "./imgs/cloe_perdeu.jpeg"

print(dividir_imagem_em_pixels(caminho_imagem, num_linhas, num_colunas))

nomes_img = ['cloe_perdeu', 'cloe_piscar_final', 'cloe_piscar_meio', 'cloe_resposta', 'cloe_sorrindo']


for img in nomes_img:
    img_ = img + ".jpeg"
    caminho_imagem = "./imgs/" + img_
    print(f"Média das cores para {img_}:")
    matriz =     dividir_imagem_em_pixels(caminho_imagem, num_linhas, num_colunas)
    criar_arquivo_texto( "./txts/"+img+".txt",format_rgb_matriz(matriz)  )
    print()
