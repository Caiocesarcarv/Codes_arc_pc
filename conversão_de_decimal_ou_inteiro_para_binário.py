#Código de conversão de inteiro para binário
import math as m
numero_inteiro = float(input("Digite número qualquer, seja decimal ou inteiro: "))
inter = int(numero_inteiro)
bruto = numero_inteiro - inter
if bruto <= 0.5:
  conv = m.floor(numero_inteiro)
  numero_binario = bin(conv)
  print(f"numero arredondado para {conv}")
  print(numero_binario)
  numero_binario = bin(conv)[2:]
  print(numero_binario)
else:
  conv2 = m.ceil(numero_inteiro)
  numero_binario2 = bin(conv2)
  print(f"numero arredondado para {conv2}")
  print(numero_binario2)
  numero_binario2 = bin(conv2)[2:]
  print(numero_binario2)
