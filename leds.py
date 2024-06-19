#leds.setPixelColor(0, leds.Color(222, 247, 208));


from PIL import Image


def criar_arquivo_texto(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f'Arquivo "{nome_arquivo}" criado com sucesso.')



def rgb2hex(r, g, b):
    return f'#{r}, {g}, {b}'.format(r, g, b)


nomes_img = ['cloe_perdeu', 'cloe_piscar_final', 'cloe_piscar_meio', 'cloe_resposta', 'cloe_sorrindo']

for img in nomes_img:
    im = Image.open("imgs/"+img+".jpeg")
    file = open("txts/"+img+ ".txt", 'w')
    pixel = im.load()
    coluna, linha = im.size
    #coluna, linha = 16,11


    n = 0
    for j in range(linha):
        for i in range(coluna):
            r, g, b = pixel[i, j]
            string = rgb2hex(r, g, b)
            if j % 2:
                x = j*coluna + (coluna - i) - 1
            else:
                x = n
            file.write(string.replace("#", "leds.setPixelColor("+str(x)+",leds.Color(")+"));")
            #leds.setPixelColor(0, leds.Color(222, 247, 208));
            n += 1
        file.write("\n")
    file.close()