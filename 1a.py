# 1a
este codigo fue hecho para crear mi primer repositorio
import this
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo terrorifico",
            }
word = input("Que palabra no entiendes? (Escribe con mayusculas): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No conozco esa palabra")
