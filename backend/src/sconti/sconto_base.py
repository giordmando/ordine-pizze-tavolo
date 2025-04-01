import abc
from backend.src.core.ordine import Ordine


class Sconto(abc.ABC):
    """
    Classe astratta base per gli sconti 
    Polimorfismo: ogni sottoclasse implementa il proprio metodo calcola_sconto
    """
    def __init__(self, nome: str, priorita: int = 0):
        self._nome = nome
        self._priorita = priorita

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def priorita(self) -> int:
        return self._priorita

    @abc.abstractmethod
    def calcola_sconto(self, prezzo: float, ordine: Ordine) -> float:
        """Metodo astratto per calcolare lo sconto"""
        pass

    @abc.abstractmethod
    def e_applicabile(self, ordine: Ordine) -> bool:
        """Verifica se lo sconto è applicabile"""
        pass