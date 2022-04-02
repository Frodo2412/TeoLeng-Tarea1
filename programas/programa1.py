# -*- coding: utf-8 -*-
import re
import sys


def programa(texto):
    # Encontrar la expresion <FileModifiedDate> DateTime </FileModifiedDate>
    # Sustituir los opening y closing tags con ""
    # Parsear el DateTime y devolver la expresion que piden
    # DateTime Format: YYYY-MM-DDThh:mm:ss.sssZ
    regex = r"<FileModifyDate>\s*(.*?)\s*</FileModifyDate>"
    resultado = re.search(regex, texto)
    fechahora = resultado.group(1).split("T")  # [0] = YYYY-MM-DD, [1] = hh:mm:ss.sssZ
    fecha = fechahora[0]
    hora = fechahora[1].split(":")  # [0] = hh, [1] = mm, [2] = ss.sssZ
    return f"{hora[0]}:{hora[1]} del {fecha}"


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
