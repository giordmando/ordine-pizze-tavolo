from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class ScontoTemporale(Sconto):
    """Sconto per dimensione gruppo"""
    def __init__(self):
        super().__init__("Temporale", priorita=0)

    def e_applicabile(self, ordine: Ordine) -> bool:
        return True

    def calcola_sconto(self, prezzo: float, ordine: Ordine) -> float:
        if self.e_applicabile(ordine):
            if ordine.data_ordine and (ordine.data_ordine.weekday() >= 5 or ordine.data_ordine.hour < 20):
                return prezzo * 0.10  # Sconto del 10%
        return 0