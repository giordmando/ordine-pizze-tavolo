

def test_sconti_cumulabili(pizza_base):
    """Test sconti cumulabili: fidelity + età anziani"""
    cliente = Cliente(nome="Mario", cognome="Rossi", eta=65, ha_fidelity_card=True)
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=1)
    ordine.aggiungi_pizza(pizza_base)
    
    sistema_ordini = crea_sistema_ordini()
    ordine_finale = sistema_ordini.crea_ordine(ordine)
    
    # Calcolo atteso: 10 * 0.85 * 0.3 = 2.55
    assert ordine_finale.totale_ordine_scontato() == pytest.approx(2.55, rel=1e-2)

def test_limite_minimo_prezzo(pizza_base):
    """Test limite minimo di prezzo a 5€"""
    cliente = Cliente(nome="Mario", cognome="Rossi", eta=2)  # Bambino sotto 4 anni
    ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=1)
    ordine.aggiungi_pizza(pizza_base)
    
    sistema_ordini = crea_sistema_ordini()
    ordine_finale = sistema_ordini.crea_ordine(ordine)
    
    assert ordine_finale.totale_ordine_scontato() == 5.00