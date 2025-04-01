from typing import Optional
from backend.src.core.ordine import Ordine
from backend.src.core.pizza import Pizza
from backend.src.sconti.sconto_base import Sconto
from backend.src.sconti.vincoli.vincolo_base import Vincolo


class GestoreSconti:
    """
    Gestore centralizzato degli sconti
    """
    def __init__(self,
                lista_sconti: list[Sconto],
                vincoli: Optional[list[Vincolo]] = None):
        
        self.__sconti_disponibili: list[Sconto] = lista_sconti
        # Definizione dei vincoli tra sconti
        self.__vincoli = vincoli or []

    def sconti_disponibili(self) -> list[Sconto]:
        return self.__sconti_disponibili
    
    def sconti_applicabili(self, ordine: Ordine) -> list[Sconto]:
        # Ordina gli sconti per priorità decrescente
        sconti_ordinati = sorted(
            [s for s in self.__sconti_disponibili if s.e_applicabile(ordine)], 
            key=lambda x: x.priorita, 
            reverse=True
        )
        
        """Restituisce gli sconti applicabili all'ordine"""
        return self.__filtra_sconti_per_vincoli(sconti_ordinati, ordine)
    
    def __filtra_sconti_per_vincoli(self,
                                    sconti_applicabili_ordine:list[Sconto],
                                    ordine:Ordine) -> list[Sconto]:
        """
        Filtra gli sconti applicabili considerando i vincoli
        """
        # Filtra gli sconti applicabili considerando tutti i vincoli
        return [
            sconto for sconto in sconti_applicabili_ordine
            if all(
                vincolo.si_verifica(sconto, sconti_applicabili_ordine, ordine)
                for vincolo in self.__vincoli
            )
        ]
    
    def applica_sconti(self, pizza:Pizza, ordine:Ordine):
        # Filtra sconti applicabili considerando i vincoli
        sconti_applicabili_cleared = self.sconti_applicabili(ordine)
       
        prezzo_sconto = pizza.prezzo_base
        for sconto in sconti_applicabili_cleared:
            prezzo_sconto -= sconto.calcola_sconto(prezzo_sconto, ordine)
        return prezzo_sconto
    
