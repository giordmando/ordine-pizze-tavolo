class Cliente:
    """
    Classe che rappresenta un cliente con le sue caratteristiche personali.
    Incapsulamento: attributi privati con metodi getter/setter
    """
    def __init__(self, nome: str, eta: int, gruppo: int = 0, 
                 fidelity_card: bool = False, disabilita: bool = False):
        self.__nome = nome  # Attributo privato
        self.__eta = eta
        self.__fidelity_card = fidelity_card
        self.__disabilita = disabilita

    # Getter e setter incapsulati
    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def eta(self) -> int:
        return self.__eta

    @property
    def ha_fidelity_card(self) -> bool:
        return self.__fidelity_card

    @property
    def e_disabile(self) -> bool:
        return self.__disabilita
    
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}\n"
            f"Età: {self.eta}\n"
            f"Fidelity Card: {'Sì' if self.ha_fidelity_card else 'No'}\n"
            f"Disabile: {'Sì' if self.e_disabile else 'No'}"
        )