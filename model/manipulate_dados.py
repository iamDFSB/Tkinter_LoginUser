import sqlite3
from sqlite3 import Error
import os

class Integre_Banco:
    def __init__(self, nome: str, telefone: str, email: str, description: str) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.description = description

    def __conectar_banco():
        caminho = r"C:\Users\daniel.sbatista\Documents\Estudo\Projetos_Python\Aprendendo Python\tkinter_project\Banco\Banco_projeto"
        try:
            conn = sqlite3.connect(caminho)
            print("Conexão feita com sucesso")
        except Error as er:
            print("Erro na conexão")
            print(er)
        return conn

    deletar_dados = """
        DELETE FROM tb_login_user WHERE 
    """

    atualizar_dados = """
        UPDATE tb_login_user
        SET 
        WHERE
    """

    connection = __conectar_banco()

    def criar_banco(self):
        criar_tabela = """
            CREATE TABLE tb_login_user(
                N_ID_USER INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOME VARCHAR(30),
                T_TELEFONE VARCHAR(14),
                T_EMAIL VARCHAR(30),
                T_DESCRIPTION VARCHAR(100)
            );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(criar_tabela)
            cursor.fetchone()
            print("Criação de banco, feita com sucesso")
        except Error as er:
            print("Erro na criação do banco")
            print(er)

    def deletar_banco(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            print("Excluir dado com sucesso")
        except Error as er:
            print("Erro ao deletar algo no banco")
            print(er)

    def consultar_banco(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            response = cursor.fetchall()
            print("Consulta feita com sucesso")
            return response
        except Error as er:
            print("Erro na consulta do banco")
            print(er)

    def atualizar_banco(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            print("Atualização feita com sucesso")
        except Error as er:
            print("Erro na atualização do banco")
            print(er)

    def inserir_no_banco(self):
        inserir_dados = ("""
            INSERT INTO tb_login_user
            (T_NOME, T_TELEFONE, T_EMAIL, T_DESCRIPTION)
            VALUES('"""+self.nome+ """','"""+self.telefone+"""','"""+self.email+"""','"""+self.description+"""')
        """)

        try:
            cursor = self.connection.cursor()
            cursor.execute(inserir_dados)
            self.connection.commit()
            print("Inserção feita com sucesso")
        except Error as er:
            print("Erro na inserção no banco")
            print(er)


# objeto_banco.criar_banco(sql=criar_tabela)
