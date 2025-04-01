from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class TracciaOrdine:
    def __init__(self, ordine: Ordine):
        self.__ordine = ordine
        # Tracciamento degli sconti applicati
        self.__sconti_applicati: list[Sconto] = []

    def ordine(self) -> Ordine:
        return self.__ordine

    def aggiungi_sconto(self, sconti:list[Sconto]) -> Ordine:
        self.__sconti_applicati = sconti

    def sconti_applicati(self) -> Ordine:
        return self.__sconti_applicati
       
    def __str__(self):
        """Stampa le informazioni dell'ordine"""
        ordine_info = f"\n"

        # Stampa gli sconti applicati
        if self.__sconti_applicati:
            ordine_info += "\nSconti applicati:\n"
            for sconto in self.__sconti_applicati:
                ordine_info += f"- {sconto.nome}\n"

        return ordine_info
    
    