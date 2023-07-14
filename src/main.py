import time
from sqlite.dados import Database
from sqlite.configPG import ConfigPG
from conn.psqlConn import Postgres
from conn.sqlQuery import QueryMaker
from common.sgm import Method as Sgm
from common.converter import Converter
from common.exportar import Exportar
from dotenv import dotenv_values

# 
# dbi = database interna
# cur = cursor do banco interno

#### CONFIGURAÇÃO ####
config = dotenv_values(".config") 

dbi = Database(config['DATABASE_INT'])
dbi.connect()
# dbi.conn.execute("PRAGMA key='" + config['KEY'] + "'")
cur = dbi.cursor()

pg = ConfigPG()
pg.createTables(cur)
pg.insertConfig(cur)
dbi.commit()

sgm = Sgm()
sgm.createTables(cur) #Create tables 

qm = QueryMaker()

# Connect to the client database
db = Postgres(
    database=config['DATABASE_CLIENT'],
)
db.connect()
cursor = db.cursor()

cvt = Converter(cursor, qm, sgm, dbi, cur)
exp = Exportar(dbi, sgm)
#### FIM CONFIGURAÇÃO ####

def exibirMenu(opcoes, titulo="Menu"):
    while True:
        print('\n', 10*'=', ' ', titulo, ' ', 10*'=')
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i}. {opcao[0]}")

        escolha = input("Escolha uma opção: ")

        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(opcoes):
            print("Opção inválida. Tente novamente.\n")
            continue

        opcaoSelecionada = opcoes[int(escolha) - 1]

        if callable(opcaoSelecionada[1]):
            opcaoSelecionada[1]()  # Chama a função associada à opção
        else:
            exibirMenu(opcaoSelecionada[1])  # Exibe o submenu

def executeCVT(fun, table=''):
    print(3*'\n', 'Iniciando conversão... ', table)
    start = time.time()
    fun()
    end = time.time()
    print('Tempo de execução: {:.2f} segundos'.format(end - start))
    time.sleep(1)

def completoCVT():
    executeCVT(cvt.clientes, 'Clientes')
    executeCVT(cvt.produtos, 'Produtos')
    executeCVT(cvt.produtosBarras, 'Produtos Barras')
    executeCVT(cvt.tributos, 'Tributos')
    executeCVT(cvt.fornecedores, 'Fornecedores')
    executeCVT(cvt.tanques, 'Tanques')
    executeCVT(cvt.bombas, 'Bombas')    
    executeCVT(cvt.grupos, 'Grupos')
    executeCVT(cvt.funcionarios, 'Funcionarios')
    executeCVT(cvt.frota, 'Frota')

def clientesCVT():
    executeCVT(cvt.clientes)

def produtosCVT():
    executeCVT(cvt.produtos)
    executeCVT(cvt.produtosBarras)
    executeCVT(cvt.tributos)

def fornecedoresCVT():
    executeCVT(cvt.fornecedores)

def mapaPistaCVT():
    executeCVT(cvt.tanques)
    executeCVT(cvt.bombas)

def gruposCVT():
    executeCVT(cvt.grupos)

def funcionariosCVT():
    executeCVT(cvt.funcionarios)

def frotaCVT():
    executeCVT(cvt.frota)

def conversao():
    subopcoes = [
        ("Clientes", clientesCVT),
        ("Produtos", produtosCVT),
        ("Fornecedores", fornecedoresCVT),
        ("Mapa de pista", mapaPistaCVT),
        ("Grupos", gruposCVT),
        ("Funcionarios", funcionariosCVT),
        ("Frota", frotaCVT),
        ("Completo", completoCVT),
        ("Voltar", main)
    ]
    exibirMenu(subopcoes, "Conversão")

def executeEXP(fun):
    print(3*'\n', 'Iniciando exportação...')
    start = time.time()
    fun()
    end = time.time()
    print('Tempo de execução: {:.2f} segundos'.format(end - start))
    time.sleep(1)

def completoEXP():
    executeEXP(exp.clientes)
    executeEXP(exp.produtos)
    executeEXP(exp.produtosBarras)
    executeEXP(exp.tributos)
    executeEXP(exp.fornecedores)
    executeEXP(exp.tanques)
    executeEXP(exp.bombas)
    executeEXP(exp.grupos)
    executeEXP(exp.funcionarios)
    executeEXP(exp.frota)

def clientesEXP():
    executeEXP(exp.clientes)

def produtosEXP():
    executeEXP(exp.produtos)
    executeEXP(exp.produtosBarras)
    executeEXP(exp.tributos)

def fornecedoresEXP():
    executeEXP(exp.fornecedores)

def mapaPistaEXP():
    executeEXP(exp.tanques)
    executeEXP(exp.bombas)

def gruposEXP():
    executeEXP(exp.grupos)

def funcionariosEXP():
    executeEXP(exp.funcionarios)

def frotaEXP():
    executeEXP(exp.frota)

def exportacao():
    subopcoes = [
        ("Clientes", clientesEXP),
        ("Produtos", produtosEXP),
        ("Fornecedores", fornecedoresEXP),
        ("Mapa de pista", mapaPistaEXP),
        ("Grupos", gruposEXP),
        ("Funcionarios", funcionariosEXP),
        ("Frota", frotaEXP),
        ("Completo", completoEXP),
        ("Voltar", main)
    ]
    exibirMenu(subopcoes, "Exportação")

def close():
    print('Saindo...')
    dbi.closeConn()
    db.closeConn()
    exit()

### MENU PRINCIPAL ###
menuPrincipal = [
    ("Conversão", conversao),
    ("Exportação", exportacao),
    ("Sair", close),
]

def main():
    exibirMenu(menuPrincipal)

main()
