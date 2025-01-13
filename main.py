meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'XD':'Una cara riendose, se usa como respuesta a algo gracioso',
            'CREEPY':  'aterrador, siniestro'
            }
while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas! y escriba 'S' para salir): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    elif word=='S':
        break
    else:
        print('La palabra no esta disponible')    
    
