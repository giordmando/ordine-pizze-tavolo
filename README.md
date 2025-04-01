# ordine-pizze-tavolo
Un sistema per calcolare il prezzo delle pizze applicando diversi sconti.

## Indice

- [Introduzione](#introduzione)
- [Funzionalità](#funzionalità)
- [Utilizzo](#utilizzo)
- [Struttura del Progetto](#struttura-del-progetto)
- [Sconti Implementati](#sconti-implementati)
- [Esempi di Utilizzo](#esempi-di-utilizzo)
- [Note](#note)

## Introduzione

Questo progetto simula un sistema di ordine pizze al tavolo, applicando una serie di sconti basati su criteri specifici come la presenza di una fidelity card, lo stato di disabilità, la dimensione del gruppo, l'orario dell'ordine, l'età del cliente e altre condizioni promozionali. Il sistema è implementato in Python seguendo i principi della programmazione ad oggetti (OOP).

## Funzionalità

- Calcolo del prezzo scontato di una pizza a partire dal prezzo.
- Applicazione di sconti basati su:
    - Fidelity card (15%)
    - Disabilità (90%)
    - Sconti per gruppi (20-50%)
    - Ordine entro le 20:00 o nel weekend (10%)
    - Età del cliente (70% per over 60, 50% per bambini sotto i 4 anni, 20% per under 12)
- Prezzo minimo della pizza: 5€.
- Gestione vincoli esclusione sconti
- Gestione di più pizze in un singolo ordine.

Nota non è stata implementata la gestione di più ordini nel SistemaOrdini solo per semplicità

## Utilizzo

1.  Clona il repository:
    ```
    git clone https://github.com/giordmando/ordine-pizze-tavolo.git
    ```
2.  Esegui lo script `main.py`:
    ```
    python main.py in Linux o Mac
    ```
    ```
    python.exe main.py in windows
    ```
3.  Ha schermo verranno visualizzati i risultati dei diversi ordini con le rispettive scontistiche applicate.

I test sui diversi tipi di scontistiche sono stati definiti nel file main.py

## Struttura del Progetto

Il progetto è strutturato in classi per gestire le pizze e gli sconti e ordini:
- **Core**:
    - `Pizza`: Rappresenta una pizza con il suo prezzo base.
    - `Ordine`: Rappresenta un ordine di un cliente ad un tavolo.
    - `Cliente`: Rappresenta il cliente che effettua un ordine
    - `Catalogo pizze`: Rappresenta la lista delle pizze che possono essere selezionate
    - `SistemaOrdini`: Gestisce l'ordine, applica gli sconti, aggiorna lista pizze socntate e traccia l'ordine
- **Sconti**:
    - `GestoreSconti`: Gestisce gli sconti, applicabili all'ordine tenendo conto dei vincoli e applica gli socnti al prezzo base delle pizze.
    - `Sconto`: Classe astratta che rappresenta un singolo Sconto, da questa classe astratta sono state derivare le implementazioni, ScontoDisabilita, ScontoEta, ScontoFidelity, ScontoGruppo, ScontoTemporale
    - **Vincoli**:
        - `Vincolo`: Classe astratta che rappresenta un singolo Vincolo fra gli Sconti, da questa derivano le implementazioni, VincoloEsclusione e VincoloEtaGruppo

## Sconti Implementati

Il codice implementa i seguenti sconti:

*   Sconto fidelity card: 15%
*   Sconto per disabili: 90%
*   Sconti per gruppi:
    *   15-20 persone: 20%
    *   21-25 persone: 30%
    *   Più di 25 persone: 50%
*   Sconto per ordine entro le 20:00 o nel weekend: 10%
*   Sconto per clienti con 60 anni o più: 70%
*   Sconto per bambini:
    *   Sotto i 4 anni: 50%
    *   Sotto i 12 anni: 20%
*   Prezzo minimo: 5€
*   Vincolo applica Sconto per ordine entro le 20:00 o nel weekend: 10% solo se lo non sono applicati altri sconti
*   Vincolo applica Sconto per bambini solo se non è stato applicato Sconti per gruppi.

## Esempi di Utilizzo

**Scenario**: Cliente con fidelity card e bambino sotto i 12 anni.

*Configurazione sconti e vincoli*

	lista_sconti = [
	ScontoEta(),
	ScontoGruppo(),
	ScontoDisabilita(),
	ScontoFidelity(),
	ScontoTemporale()
	]
	
	lista_vincoli = [
	VincoloEtaGruppo(),
	VincoloEsclusione([])
	]
	
	gestore_sconti = GestoreSconti(
	lista_sconti=crea_sconti(),
	vincoli=crea_vincoli()
	)

*Creazione ordine*

	sistema_ordini = SistemaOrdini(gestore_sconti, CatalogoPizze())
	cliente = Cliente(nome="Mario Rossi", eta=10, fidelity_card=True)
	ordine = Ordine(numero_tavolo=1, numero_ordine=1, cliente=cliente, num_persone=10)
	pizza1 = Pizza("Margherita", 10)
	pizza2 = Pizza("Capricciosa", 12)
	ordine_finale = sistema_ordini.crea_ordine(ordine)

*Output*

	print(ordine_finale)
	print(sistema_ordini.sconti_applicati_ordine())

*Output generato*

	Ordine 1 per il tavolo 1
	Cliente: Mario Rossi
	├─ Età: 10 anni
	├─ Fidelity Card: Attiva
	├─ Disabile: No
	└─ Gruppo: 10 persone
	
	Pizze ordinate:
	
	Margherita: 10.00 €
	Capricciosa: 12.00 €
	
	Prezzo scontato:
	
	Margherita: 6.80 €
	Capricciosa: 8.16 € 


## Note

*   Il codice è commentato per facilitarne la comprensione.
*   L'input dei dati è simulato nel codice, ma può essere facilmente adattato per ricevere input dall'utente.
