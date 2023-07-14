class Converter:
    def __init__(self, cursor, queryMaker, sgm, dbi, cur):
        self.cursor = cursor
        self.qm = queryMaker
        self.sgm = sgm
        self.dbi = dbi
        self.cur = cur

    def produtos(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['produtos'], order='procod', cols=self.sgm.getListComma('produtos')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertProdutos(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  
            
    def produtosBarras(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['produtos_barras'], order='procod', cols=self.sgm.getListComma('produtos_barras')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertProdutosBarras(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def bombas(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['bombas'], order='bomcod', cols=self.sgm.getListComma('bombas')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertBombas(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def frota(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['frota'], order='clicod', cols=self.sgm.getListComma('frota')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertFrota(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def grupos(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['grupos'], order='grucod', cols=self.sgm.getListComma('grupos')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertGrupos(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def tributos(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['tributos'], order='tricod', cols=self.sgm.getListComma('tributos')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertTributos(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def fornecedores(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['fornecedores'], order='forcod', cols=self.sgm.getListComma('fornecedores')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertFornecedores(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def funcionarios(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['funcionarios'], order='funcod', cols=self.sgm.getListComma('funcionarios')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertFuncionarios(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def clientes(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['clientes'], order='clicod', cols=self.sgm.getListComma('clientes')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertClientes(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  

    def tanques(self):
        self.cursor.execute(self.qm.simple(table=self.sgm.table['tanques'], order='tancod', cols=self.sgm.getListComma('tanques')))
        for row in self.cursor.fetchall():
            try:
                self.sgm.insertTanques(self.cur, row)
                self.dbi.commit()
            except Exception as e:
                print(e)
                tmp = input('Pressione qualquer tecla para continuar')  
