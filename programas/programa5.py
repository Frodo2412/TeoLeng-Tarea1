# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Removemos todos los tags que contengan solo numeros (<.*?>\d*</.*?>)
    # Removemos todos los tags que se cierran consigo mismos (<.*?></.*?>)
    texto_normal = re.sub(r"\n+", "\n", texto)
    texto_sin_numeros = re.sub(r' *<.*?>\s*\d*\.?\d*\s*</.*?>\s*\n', '', texto_normal, re.DOTALL)
    print(texto_sin_numeros)
    texto_sin_tags = re.sub(r' *<.*?>([\s\n])*</.*?>\n', '', texto_sin_numeros, re.DOTALL)
    print(texto_sin_tags)
    texto_sin_doble_salto_linea = re.sub(r'\n+\s*\n+', '\n', texto_sin_tags)
    texto_sin_salto_de_linea_al_comienzo = re.sub(r'^\s*\n', '', texto_sin_doble_salto_linea)
    # print(texto_sin_salto_de_linea_al_comienzo)
    return texto_sin_salto_de_linea_al_comienzo


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
