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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""
def newCatalog():
    catalog = {"details": None, "castings": None, "productionCompanies": None}
    catalog["details"] = lt.newList("SINGLE_LINKED", compareMovies)
    catalog["castings"] = lt.newList("SINGLE_LINKED", compareMovies)
    catalog["productionCompanies"] = mp.newMap(4003, 109345121, "CHAINING", 0.4, compareProductionCompanies) 
    
    return catalog

def newProductionCompany(name):
    productionCompany = {"name": "", "movies": None, "vote_average": 0.0}
    productionCompany["name"] = name
    productionCompany["movies"] = lt.newList("SINGLE_LINKED", compareProductionCompanies)
    return productionCompany

def addMovieDetails(catalog, movie):
    lt.addLast(catalog["details"], movie)

def addMovieCasting(catalog, movie):
    lt.addLast(catalog["castings"], movie)

def addMovieProductionCompany(catalog, companyName, movie):
    companies = catalog["productionCompanies"]
  
    exists = mp.contains(companies, companyName)
   
    if exists:
       
        entry = mp.get(companies, companyName)
        productionCompany = me.getValue(entry)
        lt.addLast(productionCompany["movies"], movie)
    else:
        
        productionCompany = newProductionCompany(companyName)
        mp.put(companies, companyName, productionCompany)
        lt.addLast(productionCompany["movies"], movie)
    companyAvg = productionCompany['vote_average']
    movieAvg = movie['vote_average']
    if (companyAvg == 0.0):
        productionCompany['vote_average'] = float(movieAvg)
       
    else:
        
        productionCompany['vote_average'] = (companyAvg + float(movieAvg)) / 2

def getMoviesByProductionCompany(catalog, companyName):
    productionCompany = mp.get(catalog["productionCompanies"], companyName)
    if productionCompany:
        return me.getValue(productionCompany)
    return None

def detailsSize(lst):
    return lt.size(lst)

def castingsSize(lst):
    return lt.size(lst)

def averageByProductionCompany(catalog, companyName):
    entry = mp.get(catalog["productionCompanies"], companyName)
    lst = me.getValue(entry)
    return lst["vote_average"]

def companyMoviesSize(catalog, companyName):
    entry = mp.get(catalog["productionCompanies"], companyName)
    lst = me.getValue(entry)
    return lt.size(lst["movies"])

def compareProductionCompanies(keyname, productionCompany):
    companyEntry = me.getKey(productionCompany)
    if (keyname == companyEntry):
        return 0
    elif (keyname > companyEntry):
        return 1
    else:
        return -1

def compareMovies(movie1, movie2):
    if (movie1 == movie2):
        return 0
    elif movie1 > movie2:
        return 1
    else:
        return -1

