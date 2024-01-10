"""
"Fare uno script per sostituire caratteri e cancellare righe a caso da un set di file in un directory, e tutte le relative sottodirectory,
filtrando solo per i file con delle determinate estensioni.
I caratteri sono sostituiti con un altro carattere random, e le righe cancellate random in percentuale e specificando un numero minimo.
Lo scopo è fornire dei codici sorgenti inutilizzabili, ma riconoscibili, almeno in parte."

Esempi di chiamate, e output aspettato:

cancella_righe(estensioni= [".js",".txt"], perc_lines = 4, perc_chars = 6, directory= "/path/to/directory")
=> cancella il 4% di righe random e sostituisce il 6% di caratteri con caratteri random nei file .js e .txt del path passato

cancella_righe(directory= "/path/to/directory")
=> se non passiamo dei parametri, i valori di default sono i seguenti:
	cancelliamo il 5% delle righe in tutti i file e sostituiamo il 5% dei caratteri con caratteri casuali a prescindere dall'estensione,
	nella directory passata. Passare una directory è invece obbligatorio, altrimenti lo script non parte e ritorna un errore.
	
Puoi usare qualunque linguaggio di programmazione, ti consiglio o Python 3 o Javascript con node. Per la consegna puoi tranquillamente creare uno snippet o un progetto su github, e mandarmi il relativo link.
Buona fortuna
"""

import os
import random


def cancella_righe(directory, estensioni=[], perc_lines=5, perc_chars=5):

    if (not os.path.isdir(directory)):
        print("Errore: Il percorso indicato non si riferisce ad una cartella")
        return

    os.chdir(directory)

    lista_dir = os.listdir()

    if(len(estensioni) == 0):

        for file in lista_dir:

            if (os.path.isfile(file)):
                with open(file, 'r') as f:
                    numero_linee = len(f.readlines())
                    f.seek(0)
                    numero_char = len(f.read())
                f.close()

                print("Il file: " + file + " è ha " + str(numero_linee) + " linee e "  + str(numero_char) + " caratteri")

                modifica_file(perc_lines, perc_chars, numero_linee, numero_char, file)

        for file in lista_dir:

            if(os.path.isdir(file)):
                cancella_righe(file, estensioni, perc_lines, perc_chars)

    else:
        for estensione in estensioni:

            for file in lista_dir:

                if (file.endswith(estensione) and os.path.isfile(file)):
                    with open(file, 'r') as f:
                        numero_linee = len(f.readlines())
                        f.seek(0)
                        numero_char = len(f.read())
                    f.close()

                    print("Il file: " + file + " ha " + str(numero_linee) + " linee e "  + str(numero_char) + " caratteri")

                    modifica_file(perc_lines, perc_chars, numero_linee, numero_char, file)

        for file in lista_dir:

            if (os.path.isdir(file)):
                cancella_righe(file, estensioni, perc_lines, perc_chars)





def modifica_file(perc_lines, perc_chars, numero_linee, numero_char, file):

    linee_da_eliminare = int(perc_lines*numero_linee/100)
    caratteri_da_modificare = int(perc_chars * numero_char / 100)

    print("Elimino "+str(linee_da_eliminare)+" linee e modifico "+str(caratteri_da_modificare)+" caratteri")

    f = open(file, 'r')
    linee = f.readlines()
    f.close()

    for i in range(0, caratteri_da_modificare):
        index_linea_da_modificare = random.randrange(len(linee))
        index_char_da_modificare = random.randrange(len(linee[index_linea_da_modificare]))

        caratteri_in_linea = list(linee[index_linea_da_modificare])

        caratteri_in_linea[index_char_da_modificare] = chr(random.randint(32, 125))
        linee[index_linea_da_modificare] = "".join(caratteri_in_linea)

    for i in range(0, linee_da_eliminare):
        index_da_eliminare = random.randrange(len(linee))
        del linee[index_da_eliminare]

    f = open(file, 'w')
    f.writelines(linee)
    f.close()

    print("Modifica Salvata \n")


#Test 1
#cancella_righe("C:/Users/aless/Desktop/Test_Dir/")

#Test 2
#cancella_righe("C:/Users/aless/Desktop/Test_Dir/", [".txt", ".c"], 8, 10)

#Test 3
#cancella_righe("C:/Users/aless/Desktop/Test_Dir/dsfs")


