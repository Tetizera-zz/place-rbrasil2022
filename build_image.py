import sys
from pathlib import Path

from PIL import Image
import numpy as np


#
# Como usar:
#  python build_image.py
#
# Saida:
#  image.png - overlay para o userscript
#  composited.png - imagem menor, para ver o resultado
#

# Listar os componentes da imagem aqui.
# Primeiro as do "fundo" e depois as da "frente"
sprites = [
    (910,  567, "borda"),
    (911,  568, "bandeira"),

    (910,  567, "arara"),
    (1073, 571, "cristo"),
    (1104, 606, "coxinha"),
    (1097, 601, "lua"),
    (1108, 567, "maracana"),
    (1154, 597, "turma_da_monica"),
    (1215, 567, "51"),
]

# Criar a imagem, a partir das partes
def composite():
    canvas = Image.new('RGBA', (2000,1000), (0,0,0,0))
    for (x,y,name) in sprites:
        path = "sprites/" + name + ".png"
        img = Image.open(path).convert('RGBA')  # make sure image is RGBA
        canvas.paste(img, (x,y), img)    
    return canvas

# Gerar a versão final com pontinhos
def explode(img):
    img_3x = img.resize((img.width * 3, img.height * 3), Image.NEAREST)
    img_3x_arr = np.array(img_3x)

    for i in range(img_3x_arr.shape[0]):
        if i % 3 == 0 or (i - 2) % 3 == 0:
            img_3x_arr[i, :, 3] = 0
    for i in range(img_3x_arr.shape[1]):
        if i % 3 == 0 or (i - 2) % 3 == 0:
            img_3x_arr[:, i, 3] = 0

    img_3x_back = Image.fromarray(img_3x_arr)
    return img_3x_back


# Vamos lá!
img = composite()

crop = img.crop((910, 567, 1290, 619))
crop.save('composited.png')

img_3x = explode(img)
img_3x.save('image.png')
