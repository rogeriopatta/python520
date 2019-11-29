

#!/usr/bin/env python3

#programa para interfaceamento entre o python e o SQL

import psycopg2
import MySQLdb

from orm import Banco

try:
    #conexao postgres
    con_psql = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con_psql.cursor()

    banco_psql = Banco(con_psql,cur)

    #conexao com mysql
    con_mysql = MySQLdb.connect(host='127.0.0.1',db='scripts',
                                user='developer',passwd='4linux')

    cur_mysql = con_mysql.cursor()
    banco_mysql = Banco(con_mysql,cur_mysql)

except Exception as e:
    print(e)
    exit()

try:
    # print(banco_psql.seleciona_todos('s'))
    # print(banco_psql.seleciona_primeiro('s'))
    #banco_psql.delete('s','nome','Daniel')
    #print(banco_psql.seleciona_todos('s'))
    banco_mysql.inserir('daniel','programador python')
    print(banco_mysql.seleciona_todos())
    

except Exception as e:
    con_psql.rollback()
    con_mysql.rollback()
    print(e)