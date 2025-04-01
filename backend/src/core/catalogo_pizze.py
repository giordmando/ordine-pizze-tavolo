from backend.src.core.pizza import Pizza


class CatalogoPizze:
    def __init__(self):
        self.__pizze_disponibili = {
            "Margerita": 10,
            "Capricciosa": 12,
            "Marinara": 8,
            "Formaggi": 12,
        }

    def __str__(self):
        catalogo_str = "Catalogo Pizze Disponibili:\n"
        for nome, prezzo in self.__pizze_disponibili.items():
            catalogo_str += f"- {nome}: {prezzo} €\n"
        return catalogo_str
    
    def aggiungi_pizza(self, pizza: Pizza):
        pass

    def get_dict_pizze_disponibili(self):
        return list(self.__pizze_disponibili.values())
    
    def get_pizze_disponibili(self):
        return [Pizza(nome, prezzo) for nome, prezzo in self.__pizze_disponibili.items()]