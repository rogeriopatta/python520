#!/usr/bin/python3

class Banco():
    def __init__(self,conexao,cursor):
        try:
            self.conexao = conexao
            self.cursor = cursor
        except Exception as e:
            raise Exception(e)

    
    def __del__(self):
        self.cursor.close()
        self.conexao.close()

    #crian CRUDE - Create, Read, Update, Delete, 
    def inserir(self,nome,conteudo):
        self.cursor.execute(f"INSERT INTO scripts(nome,conteudo) VALUES('{nome}','{conteudo}')")
        self.conexao.commit()
        print('inserido com sucesso')
    
    
    
    def atualizar(self,tabela,coluna,valor,coluna_old,valor_old):
        self.cursor.execute(f"UPDATE {tabela} SET {coluna} = {valor} WHERE {coluna_old} = {valor_old}")
        self.conexao.commit()
        print('atualizado com sucesso')

    def delete(self,tabela,coluna,valor):
        self.cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = '{valor}'")
        self.conexao.commit()
        print('deletado com sucesso')

    def seleciona_todos(self):
        self.cursor.execute("SELECT * FROM scripts")
        return self.cursor.fetchall()
        
    def seleciona_primeiro(self):
        self.cursor.execute("SELECT * FROM scripts")
        return self.cursor.fetchone()        