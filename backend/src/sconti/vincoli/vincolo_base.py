from abc import ABC, abstractmethod

from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class Vincolo(ABC):
    """
    Classe astratta base per la gestione dei vincoli tra sconti
    Ogni vincolo specifico implementerà il metodo si_verifica
    """
    @abstractmethod
    def si_verifica(
        self, 
        sconto_attuale: Sconto, 
        sconti_applicati: list[Sconto], 
        ordine: Ordine
    ) -> bool:
        """
        Verifica se il vincolo è rispettato
        
        :param sconto_attuale: Sconto che si sta valutando
        :param sconti_applicati: Sconti già applicati all'ordine
        :param ordine: Ordine corrente
        :return: True se il vincolo è rispettato, False altrimenti
        """
        pass