# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Findall (<(.*)Date>(.*?)</(.*)Date>)
    nuevo_texto = re.sub(r"(\s|\n)*", "", texto)
    regex = r"<(.*?Date.*?)>(.*?)</(.*?Date.*?)>"
    resultados = re.findall(regex, nuevo_texto)
    return str(len(resultados))


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
