from backend.src.core.catalogo_pizze import CatalogoPizze
from backend.src.core.ordine import Ordine
from backend.src.core.traccia_ordine import TracciaOrdine
from backend.src.sconti.gestore_sconti import GestoreSconti


class SistemaOrdini:
    def __init__(self, gestoresconti: GestoreSconti, catalogo_pizze: CatalogoPizze):
        self.__gestoresconti = gestoresconti
        self.__catalogo_pizze = catalogo_pizze
        self.__traccia_ordine: TracciaOrdine = None

    def catalogo_pizze(self) -> dict:
        return self.__catalogo_pizze.get_pizze_disponibili()

    def crea_ordine(self, ordine: Ordine) -> Ordine:
        self.__traccia_ordine = TracciaOrdine(ordine)
        self.__traccia_ordine.aggiungi_sconto(self.__gestoresconti.sconti_applicabili(ordine))
        return self.__calcola_prezzi_ordine(ordine)

    def __calcola_prezzi_ordine(self, ordine: Ordine) -> Ordine:
        # Applica gli sconti in sequenza
        pizze_scontate = {}
        for pizza in ordine.pizze:
            prezzo_scontato = self.__gestoresconti.applica_sconti(pizza, ordine)
            pizze_scontate[pizza.nome] = max(prezzo_scontato, 5.0)

        ordine.aggiungi_pizze_scontate(pizze_scontate)
        
        return ordine
    
    def sconti_applicati_ordine(self):
        return self.__traccia_ordine
    