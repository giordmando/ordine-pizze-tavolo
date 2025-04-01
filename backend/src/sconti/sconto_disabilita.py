from backend.src.core.cliente import Cliente
from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto


class ScontoDisabilita(Sconto):
    """Sconto per persone diversamente abili"""
    def __init__(self):
        super().__init__("Disabilità", priorita=100)

    def e_applicabile(self, ordine: Ordine) -> bool:
        return ordine.cliente.e_disabile

    def calcola_sconto(self, prezzo: float, ordine: Ordine) -> float:
        if self.e_applicabile(ordine):
            return prezzo * 0.90
        return 0
