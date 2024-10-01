from projeto.models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, lagradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.lagradouro = lagradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade 
        self.uf = uf


    def __str__(self) -> str:
        return(f"\nLagradouro: {self.lagradouro}"
               f"\nNúmero: {self.numero}"
               f"\nComplemento: {self.complemento}"
               f"\nCEP: {self.cep}"
               f"\nCidade: {self.cidade}"
               f"\nUF: {self.uf.sigla} / {self.uf.nome}"
               )    