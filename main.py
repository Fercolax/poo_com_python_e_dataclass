from categoria import Categoria
from transacao import Transacao


c = Categoria(nome="Receitas")

t = Transacao(
    descricao="Salário Jan/2024",
    valor=1000.0,
    categoria=c
)

t.exibir()