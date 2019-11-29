#!/sudo/bin/env python3

import psycopg2  # modulo para conectar python ao postgre

try:

    con = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')

except Exception as e:

    print(e)
    exit()  # para a execução no caso de erro

cur = con.cursor()

try:

    cur.execute("INSERT into scripts(nome,conteudo) values('juliana','analista')")
    con.commit()

except Exception as e:
    con.rollback()
    print(e)

finally:
    cur.close()
    con.close()





