from PySide2.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget)
from ui_main import Ui_MainWindow
from ui_excluir_tec import Ui_WinDelTEc
from ui_excluir_fer import Ui_WinDelFerramenta
from ui_devol import Ui_WinDevol
import sys
from database import DataBase
import sqlite3
import pandas as pd
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Missão Certificado DEV Team 15')
        db = DataBase()
        self.table_ferramentas()
        self.table_tecnicos()
        self.table_reservas()

        # -------------------Páginas do sistema----------------
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_tabelas))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_nova_reserva.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_nova_reserva))
        self.btn_nova_ferramenta.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_ferramentas))
        self.btn_novo_tecnico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_tecnicos))
        self.btn_voltar_reserva.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_tabelas))
        self.btn_voltar_tecnico.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_tabelas))
        self.btn_voltar_ferramenta.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_tabelas))
        # ------------------------Botões de função-------------------
        self.btn_cadastrar_ferramenta.clicked.connect(lambda: self.nova_ferramenta())
        self.btn_cadastrar_tecnico.clicked.connect(lambda: self.novo_tecnico())
        self.btn_reservar_feramenta.clicked.connect(lambda: self.nova_reserva())
        self.btn_exportar_ferramenta.clicked.connect(lambda: self.exportar_excel('ferramentas'))
        self.btn_exportar_reservas.clicked.connect(lambda: self.exportar_excel('reservas'))
        self.btn_exportar_tecnicos.clicked.connect(lambda: self.exportar_excel('tecnicos'))
        self.btn_excluir_ferramenta.clicked.connect(lambda: self.tela_excluir_ferramenta())
        self.btn_excluir_tecnico.clicked.connect(lambda: self.tela_excluir_cadastro())
        self.btn_finalizar_reserva.clicked.connect(lambda: self.tela_devolucao())
        self.txt_data_retirada.dateTimeChanged.connect(lambda: self.update_data())
        self.txt_data_dev.dateTimeChanged.connect(lambda: self.update_data())
        self.txt_codigo.editingFinished.connect(lambda: self.ver_disp_ferramenta())

    def nova_ferramenta(self):
        descricao_ferramenta = self.txt_descricao.text()
        fabricante = self.txt_fabricante.text()
        voltagem = self.txt_voltagem.text()
        part_num = int(self.txt_part_numb.text())
        tamanho = self.txt_tamanho.text()
        un_medida = self.txt_un_medida.text()
        tipo = self.txt_tipo.text()
        material = self.txt_material.text()
        tempo_max_reserva = int(self.txt_horas.text())

        db = DataBase()
        db.conecta()

        db.insert_ferramenta(descricao_ferramenta, fabricante, voltagem, part_num,
                             tamanho, un_medida, tipo, material, tempo_max_reserva)

        db.close_connection()
        msg = QMessageBox()
        msg.setWindowTitle("Cadastro Realizado")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec_()

        self.txt_descricao.setText("")
        self.txt_fabricante.setText("")
        self.txt_voltagem.setText("")
        self.txt_part_numb.setText("")
        self.txt_tamanho.setText("")
        self.txt_un_medida.setText("")
        self.txt_tipo.setText("")
        self.txt_material.setText("")
        self.txt_horas.setText("")
        self.table_ferramentas()

    def novo_tecnico(self):
        nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        telefone = self.txt_telefone.text()
        turno = self.txt_turno.currentText()
        nome_equipe = self.txt_nome_equipe.text()

        validacao = self.validar_cpf(cpf)

        if validacao:

            db = DataBase()
            db.conecta()

            db.insert_tecnico(nome, cpf, telefone, turno, nome_equipe)

            self.txt_nome.setText("")
            self.txt_cpf.setText("")
            self.txt_telefone.setText("")
            self.txt_turno.setCurrentText("")
            self.txt_nome_equipe.setText("")

            db.close_connection()
            msg = QMessageBox()
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro realizado com sucesso!")
            msg.exec_()
            self.table_tecnicos()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("CPF Inválido")
            msg.setText("Insira um CPF válido!")
            msg.exec_()

    def nova_reserva(self):
        data_retirada = self.txt_data_retirada.text()
        codigo_ferramenta = self.txt_codigo.text()
        descricao_reserva = self.txt_solicitacao.text()
        data_devolucao = self.txt_data_dev.text()
        cod_tecnico = self.txt_cod_tecnico_reserva.text()

        db = DataBase()
        db.conecta()

        if not db.check_exclusao(cod_tecnico, 'tecnicos'):
            msg = QMessageBox()
            msg.setWindowTitle("Técnico não encontrado")
            msg.setText("Técnico não encontrado!")
            msg.exec_()

            self.txt_cod_tecnico_reserva.setText("")
        else:
            db.insert_reserva(codigo_ferramenta, descricao_reserva, data_retirada, data_devolucao, cod_tecnico)

            db.close_connection()
            msg = QMessageBox()
            msg.setWindowTitle("Reserva Realizada")
            msg.setText("Reserva realizada com sucesso!")
            msg.exec_()
            self.table_reservas()

    def table_ferramentas(self):
        self.tabela_ferramentas.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tabela_ferramentas.setModel(self.model)
        self.model.setTable("ferramentas")
        self.model.select()

    def table_tecnicos(self):
        self.tabela_tecnicos.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tabela_tecnicos.setModel(self.model)
        self.model.setTable("tecnicos")
        self.model.select()

    def table_reservas(self):
        self.tabela_reservas.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;")

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tabela_reservas.setModel(self.model)
        self.model.setTable("reservas")
        self.model.select()

    def validar_cpf(self, cpf):

        cpf1 = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf1 or len(cpf1) < 11 or len(set(cpf1)) == 1:
            return False

        antigo = [int(d) for d in cpf1]

        # Gera CPF com novos dígitos verificadores e compara com CPF informado
        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return True

        return False

    def exportar_excel(self, name):
        cnx = sqlite3.connect('system.db')
        tabela = name.lower()

        result = pd.read_sql_query(f"SELECT * FROM {tabela}", cnx)
        sheet_name = tabela.capitalize()
        result.to_excel(f"Resumo de {tabela}.xlsx", sheet_name=sheet_name, index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exportar Relatório")
        msg.setText("Relatório Exportado com Sucesso")
        msg.exec_()

    def update_data(self):
        cod = int(self.txt_codigo.text())
        dt = self.txt_data_retirada.dateTime()

        db = DataBase()
        db.conecta()
        cod = db.get_code(cod)
        add = (cod * 60) * 60
        dt = dt.addSecs(add)
        self.txt_data_dev.setDateTime(dt)
        db.close_connection()

    def ver_disp_ferramenta(self):
        cod = int(self.txt_codigo.text())

        db = DataBase()
        db.conecta()
        disp = db.check_disponibilidade(cod)
        if disp == 'NÃO':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ferramenta Indisponível")
            msg.setText("Ferramenta Indisponível")
            msg.exec_()
        elif disp == 'Código Inválido':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Código Inválido")
            msg.setText("Ferramenta não cadastrada")
            msg.exec_()
            self.txt_codigo.setText("")

        else:
            pass

    def tela_excluir_ferramenta(self):
        self.w = WindDelFerramenta()
        self.w.show()

    def tela_excluir_cadastro(self):
        self.w = WinDelTec()
        self.w.show()

    def tela_devolucao(self):
        self.w = WinDevol()
        self.w.show()


class WindDelFerramenta(QWidget, Ui_WinDelFerramenta):
    def __init__(self) -> None:
        super(WindDelFerramenta, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Deletar Ferramenta")

        self.btn_excluir_ferr.clicked.connect(lambda: self.deletar_ferramenta())
        self.btn_voltar_exc_ferr.clicked.connect(lambda: self.close())

    def deletar_ferramenta(self):
        cod = self.txt_cod_excluir_ferr.text()
        db = DataBase()
        db.conecta()
        disp = db.check_disponibilidade(cod)
        if disp == 'NÃO':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Ferramenta Indisponível")
            msg.setText("Ferramenta não pode ser excluida!")
            msg.exec_()
            return
        else:
            db = DataBase()
            db.conecta()
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM ferramentas WHERE [CÓDIGO]=?", (cod))
            db.connection.commit()
            if db.check_exclusao(cod, 'ferramentas'):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Ferramenta Excluída")
                msg.setText("Ferramenta Excluída com Sucesso")
                msg.exec_()
                self.txt_cod_excluir_ferr.setText('')

            cursor.close()


class WinDelTec(QWidget, Ui_WinDelTEc):
    def __init__(self) -> None:
        super(WinDelTec, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Deletar Técnico')

        self.btn_excluir_tec.clicked.connect(lambda: self.deletar_cadastro())
        self.btn_voltar_exc_tec.clicked.connect(lambda: self.close())

    def deletar_cadastro(self):
        cod = self.txt_cod_excluir.text()
        db = DataBase()
        db.conecta()
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM tecnicos WHERE [CÓDIGO]=?", (cod))
        db.connection.commit()
        if db.check_exclusao(cod, 'tecnicos'):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Excluído")
            msg.setText("Cadastro Excluído com Sucesso")
            msg.exec_()
            self.txt_cod_excluir.setText('')
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Cadastro não excluído")
            msg.setText("Cadastro não pode ser excluído")
            msg.exec_()
            self.txt_cod_excluir.setText("")


class WinDevol(QWidget, Ui_WinDevol):
    def __init__(self) -> None:
        super(WinDevol, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Devolver Ferramenta')

        self.btn_devolv.clicked.connect(lambda: self.entregar_ferramenta())
        self.btn_voltar_devolv.clicked.connect(lambda: self.close())

    def entregar_ferramenta(self):
        code = self.txt_cod_devol.text()
        db = DataBase()
        db.conecta()
        if db.devolucao_ferramenta(code):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Devolver Ferramenta")
            msg.setText("Ferramenta Devolvida")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Devolver Ferramenta")
            msg.setText("Algo deu Errado!")
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
