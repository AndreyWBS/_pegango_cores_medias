import cv2
import numpy as np


def draw_grid(caminho_para_img, linhas, colunas, caminha_para_salvar):
    imagem = cv2.imread(caminho_para_img)

    if imagem is None:
        print(f"Erro ao carregar a imagem em {caminho_para_img}")
        return

    altura, largura = imagem.shape[:2]

    quadrado_altura = altura // linhas
    quadrado_largura = largura // colunas

    for i in range(1, colunas):
        x = i * quadrado_largura
        cv2.line(imagem, (x, 0), (x, altura), (0, 255, 0), 1)

    for i in range(1, linhas):
        y = i * quadrado_altura
        cv2.line(imagem, (0, y), (largura, y), (0, 255, 0), 1)

    cv2.imwrite(caminha_para_salvar, imagem)
    print(f"imagem com grade salva em: {caminha_para_salvar}")





linhas = 11
colunas = 16


nomes_img = ['cloe_perdeu', 'cloe_piscar_final', 'cloe_piscar_meio', 'cloe_resposta', 'cloe_sorrindo']

for img in nomes_img:
    caminho_para_img = fr'imgs\{img}.jpeg'
    caminha_para_salvar = f'./imgs_grade/{img}_com_grade.jpeg'
    draw_grid(caminho_para_img, linhas, colunas, caminha_para_salvar)
