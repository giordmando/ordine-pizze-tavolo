from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto
from backend.src.sconti.vincoli.vincolo_base import Vincolo


class VincoloEsclusione(Vincolo):
    """
    Vincolo che impedisce l'applicazione di sconti in conflitto
    """
    def __init__(self, nomi_sconti_in_conflitto: list[str]):
        self.nomi_sconti_in_conflitto = nomi_sconti_in_conflitto
    
    def si_verifica(
        self, 
        sconto_attuale: Sconto, 
        sconti_applicati: list[Sconto], 
        ordine: Ordine
    ) -> bool:
        """
        Verifica che non siano già stati applicati sconti in conflitto
        """
        # Lo sconto temporale deve essere unico
        temporale_unico = (
            sconto_attuale.nome == "Temporale" 
            and len(sconti_applicati) > 1
        )
        return not temporale_unico