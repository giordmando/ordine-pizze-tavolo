from backend.src.core.catalogo_pizze import CatalogoPizze
from backend.src.core.sistema_ordini import SistemaOrdini
from backend.src.sconti.gestore_sconti import GestoreSconti
from fastapi import FastAPI

app = FastAPI()

# Inizializzazione del sistema ordini
gestore_sconti = GestoreSconti()
catalogo_pizze = CatalogoPizze()
sistema_ordini = SistemaOrdini(gestore_sconti, catalogo_pizze)


@app.get("/pizze/")
async def get_pizze():
    pizze = sistema_ordini.catalogo_pizze()
    return [{"nome": nome, "prezzo_base": prezzo_base} for nome, prezzo_base in pizze.items()]