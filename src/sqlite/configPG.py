import sqlite3
import logging

class ConfigPG():
    def __init__(self, database='config'):
        self.database = 'db/' + database + '.db'
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.database)

    def cursor(self):
        return self.conn.cursor()
    
    def closeConn(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def createTables(self, cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pg_configuracao_fiscal (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo CHAR(1),
                cod_empresa INTEGER,
                codigo_fiscal TEXT UNIQUE,
                prioridade INTEGER,
                finalidade CHAR(1)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pg_configuracao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chave TEXT UNIQUE,  
                valor TEXT
            )
        ''')

    def insertConfig(self, cursor):
        configs = {
            'CLIENTE_PAIS': 'BRASIL',
            'CLIENTE_ESTADO': 'SC',
            'CLIENTE_CIDADE': 'RIO DO SUL',
            'TIPO_LANCAMENTO_FINANCEIRO': '65-1',
            'ESPECIE_LANCAMENTO_FINANCEIRO': '3-1',
            'PLANO_DE_CONTAS_DEBITO': '54-1',
            'PLANO_DE_CONTAS_CREDITO': '150-1',
        }
        for chave, valor in configs.items():
            try:
                cursor.execute('INSERT INTO pg_configuracao (chave, valor) VALUES (?, ?)', (chave, valor))
            except Exception as e:
                logging.info(e)
    
        config_fiscal = {
            '1': [
                'G',
                '1',
                '15-1',
                '1',
                'P'
            ],
            '2': [
                'G',
                '1',
                '14-1',
                '2',
                'P'
            ], 
            '3': [
                'G',
                '1',
                '1-1',
                '1',
                'T'
            ],
            '4': [
                'G',
                '1',
                '32-1',
                '2',
                'T'
            ]
        }

        for chave, valor in config_fiscal.items():
            try:
                cursor.execute('INSERT INTO pg_configuracao_fiscal (tipo, cod_empresa, codigo_fiscal, prioridade, finalidade) VALUES (?, ?, ?, ?, ?)', (valor[0], valor[1], valor[2], valor[3], valor[4]))
            except:
                pass
