class Cliente:
    def __init__(self, nome:str,email:str):
        self.nome = nome
        self.email = email
        
    def exibir(self):
        print(self.nome , self.email)
        
        
cliente = Cliente("fernando",'a@gmail.com')

cliente.exibir()