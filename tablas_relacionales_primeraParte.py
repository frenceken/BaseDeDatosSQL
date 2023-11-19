"""Relacionar Tablas primera parte"""
import sqlite3

ruta = "C:/Users/Fzel1/Documents/BASEDEDATOS/SalaDeVideos.db"
conectar = sqlite3.connect(ruta)

cursor = conectar.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS SalaDeVideos(
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NOMBRE" TEXT,
    "GENERO" TEXT,
    "DURACION" TEXT,
    "AÑO" INTEGER,
    "PROTAGONISTAS" TEXT,
    "PAIS" TEXT
)""")
conectar.commit()

cursor.execute("""INSERT INTO SalaDeVideos(NOMBRE, GENERO, DURACION, AÑO, 
PROTAGONISTAS, PAIS) VALUES("Passengers", "Ciencia Ficcion/Romance", "1h 56m", 
2016, "Jennifer Lawrence/Chris Pratt/Michael Sheen", "EEUU")""")
conectar.commit()

conectar.close()

ruta = "C:/Users/Fzel1/Documents/BASEDEDATOS/SalaDeVideos.db"

conectar = sqlite3.connect(ruta)
cursor = conectar.cursor()

cursor.execute("""INSERT INTO SalaDeVideos(NOMBRE, GENERO, DURACION, AÑO,
PROTAGONISTAS, PAIS) VALUES("Interstellar", "Ciencia Ficcion/Drama", "2h 49m",
2014, "Matthew McConaughey/Jessica Chastain/Anne Hathaway", "EEUU")""")
conectar.commit()

cursor.execute("SELECT * FROM SalaDeVideos")
lista_videos = cursor.fetchall()
for videos in lista_videos:
    print(videos)

conectar.close()
