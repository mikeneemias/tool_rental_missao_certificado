import sqlite3
from datetime import datetime


class DataBase():
    def __init__(self, name="system.db"):
        self.name = name
        self.conecta()
        self.create_table_ferramentas()
        self.create_table_tecnicos()
        self.create_table_reservas()

        self.close_connection()

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()

        except:
            pass

    def create_table_ferramentas(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS ferramentas(
                    "CÓDIGO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "DESCRIÇÃO" TEXT NOT NULL,
                    "FABRICANTE" TEXT NOT NULL,
                    "VOLTAGEM" TEXT NOT NULL,
                    "PART_NUMBER" INTEGER NOT NULL,
                    "TAMANHO" TEXT NOT NULL,
                    "UN_MEDIDA" TEXT NOT NULL,
                    "TIPO" TEXT NOT NULL,
                    "MATERIAL" TEXT NOT NULL,
                    "TEMPO_MAX_RESERVA" INTEGER NOT NULL,
                    "DISPONÍVEL" TEXT NOT NULL
                );
            ''')
        except AttributeError:
            print("faça a conexão")

    def create_table_tecnicos(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS tecnicos(
                    "CÓDIGO" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    "NOME_COMPLETO" TEXT UNIQUE NOT NULL,
                    "CPF" INTEGER NOT NULL,
                    "TELEFONE" INTEGER NOT NULL,
                    "TURNO" TEXT NOT NULL,
                    "NOME_EQUIPE" TEXT NOT NULL                    
                );
            ''')
        except AttributeError:
            print("faça a conexão")

    def create_table_reservas(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservas(
                    "COD_FERRAMENTA" INTEGER NOT NULL,
                    "DESCRIÇÃO" TEXT NOT NULL,
                    "DATA_SOLIC" INTEGER,
                    "DATA_RETIRADA" DATE NOT NULL,
                    "PREVISÃO_DEVOL" TEXT,
                    "DATA_DEVOL" DATE,
                    "COD_TECNICO" TEXT NOT NULL,
                    "NOME_TECNICO" TEXT NOT NULL
                    
                );
            ''')
        except AttributeError:
            print("faça a conexão")

    def insert_ferramenta(self, descricao_ferramenta, fabricante, voltagem, part_num,
                          tamanho, un_medida, tipo, material, tempo_max_reserva):

        self.conecta()
        cursor = self.connection.cursor()
        cursor.execute(
            """INSERT INTO ferramentas (DESCRIÇÃO, FABRICANTE, VOLTAGEM, PART_NUMBER, TAMANHO, UN_MEDIDA, TIPO, 
            MATERIAL, TEMPO_MAX_RESERVA, DISPONÍVEL) VALUES (:DESCRIÇÃO, :FABRICANTE, :VOLTAGEM, :PART_NUMBER, 
            :TAMANHO, :UN_MEDIDA, :TIPO, :MATERIAL, :TEMPO_MAX_RESERVA, :DISPONÍVEL)""",
            {
                'DESCRIÇÃO': descricao_ferramenta,
                'FABRICANTE': fabricante,
                'VOLTAGEM': voltagem,
                'PART_NUMBER': part_num,
                'TAMANHO': tamanho,
                'UN_MEDIDA': un_medida,
                'TIPO': tipo,
                'MATERIAL': material,
                'TEMPO_MAX_RESERVA': tempo_max_reserva,
                'DISPONÍVEL': 'SIM'
            })
        self.connection.commit()
        cursor.close()
        self.close_connection()

    def insert_reserva(self, codigo, descricao, data_retirada, data_dev, cod_tec):

        self.conecta()
        cursor = self.connection.cursor()
        nome = cursor.execute("SELECT NOME_COMPLETO FROM tecnicos WHERE [CÓDIGO]=?",(cod_tec))
        nome = nome.fetchall()
        nome = nome[0][0]
        cursor.execute("INSERT INTO reservas (COD_FERRAMENTA, DESCRIÇÃO, DATA_SOLIC, DATA_RETIRADA, PREVISÃO_DEVOL,"
                       "COD_TECNICO, NOME_TECNICO) VALUES (:COD_FERRAMENTA, :DESCRIÇÃO, :DATA_SOLIC, :DATA_RETIRADA, "
                       ":PREVISÃO_DEVOL, :COD_TECNICO, :NOME_TECNICO)",
                        {
                           'COD_FERRAMENTA': codigo,
                           'DESCRIÇÃO': descricao,
                           'DATA_SOLIC': datetime.now(),
                           'DATA_RETIRADA': data_retirada,
                           'PREVISÃO_DEVOL': data_dev,
                           'COD_TECNICO': cod_tec,
                           'NOME_TECNICO': nome
                       }
                       )

        cursor.execute(f"UPDATE ferramentas SET DISPONÍVEL = 'NÃO' WHERE CÓDIGO = {codigo}")
        self.connection.commit()
        cursor.close()
        self.close_connection()

    def devolucao_ferramenta(self, code):
        cod = code
        data = datetime.now()
        self.conecta()
        cursor = self.connection.cursor()
        cursor.execute(f"UPDATE ferramentas SET DISPONÍVEL='SIM' WHERE CÓDIGO = {cod}", ())
        cursor.execute(f"UPDATE reservas SET DATA_DEVOL = CURRENT_TIMESTAMP WHERE COD_FERRAMENTA = {cod}")
        self.connection.commit()
        cursor.close()
        self.close_connection()
        return True

    def insert_tecnico(self, nome, cpf, telefone, turno, nome_equipe):

        self.conecta()
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tecnicos (NOME_COMPLETO, CPF, TELEFONE, TURNO, NOME_EQUIPE) VALUES ("
                       ":NOME_COMPLETO, :CPF, :TELEFONE, :TURNO, :NOME_EQUIPE)",
                       {
                           'NOME_COMPLETO': nome,
                           'CPF': cpf,
                           'TELEFONE': telefone,
                           'TURNO': turno,
                           'NOME_EQUIPE': nome_equipe
                       }
                       )
        self.connection.commit()
        cursor.close()
        self.close_connection()

    def get_code(self, cod):
        cod = cod
        cursor = self.connection.cursor()
        horas = cursor.execute(f"SELECT TEMPO_MAX_RESERVA FROM ferramentas WHERE CÓDIGO = {cod} ")
        horas = horas.fetchall()
        horas = horas[0][0]
        cursor.close()
        self.close_connection()
        return horas

    def check_disponibilidade(self, cod):
        cursor = self.connection.cursor()
        try:
            disp = cursor.execute(f"""SELECT DISPONÍVEL FROM ferramentas WHERE CÓDIGO = '{cod}'""")
            disp = disp.fetchall()
            disp = disp[0][0]
            cursor.close()
            self.close_connection()
            return disp
        except IndexError:
            return 'Código Inválido'

    def check_exclusao(self, cod, table):
        try:
            cursor = self.connection.cursor()
            check = cursor.execute(f"""SELECT CÓDIGO FROM {table} WHERE [CÓDIGO]=?""", (cod))
            check = check.fetchall()
            check = check[0][0]
            cursor.close()
            self.close_connection()
            print(check, cod)
            if cod != check:
                return True
        except IndexError:
            return True


if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_ferramentas()
    db.create_table_reservas()
    db.create_table_tecnicos()
    db.close_connection()
