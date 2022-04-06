# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Normalizamos el documento
    texto_normal = re.sub(r"\n+\s*\n+", "\n", texto)
    texto_normal = re.sub(r"^\n", "", texto_normal)
    # Borramos los tags que solo contienen numeros
    texto_sin_numeros = re.sub(r' *<.*?>\s*\d*\.?\d*\s*</.*?>\s*\n', '', texto_normal, re.DOTALL)
    # Borramos los tags que quedan vacios
    texto_sin_tags = re.sub(r' *<.*?>\s*</.*?>\s*\n', '', texto_sin_numeros, re.DOTALL)
    return texto_sin_tags


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
