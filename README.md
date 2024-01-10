# Test_Python
  
Fare uno script per sostituire caratteri e cancellare righe a caso da un set di file in un directory ed in tutte le relative sottodirectory, filtrando solo per i file con determinate estensioni.  
I caratteri sono sostituiti con un altri caratteri randomici,  
le righe sono cancellate in modo randomico in percentuale, specificando un numero minimo.  
Lo scopo è fornire dei codici sorgenti inutilizzabili, ma riconoscibili, almeno in parte.  
  
Esempi di chiamate e output aspettato:  
  
cancella_righe(estensioni= [".js",".txt"], perc_lines = 4, perc_chars = 6, directory= "/path/to/directory")  
=> cancella il 4% di righe in modo randomico e sostituisce il 6% di caratteri con caratteri randomici nei file .js e .txt del path passato  
  
  
cancella_righe(directory= "/path/to/directory")  
=> se non passiamo dei parametri,come in questo caso, i valori di default sono i seguenti:  
  si cancellino il 5% delle righe in tutti i file  
  si sostituiscano il 5% dei caratteri con caratteri randomici a prescindere dall'estensione, nella directory passata.  
  Passare una directory è invece obbligatorio, altrimenti lo script non parte e ritorna un errore.  
