from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.fisica import Fisica

class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.protocoloAtendimento = protocoloAtendimento


    def __str__(self) -> str:
        return (f"\n{super().__str__()}"
                f"\nProtocolo de atendimento: {self.protocoloAtendimento}") 
    