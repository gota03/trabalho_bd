import mysql.connector as sql
from mysql.connector import Error


def criar_conexao_bd(host_name, user_name, user_pswd):
    conexao = None
    try:
        conexao = sql.connect(
                host=host_name,
                user=user_name,
                passwd=user_pswd
        )
        print("Conexão com banco de dados feita com sucesso")
    except Error:
        print(f"Erro: {Error}")

    return conexao


def criar_database(conexao):
    sql_criar_database = """
        CREATE DATABASE Tradicional_Public_Schools;
    """
    cursor = conexao.cursor()
    try:
        cursor.execute(sql_criar_database)
        print("Database criada com sucesso")
    except Error:
        print(f"Erro: {Error}")


def usar_database(conexao):
    sql_usar_database = """
            USE Tradicional_Public_Schools;
        """
    cursor = conexao.cursor()
    try:
        cursor.execute(sql_usar_database)
        print("Database usada com sucesso")
    except Error:
        print(f"Erro: {Error}")


def executar_comando(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
        conexao.commit()
        print("Comando feito com sucesso")
    except Error:
        print(f"Erro: {Error}")


sql_criar_tabela_usuario = """
    CREATE TABLE Usuario(
        id int primary key auto_increment,
        nome varchar(100),
        tipo_usuario varchar(30),
        data_nascimento date,
        cpf varchar(11)
        );
"""

sql_inserir_usuario = """
    INSERT INTO Usuario (nome, tipo_usuario, data_nascimento, cpf) VALUES
    (%s, %s, %s, %s);
"""
valores = ("mateus", "admin", "2002/11/23", "123")

conexao_bd = criar_conexao_bd("localhost", "root", "Gote03/18")
usar_database(conexao_bd)
cursor = conexao_bd.cursor()
cursor.execute(sql_inserir_usuario, valores)
conexao_bd.commit()

# executar_comando(conexao_bd, sql_inserir_usuario)
