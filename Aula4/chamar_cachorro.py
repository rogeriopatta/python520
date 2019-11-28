#!/usr/bin/env python3

# from Cachorro import Cachorro
import Cachorro
# nome, idade, cor, raca='Vira-lata', porte='Médio'

dados_do_cachorro = {
    'nome':'Totó',
    'idade':8,
    'cor':'Branco',
    'raca':'Poodle',
    'porte':'Pequeno'
}
dados_do_cachorro2 = {
    'nome':'Rex',
    'idade':12,
    'cor':'Caramelo',
    'raca':'Vira-lata',
    'porte':'Medio'
}
toto = Cachorro.Cachorro(**dados_do_cachorro)
toto.latir()
print(toto.lingua)
toto.lingua = False
toto.latir()
rex = Cachorro.Cachorro(**dados_do_cachorro2)
rex.latir()
input()


