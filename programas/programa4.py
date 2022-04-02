# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Sacar todas url que terminen en .uy
    # Obtenemos todas las urls que quedan
    # Armamos el string a devolver
    nuevo_texto = re.sub(r'(http|https).*?\.uy', '', texto)
    regex_links = r"<(.*?)>.*?\s((http|https).*?)\s</.*?>"
    resultados = re.findall(regex_links, nuevo_texto)
    string = ""
    for resultado in resultados:
        string += f"{resultado[0]} -- {resultado[1]}\n"
    return string[:-1]


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
