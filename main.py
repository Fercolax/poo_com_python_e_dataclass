class Cliente:
    def __init__(self, nome:str,email:str):
        self.nome = nome
        self.email = email
        
    def exibir(self):
        print(self.nome , self.email)
        
    def chamar_exibir(self):
        self.exibir()
        
        
cliente = Cliente("fernando",'a@gmail.com')

cliente.exibir()

cliente.chamar_exibir()