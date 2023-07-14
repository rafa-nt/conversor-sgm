class Method():
    def __init__(self):
        self.table ={
            'produtos': 'ect001', # ok
            'produtos_barras': 'ect001d', # ok
            'bombas': 'bombas', # ok
            'frota': 'ect002g', # ok
            'grupos': 'ect004', # ok
            'tributos': 'ect010', # ok
            'fornecedores': 'oft003', # ok
            'funcionarios': 'oft006', # ok
            'clientes': 'spt002', # ok
            'tanques': 'tanque', # ok
        }
        self.fields = {
            'frota': [
                'clicod',
                'clpplaca',
                'clpmarca',
                'clpultkm',
                'clpativa',
            ],
            'produtos': [
                'procod',
                'prodescric',
                'grucod',
                'proprecusr',
                'proprevist',
                'prounidmed',
                'protipo',
                'tricod',
                'proclafisc',
                'proippt',
                'proiat',
                'proqtdatue',
                'procodanp',
            ],
            'produtos_barras': [
                'procod',
                'pcbsequenc',
                'pcbcodbarr',
            ],
            'grupos': [
                'grucod',
                'grudescric',
            ],
            'bombas': [ 
                'bomcod',
                'tancod',
                'procod',
                'bomcodcomp',
                'bomilhcod',
            ],
            'tributos': [
                'tricod',
                'trides',
                'tbbcod',
                'alicod',
                'natcod',
            ],
            'fornecedores': [
                'forcod',
                'fortippess',
                'fornome',
                'fornomfant',
                'forenderec',
                'forbairro',
                'forcidade',
                'forcep',
                'forcgc',
                'forcpf',
                'forinsesta',
                'fornro1fon',
                'formail',
                'foruf',
                'forendnro',
                'forendcomp'
            ],
            'funcionarios': [
                'funcod',
                'funnome',
                'funativo'
            ],
            'clientes': [
                'clicod',
                'clitippess',
                'cliindativ',
                'clirazsoci',
                'clinomfant',
                'clienderec',
                'clibairro',
                'cliuf',
                'clicep',
                'clicgc',
                'cliinsesta',
                'clinrocpf',
                'clinroiden',
                'clinro1fon',
                'climail',
                'cliendnro',
                'cliendcomp'
            ],
            'tanques': [
                'tancod',
                'taqcaparma',
                'taqativo',
            ]
        }

    def getListComma(self, key):
        return ', '.join(self.fields[key])

    def createTables(self, cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                descricao TEXT,
                codigo_grupo TEXT,
                preco_custo REAL,
                preco_venda REAL,
                unidade_medida TEXT,
                tipo TEXT,
                codigo_tributo TEXT,
                codigo_ncm TEXT,
                ippt TEXT,
                iat TEXT,
                quantidade TEXT,
                anp TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos_barras (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                sequencia TEXT,
                codigo_barras TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS frota (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo_cliente TEXT,
                placa TEXT,
                marca TEXT,
                ultimo_km TEXT,
                ativo TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bombas (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                codigo_tanque TEXT,
                codigo_produto TEXT,
                hexa TEXT,
                casa_milhao TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grupos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                descricao TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tributos (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                descricao TEXT,
                cst TEXT,
                aliquota REAL,
                cfop TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                tipo TEXT,
                nome TEXT,
                nome_fantasia TEXT,
                endereco TEXT,
                bairro TEXT,
                cidade TEXT,
                cep TEXT,
                cnpj TEXT,
                cpf TEXT,
                inscr_estadual TEXT,
                fone TEXT,
                email TEXT,
                uf TEXT,
                numero TEXT,
                complemento TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                nome TEXT,
                ativo TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                tipo TEXT,
                ativo TEXT,
                nome TEXT,
                nome_fantasia TEXT,
                endereco TEXT,
                bairro TEXT,
                uf TEXT,
                cep TEXT,
                cnpj TEXT,
                inscr_estadual TEXT,
                cpf TEXT,
                identidade TEXT,
                fone TEXT,
                email TEXT,
                numero TEXT,
                complemento TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tanques (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                codigo TEXT,
                capacidade REAL,
                ativo TEXT
            )
        ''')

    def insert(self, key):
        tam = len(self.fields[key])
        elementos = self.fields[key]
        query = 'INSERT INTO ' + key + \
            ' (' + ', '.join(elementos) + ')' + \
            ' VALUES (' + ', '.join(['?'] * tam) + ')'
        return query
    
    def directInsert(self, key):
        query = 'INSERT INTO ' + key + \
            ' VALUES (?, ' + ', '.join(['?'] * len(self.fields[key])) + ')'
        return query
    
    def insertProdutos(self, cursor, row):
        cursor.execute(self.directInsert('produtos'), (None, row[0], row[1], row[2], float(row[3]), float(row[4]), row[5], row[6], row[7], row[8], row[9], row[10], float(row[11]), row[12]))
    
    def insertProdutosBarras(self, cursor, row):
        cursor.execute(self.directInsert('produtos_barras'), (None, row[0], row[1], row[2]))

    def insertBombas(self, cursor, row):
        cursor.execute(self.directInsert('bombas'), (None, row[0], row[1], row[2], row[3], row[4]))

    def insertFrota(self, cursor, row):
        cursor.execute(self.directInsert('frota'), (None, row[0], row[1], row[2], row[3], row[4]))
    
    def insertGrupos(self, cursor, row):
        cursor.execute(self.directInsert('grupos'), (None, row[0], row[1]))

    def insertTributos(self, cursor, row):
        cursor.execute(self.directInsert('tributos'), (None, row[0], row[1], row[2], float(row[3]), row[4]))

    def insertFornecedores(self, cursor, row):
        cursor.execute(self.directInsert('fornecedores'), (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))

    def insertFuncionarios(self, cursor, row):
        cursor.execute(self.directInsert('funcionarios'), (None, row[0], row[1], row[2]))

    def insertClientes(self, cursor, row):
        cursor.execute(self.directInsert('clientes'), (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]))

    def insertTanques(self, cursor, row):
        cursor.execute(self.directInsert('tanques'), (None, row[0], float(row[1]), row[2]))

    # def insertProdutosCompletos(self, cursor, row):
    #     codigo = row[0]
    #     codigo_aliquota = row[1]
    #     descricao = row[2]
    #     chave_grupo = row[3]
    #     codigo_ncm = row[4]
    #     codigo_cest = row[5]
    #     codigo_unidade = row[6]
    #     embalagem = 0 if row[7] is None else float(row[7])
    #     custo = 0 if row[8] is None else float(row[8])
    #     preco_de_venda = 0 if row[9] is None else float(row[9])
    #     quantidade = 0 if row[10] is None else float(row[10])
    #     cst = row[11]

    #     cursor.execute('''
    #         INSERT INTO produtos_completos (codigo, codigo_aliquota, descricao, chave_grupo, codigo_ncm, codigo_cest, codigo_unidade, embalagem, custo, preco_de_venda, quantidade, cst) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    #     ''', (codigo, codigo_aliquota, descricao, chave_grupo, codigo_ncm, codigo_cest, codigo_unidade, embalagem, custo, preco_de_venda, quantidade, cst))
