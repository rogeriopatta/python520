#!/usr/bin/python3

variavel = 3 # variavel no escopo global

def muda_variavel():
    #variavel = 2 # no escopo local
    global variavel # faz a variavel ser global e naõ local
    variavel = 2
    print('variavel')

muda_variavel()

print('variavel')