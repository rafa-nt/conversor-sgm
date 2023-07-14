import pandas as pd

class Exportar:
    def __init__(self, conn, sgm):
        self.conn = conn
        self.sgm = sgm

    def export(self, query, conn, filename):
        filename = filename + '.xlsx'
        df = pd.read_sql(query, conn)
        df.to_excel(filename, index=False)

    def grupos(self):
        query = 'SELECT * FROM grupos'
        self.export(query, self.conn, 'grupos')

    def tanques(self):
        query = 'SELECT * FROM tanques'
        self.export(query, self.conn, 'tanques')
    
    def bombas(self):
        query = 'SELECT * FROM bombas'
        self.export(query, self.conn, 'bombas')
    
    def clientes(self):
        query = 'SELECT * FROM clientes'
        self.export(query, self.conn, 'clientes')

    def fornecedores(self):
        query = 'SELECT * FROM fornecedores'
        self.export(query, self.conn, 'fornecedores')

    def produtos(self):
        query = 'SELECT * FROM produtos'
        self.export(query, self.conn, 'produtos')

    def produtosBarras(self):
        query = 'SELECT * FROM produtos_barras'
        self.export(query, self.conn, 'produtos_barras')

    def frota(self):
        query = 'SELECT * FROM frota'
        self.export(query, self.conn, 'frota')
    
    def tributos(self):
        query = 'SELECT * FROM tributos'
        self.export(query, self.conn, 'tributos')

    def funcionarios(self):
        query = 'SELECT * FROM funcionarios'
        self.export(query, self.conn, 'funcionarios')

    # def cfgFiscalProdutos(self):
    #     configFiscal = pd.read_sql('SELECT * FROM pg_configuracao_fiscal', self.conn)
    #     produtos = pd.read_sql('SELECT codigo FROM produtos_completos', self.conn)
    #     export = pd.DataFrame(columns=['codigo', 'tipo', 'cod_empresa', 'codigo_fiscal', 'prioridade', 'finalidade'])
    #     for i in produtos['codigo']:
    #         for index, row in configFiscal.iterrows():
    #             export.loc[len(export)] = [i, row['tipo'], row['cod_empresa'], row['codigo_fiscal'], row['prioridade'], row['finalidade']]
    #     export.to_excel('configFiscalProdutos.xlsx', index=False)
