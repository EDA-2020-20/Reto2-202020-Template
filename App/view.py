"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
moviesDetails = "Data/SmallMoviesDetailsCleaned.csv"
moviesCasting = "Data/MoviesCastingRaw-small.csv"




# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
def printMenu ():
    print("Bienvenido")
    print("1. Cargar Datos")
    print("2. Descubrir productoras de cine")
    print("3. Conocer a un director")
    print("4. Conocer a un actor")
    print("5. Entender un género cinematográfico")
    print("6. Encontrar películas por país") 
    print("0. Salir")
# ___________________________________________________

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Cargando datos ....")
        details = controller.loadMoviesDetails(moviesDetails)
        castings = controller.loadMoviesCasting(moviesCasting)
        detailsSize = controller.detailsSize(details)
        castingsSize = controller.castingsSize(castings)
        print("Se cargaron: "+str(detailsSize)+" datos")
        print("Se cargaron: "+str(castingsSize)+" datos")
        print(lt.firstElement(details)["original_title"])
        print(lt.firstElement(details)["release_date"])
        print(lt.firstElement(details)["vote_average"])
        print(lt.firstElement(details)["vote_count"])
        print(lt.firstElement(details)["original_language"])
        print(" ")
        print(lt.lastElement(details)["title"])
        print(lt.lastElement(details)["release_date"])
        print(lt.lastElement(details)["vote_average"])
        print(lt.lastElement(details)["vote_count"])
        print(lt.lastElement(details)["original_language"])

    elif int(inputs[0]) == 2:
        print("Opción aún no disponible")

    elif int(inputs[0]) == 3:
        print("Opción aún no disponible")

    elif int(inputs[0]) == 4:
        print("Opción aún no disponible")

    elif int(inputs[0]) == 5:
        print("Opción aún no disponible")
    
    elif int(inputs[0]) == 6:
        print("Opción aún no disponible")
    else:
        sys.exit(0)
sys.exit(0)
