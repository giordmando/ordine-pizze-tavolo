class Pizza:
    """
    Classe che rappresenta una pizza
    """
    def __init__(self, nome: str, prezzo_base: float):
        self.__nome = nome
        self.__prezzo_base = prezzo_base

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def prezzo_base(self) -> float:
        return self.__prezzo_base