from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class ScontoFidelity(Sconto):
    """Sconto per possessori di fidelity card"""
    def __init__(self):
        super().__init__("Fidelity Card", priorita=10)

    def e_applicabile(self, ordine: Ordine) -> bool:
        return ordine.cliente.ha_fidelity_card

    def calcola_sconto(self, prezzo: float, ordine: Ordine) -> float:
        if self.e_applicabile(ordine):
            return prezzo * 0.15 
        return 0