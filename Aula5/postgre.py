#!/usr/bin/env python3

import psycopg2

from orm import Banco


try:

    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()
    banco = Banco(con,cur)

except Exception as e:
    print(e)
    exit()


try:

    banco.inserir('juliana','analista')

    print(banco.seleciona_todos())
    #print(p)

    #print(banco.seleciona_primeiro())


except Exception as e:
    con.rollback()
    print(e)

