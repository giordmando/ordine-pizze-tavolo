from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto
from backend.src.sconti.vincoli.vincolo_base import Vincolo


class VincoloEtaGruppo(Vincolo):
    """
    Vincolo specifico per gestire il conflitto tra sconti Età e Gruppo
    """
    def si_verifica(
        self, 
        sconto_attuale: Sconto, 
        sconti_applicati: list[Sconto], 
        ordine: Ordine
    ) -> bool:
        """
        Impedisce lo sconto Età per under 12 se è stato applicato lo sconto Gruppo
        """
        # Se lo sconto attuale è Età e l'età è < 12
        if sconto_attuale.nome == "Età" and ordine.cliente.eta < 12:
            # Verifico se è stato applicato uno sconto Gruppo
            return not any(
                sconto.nome == "Gruppo" 
                for sconto in sconti_applicati
            )
        return True