# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Sacamos todos los espacios y saltos de linea
    # Matchear Resolution
    # Matchear X e Y
    # Extraemos los numeros
    # Devolvemos el texto
    nuevo_texto = re.sub(r"(\s|\n)*", "", texto)
    regex_res = r"<Resolution>(.*)</Resolution>"
    resolution = re.search(regex_res, nuevo_texto).group(1)
    regex_x = r"<X>(\d+)</X>"
    x = re.search(regex_x, resolution).group(1)
    regex_y = r"<Y>(\d+)</Y>"
    y = re.search(regex_y, resolution).group(1)
    return f"Resolucion X: {x}\nResolucion Y: {y}"


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()
