from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.produto = produto


    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nProduto: {self.produto}")    