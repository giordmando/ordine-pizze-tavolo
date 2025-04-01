from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class ScontoEta(Sconto):
    """Sconto per fasce d'età"""
    def __init__(self):
        super().__init__("Età", priorita=5)

    def e_applicabile(self, ordine: Ordine) -> bool:
        eta = ordine.cliente.eta
        return (eta >= 60) or (eta < 12)

    def calcola_sconto(self, prezzo: float, ordine:Ordine) -> float:
        eta = ordine.cliente.eta
        return (
            prezzo * 0.70 if self.e_applicabile(ordine) and eta >= 60 else
            prezzo * 0.50 if self.e_applicabile(ordine) and eta < 4 else
            prezzo * 0.20 if self.e_applicabile(ordine) and eta < 12 else
            0
        )
