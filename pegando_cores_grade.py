import cv2
import numpy as np



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



def draw_grid(caminho_para_img, linhas, colunas, caminho_para_salvar):
    imagem = cv2.imread(caminho_para_img)

    if imagem is None:
        print(f"Erro ao carregar a imagem em {caminho_para_img}")
        return None, None

    altura, largura = imagem.shape[:2]

    quadrado_altura = altura // linhas
    quadrado_largura = largura // colunas

    cores_quadrados = np.zeros((linhas, colunas, 3), dtype=np.uint8)

    for i in range(colunas):
        for j in range(linhas):
            x1 = i * quadrado_largura
            y1 = j * quadrado_altura
            x2 = min((i + 1) * quadrado_largura, largura)
            y2 = min((j + 1) * quadrado_altura, altura)


            quadrado = imagem[y1:y2, x1:x2]


            cor_media = np.mean(quadrado, axis=(0, 1))


            cores_quadrados[j, i] = cor_media


            cv2.rectangle(imagem, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imwrite(caminho_para_salvar, imagem)
    print(f"Imagem com grade salva em: {caminho_para_salvar}")

    return imagem, cores_quadrados


caminho_para_img = r'.\imgs\cloe_perdeu.jpeg'
caminho_para_salvar = './imagem_com_grade.jpg'
linhas = 11
colunas = 16


nomes_img = ['cloe_perdeu', 'cloe_piscar_final', 'cloe_piscar_meio', 'cloe_resposta', 'cloe_sorrindo']

for img in nomes_img:
    caminho_para_img = fr'imgs\{img}.jpeg'
    caminha_para_salvar = f'./imgs_grade/{img}_com_grade.jpeg'


    imagem_com_grade, matriz_cores_quadrados = draw_grid(caminho_para_img, linhas, colunas, caminho_para_salvar)
    criar_arquivo_texto("./txts/" + img + ".txt", format_rgb_matriz(matriz_cores_quadrados))





