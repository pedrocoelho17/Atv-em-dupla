from projeto.models.endereco import Endereco
from abc import ABC

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nIdentidade: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nE-mail: {self.email}"
                f"\nEndereço: {self.endereco}"
                )  