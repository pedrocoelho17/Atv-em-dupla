from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco
from abc import ABC

class Prestacao_de_Servico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str, contratoInicio: str, contratoFim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nContrato início: {self.contratoInicio}"
                f"\nContrato fim: {self.contratoFim}"
                )   