from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.pessoa import Pessoa

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento

    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nSexo: {self.sexo.value}"
                f"\nEstado Civil: {self.estadoCivil}"
                f"\nData de nascimento: {self.dataNascimento}")    