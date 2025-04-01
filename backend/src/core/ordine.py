from datetime import datetime
from backend.src.core.cliente import Cliente
from backend.src.core.pizza import Pizza


class Ordine:
    """
    Classe che rappresenta un ordine per un tavolo
    """
    def __init__(self, numero_tavolo: int, numero_ordine: int, cliente: Cliente, num_persone: int):
        self.__numero_tavolo = numero_tavolo
        self.__numero_ordine = numero_ordine
        self.__cliente = cliente
        self.__num_persone = num_persone
        self.__pizze: list[Pizza] = []
        self.__pizze_scontate: dict = {}
        self.__data_ordine: datetime = datetime.now()

    @property
    def numero_tavolo(self) -> int:
        return self.__numero_tavolo

    @property
    def numero_ordine(self) -> int:
        return self.__numero_ordine

    @property
    def num_persone(self) -> int:
        return self.__num_persone
    
    @property
    def cliente(self) -> Cliente:
        return self.__cliente
    
    @property
    def data_ordine(self) -> int:
        return self.__data_ordine
    
    @property
    def pizze(self) -> list[Pizza]:
        return self.__pizze
    
    def totale_ordine(self):
        return sum(pizza.prezzo_base for pizza in self.__pizze)
    
    def totale_ordine_scontato(self):
        return sum(importo for nome, importo in self.__pizze_scontate.items())

    def aggiungi_pizza(self, pizza: Pizza):
        """Aggiunge una pizza all'ordine"""
        self.__pizze.append(pizza)

    def aggiungi_pizze(self, pizze:list[Pizza]):
        """Aggiunge più pizze all'ordine"""
        self.__pizze.extend(pizze)  # Aggiungi tutte le pizze della lista

    def aggiungi_pizze_scontate(self, pizze_scontate: dict):
        """Aggiunge una pizza all'ordine"""
        self.__pizze_scontate = pizze_scontate

    def imposta_orario_ordine(self, dataordine:datetime):
        self.__data_ordine = dataordine
    
    def __str__(self):
        """Stampa le informazioni dell'ordine"""
        ordine_info = f"Ordine {self.numero_ordine} per il tavolo {self.numero_tavolo}\n"
        ordine_info += f"Cliente: {self.cliente}\n"
        ordine_info += f"Numero di persone: {self.num_persone}\n\n"

        # Stampa le pizze ordinate
        ordine_info += "Pizze ordinate:\n"
        for pizza in self.__pizze:
            ordine_info += f"- {pizza.nome}: {pizza.prezzo_base} €\n"

        # Stampa le pizze scontate
        if self.__pizze_scontate:
            ordine_info += "\nPizze scontate:\n"
            for pizza_nome, prezzo_scontato in self.__pizze_scontate.items():
                ordine_info += f"- {pizza_nome}: {prezzo_scontato} €\n"

        return ordine_info
    