from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.fisica import Fisica
from projeto.models.enums.setor import Setor



class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario


    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatrícula: {self.matricula}"
                f"\nSetor: {self.setor.value}"
                f"\nSalário: {self.salario}"
                )   
    
