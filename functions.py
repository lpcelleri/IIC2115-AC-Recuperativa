# -*- coding: utf-8 -*-
"""
# Parte 1

Generamos el data
"""

data= [b'_/\xef\xb9\x8b\\_ \n(\xd2\x82`_\xc2\xb4)\n<,\xef\xb8\xbb\xe2\x95\xa6\xe2\x95\xa4\xe2\x94\x80 \xd2\x89 - -\n_/\xef\xb9\x8b\\_',
       b'(\xe2\x95\xad\xe0\xb2\xb0_\xe2\x8a\x99)',
       b'(\xc2\xa6\xea\x92\x89[\xe2\x96\x93\xe2\x96\x93]',
       b'\xef\xbc\xbc\xef\xbc\x88\xef\xbc\xbe\xe2\x96\xbd\xef\xbc\xbe\xef\xbc\x89\xef\xbc\x8f']

"""Intentamos decodificar la información"""

def modulo(numero):
  """
  Completar para que retorne número módulo 4 y no siempre 1
  Es decir: 0, 1, 2 o 3 según el número.
  """
  return 1

nombre = input("Ingresa tu nombre de usuario: ")

with open("output.txt", "w", encoding="UTF-8") as file:
  file.write(data[modulo(hash(nombre))].decode("UTF-8"))
