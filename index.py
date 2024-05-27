import sqlite3 as sql
from sqlite3 import Error


def criar_conexao_bd(caminho):
    conexao = None
    try:
        conexao = sql.connect(caminho)
        print("Conexão estabelecida com sucesso ao bd")
    except Error:
        print(f"Erro: {Error}")
    return conexao


bd = criar_conexao_bd("teste.db")


def executar_comando(conexao, comando, valores):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando, valores)
        conexao.commit()
        print("Comando feito com sucesso")
    except Error:
        print(f"Erro: {Error}")


def inserir_aluno(conexao):
    cursor = conexao.cursor()
    nome = input("Qual o nome do aluno: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")
    valores = (nome, data_nascimento, cpf)

    sql_inserir_aluno = """
    INSERT INTO Aluno(id, nome, data_nascimento, cpf) VALUES
    (2, ?, ?, ?)
    """
    cursor.execute(sql_inserir_aluno, valores)
    conexao.commit()


inserir_aluno(bd)
