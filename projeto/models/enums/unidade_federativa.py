from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SÃO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla
        