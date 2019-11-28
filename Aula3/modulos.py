# #!/usr/bin/python3

# import modulos.calculadora as calculadora

# from modulos.calculadora import somar  # ou * no final para todas as funções
# from modulos.calculadora import multiplica


# soma = calculadora.somar(1,3)

# divide = calculadora.divide(144,12)

# print(soma)

# print(divide)

# soma = somar(4,6) # com uso do from 

# print(soma)
# print(multiplica(40,22))

# import random  # modulo de randomicos

# print(random.randint(1,90))

# import os        # permite funcionalidades do sistema operacional
#import sys         # acessar variaveis do sistema e alguns parametro especificos
#import datetime     # data e hora
#import json         # codifica e ou arquivo no formato JSON
import csv      # trabalha com planilhas


# o.s

#print(os.listdir('/home/developer')) # lista pastas do diretorio

#print(os.rename('nomeerrado.txt','nomecerto.txt')) # troca nome de arquivo

# os.system('ls')
# os.system('sudo systemctl restar apache2') # restar serviço apache2 , necessario dar sudo no prompt

#print(sys.plataform)

# print(sys.builtin_module_names)
# print(sys.argv)
# print(sys.exit)
# print('hello')

#datetime

# print(datetime.datetime.now())

# #print(datetime.datedelta(7))
# print(datetime.time(14,0,0))

# print(datetime.date(2019,5,4))

##exemplo pratico - verifica o tempo de utilização de um tokem que nao deve ultrapasasar uma hora

# acesso = datetime.datetime(2019,1,22,00,00,00)
# atual = datetime.datetime(2019,1,22,1,1,0)

# if(atual - acesso).total_seconds() > 3600:
#     print('seu tokem expirou')
# else:
#     print('acesso liberado')

# json
#print(json.dumps({"nome":"daniel","sobrenome":"silva"}))

print(json.loads('{"nome":"daniel","sobrenome":"silva"}'))







