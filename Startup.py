from StartupImpl import StartupImpl


class Startup(StartupImpl):
    def __init__(self, data_id, data_nome, data_sede):
        self.data_id = data_id
        self.data_nome = data_nome
        self.data_sede = data_sede

    def setId(self, data_id):
        self.data_id = data_id

    def getId(self):
        return self.data_id
    
    def setNome(self, data_nome):
        self.data_nome = data_nome
    
    def getNome(self):
        return self.data_nome
    
    def setCidade(self, data_sede):
        self.data_sede = data_sede
        
    def getCidade(self):
        return self.data_sede
