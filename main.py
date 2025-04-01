import datetime
from backend.src.core.catalogo_pizze import CatalogoPizze
from backend.src.core.cliente import Cliente
from backend.src.core.pizza import Pizza
from backend.src.core.ordine import Ordine
from backend.src.sconti.sconto_base import Sconto
from backend.src.sconti.sconto_disabilita import ScontoDisabilita
from backend.src.sconti.sconto_temporale import ScontoTemporale
from backend.src.sconti.vincoli.vincolo_base import Vincolo
from backend.src.sconti.gestore_sconti import GestoreSconti
from backend.src.core.sistema_ordini import SistemaOrdini
from backend.src.sconti.sconto_eta import ScontoEta
from backend.src.sconti.sconto_gruppi import ScontoGruppo
from backend.src.sconti.sconto_fidelity_card import ScontoFidelity
from backend.src.sconti.vincoli.vincolo_eta_gruppo import VincoloEtaGruppo
from backend.src.sconti.vincoli.vincolo_esclusione import VincoloEsclusione

def crea_sconti() -> list[Sconto]:
    """
    Crea una lista di sconti disponibili
    """
    return [
        ScontoEta(),
        ScontoGruppo(),
        ScontoDisabilita(),
        ScontoFidelity(),
        ScontoTemporale()
    ]

def crea_vincoli() -> list[Vincolo]:
    """
    Crea una lista di vincoli per gli sconti
    """
    return [
        VincoloEtaGruppo(),
        VincoloEsclusione([])
    ]

def crea_sistema_ordini() -> SistemaOrdini:

    gestore_sconti = GestoreSconti(
        lista_sconti=crea_sconti(),
        vincoli=crea_vincoli()
    )
    catalogo_pizze = CatalogoPizze()
    return SistemaOrdini(gestore_sconti, catalogo_pizze)

def catalogo_pizze_base() -> list[Pizza]:
    pizze_disponibili = CatalogoPizze()
    print(pizze_disponibili)
    return pizze_disponibili.get_pizze_disponibili()

def stampa_risultato(ordine):
    sistema_ordini = crea_sistema_ordini()
    ordine.aggiungi_pizze(sistema_ordini.catalogo_pizze())
    ordine_finale = sistema_ordini.crea_ordine(ordine)
    # Stampo i dettagli dell'ordine
    print(ordine_finale)

    # Stampo il totale originale e scontato
    print(f"\nTotale originale: {ordine.totale_ordine()} €")
    print(f"Totale scontato: {ordine_finale.totale_ordine_scontato()} €")
    print(sistema_ordini.sconti_applicati_ordine())


def test_sconto_fidelity():
    print("\nTest sconto fidelity card (15%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40, fidelity_card=True)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=1)
    stampa_risultato(ordine)

def test_sconto_disabilita():
    print("\nTest sconto disabilità (90%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40, disabilita=True)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=1)
    stampa_risultato(ordine)

def test_sconto_gruppo_medio():
    print("\nTest sconto gruppo da 15 a 20 persone (20%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=16)
    stampa_risultato(ordine)

def test_sconto_gruppo_grande():
    print("\nTest sconto gruppo da 21 a 25 persone (30%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=23)
    stampa_risultato(ordine)

def test_sconto_gruppo_molto_grande():
    print("\n Test sconto gruppo oltre 25 persone (50%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=30)
    stampa_risultato(ordine)

def test_sconto_orario_infrasettimanale():
    print("\nTest sconto orario infrasettimanale entro le 20:00 (10%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    ordine.imposta_orario_ordine(datetime.datetime(2024, 1, 10, 19, 30))  # Mercoledì
    stampa_risultato(ordine)

def test_sconto_weekend():
    print("\nTest sconto weekend (10%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=40)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=2)
    ordine.imposta_orario_ordine(datetime.datetime(2024, 1, 13, 22, 30))  # Sabato
    stampa_risultato(ordine)

def test_sconto_weekend_piu_fidelity():
    print("\n Test sconto week o infrasettimanale insieme allo sconto fidelity.\n")
    cliente = Cliente(nome="Mario Rossi", eta=40, fidelity_card=True)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    stampa_risultato(ordine)

def test_sconto_eta_anziani():
    print("\n Test sconto per over 60 (70%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=65)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    stampa_risultato(ordine)

def test_sconto_bambini_sotto_4_anni():
    print("\n Test sconto bambini sotto 4 anni (50%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=2)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    stampa_risultato(ordine)

def test_sconto_bambini_sotto_12_anni():
    print("\n Test sconto bambini sotto 12 anni (20%)\n")
    cliente = Cliente(nome="Mario Rossi", eta=10)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    stampa_risultato(ordine)

def test_sconti_cumulabili():
    print("\n Test sconti cumulabili: fidelity + bambino sotto 12 anni\n")
    cliente = Cliente(nome="Mario Rossi", eta=10, fidelity_card=True)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
    stampa_risultato(ordine)

def test_sconti_gruppo_bambino():
    print("\n Test sconti gruppo + bambino sotto 4 anni\n")
    cliente = Cliente(nome="Mario Rossi", eta=2)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=21)
    stampa_risultato(ordine)

def main():

    test_sconto_fidelity()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_disabilita()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_gruppo_medio()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_gruppo_grande()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_gruppo_molto_grande()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_orario_infrasettimanale()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_weekend()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_weekend_piu_fidelity()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_eta_anziani()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_bambini_sotto_4_anni()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconto_bambini_sotto_12_anni()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconti_cumulabili()

    print("\n ############ NUOVO ORDINE ########### \n")
    test_sconti_gruppo_bambino()

if __name__ == "__main__":
    main()
