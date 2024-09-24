from PIL import Image
import numpy as np
from numpy import asarray

def from_image(name:str) -> list:
    image = Image.open(name)
    return asarray(image)

def to_image(a: list, name: str) -> None:
    array = np.array(a)
    image = Image.fromarray(array,'RGB')
    image.save(name)

def closest(old: int) -> int:
    return (old//10) *10


def dither (array_v2: list) -> list:
    rows = len(array_v2)
    columns = len(array_v2[0])
    colors = 3

    array = []
    for r in range(rows):
        row = []
        for c in range(columns):
            color = []
            for i in range(colors):
                color.append(array_v2[r][c][i])
            row.append(color)
        array.append(row)
    new_array = [[0]]


    for r in range(rows):
        for c in range(columns):
            for i in range(colors):
                old = array[r][c][i]
                new = closest(old)
                array[r][c][i] = new
                error = old-new
                array[r][c+1][i] += error *7/16
                array[r+1][c-1][i] += error *3/16
                array[r+1][c][i] += error *5/16
                array[r+1][c+1][i] += error *1/16
            return array
image = from_image("Dithering_example_undithered_web_palette.jpg")
image = dither(image)
to_image(image,"cat.png")