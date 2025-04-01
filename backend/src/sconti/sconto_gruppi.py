from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class ScontoGruppo(Sconto):
    """Sconto per dimensione gruppo"""
    def __init__(self):
        super().__init__("Gruppo", priorita=20)

    def e_applicabile(self, ordine: Ordine) -> bool:
        return ordine.num_persone > 15

    def calcola_sconto(self, prezzo: float, ordine: Ordine) -> float:
        if 15 <= ordine.num_persone <= 20:
            return prezzo * 0.20
        elif 21 <= ordine.num_persone <= 25:
            return prezzo * 0.30
        elif ordine.num_persone > 25:
            return prezzo * 0.50
        return 0