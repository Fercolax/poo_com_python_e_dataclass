from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email:str
    idade:int
    
    def exibir(self):
        print(f"O cliente {self.nome} tem {self.idade} anos e seu email de contato é {self.email}")
    
cliente = Cliente(nome='fernando',email='a@l.com',idade=20)

print(cliente)
print(cliente.nome, cliente.email, cliente.idade)

cliente.exibir()