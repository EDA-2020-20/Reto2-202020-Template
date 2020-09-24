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

#Catalogo de TADs
def newCatalog():
    catalog = {"details": None, "castings": None, "productionCompanies": None}
    catalog["details"] = lt.newList("SINGLE_LINKED", compareMovies)
    catalog["castings"] = lt.newList("SINGLE_LINKED", compareMovies)
    catalog["moviesIds"] = mp.newMap(4003, 109345121, "CHAINING", 0.4, compareMoviesId)
    catalog["productionCompanies"] = mp.newMap(4003, 109345121, "CHAINING", 0.4, compareProductionCompanies)
    catalog["directors"] = mp.newMap(2003, 109345121, "CHAINING", 0.4, compareDirectors)
    catalog["actors"] = mp.newMap(2003, 109345121, "CHAINING", 0.4, compareActors)
    catalog["genres"] = mp.newMap(2003, 109345121, "CHAINING", 0.4, compareGenres)
    catalog["productionCountries"] = mp.newMap(2003, 109345121, "CHAINING", 0.4, compareProductionCountries)
 
    
    return catalog

def newMovieId(name):
    movieId = {"id": "", "detail": None, "casting": None}
    movieId["id"] = name 
    return movieId

def newProductionCompany(name):
    productionCompany = {"name": "", "movies": None, "vote_average": 0.0}
    productionCompany["name"] = name
    productionCompany["movies"] = lt.newList("SINGLE_LINKED", compareProductionCompanies)
    return productionCompany

def newDirector(name):
    director = {"name": "", "movies": None, "vote_average": 0.0}
    director["name"] = name
    director["movies"] = lt.newList("SINGLE_LINKED", compareDirectors)
    return director

def newActor(name):
    actor = {"name": "", "movies": None, "vote_average": 0.0}
    actor["name"] = name
    actor["movies"] = lt.newList("SINGLE_LINKED", compareActors)
    return actor

def newGenre(name):
    genre = {"name": "", "movies": None, "vote_count": 0.0}
    genre["name"] = name
    genre["movies"] = lt.newList("SINGLE_LINKED", compareGenres)
    return genre

def newProductionCountry(name):
    country = {"name": "", "movies": None}
    country["name"] = name
    country["movies"] = lt.newList("SINGLE_LINKED", compareGenres)
    return country
#Agregar datos
def addMovieDetails(catalog, movie):
    lt.addLast(catalog["details"], movie)

def addMovieCasting(catalog, movie):
    lt.addLast(catalog["castings"], movie)
    
def addMovieIdDetail(catalog, name, elemento):
    movieIds = catalog["moviesIds"]   
    exists = mp.contains(movieIds, name)
   
    if exists:
       
        entry = mp.get(movieIds, name)
        movieId = me.getValue(entry)
        movieId["detail"] = elemento
    else:
        
        movieId = newMovieId(name)
        mp.put(movieIds, name, movieId)
        movieId["detail"] = elemento     
    

def addMovieIdCasting(catalog, name, elemento):
    movieIds = catalog["moviesIds"]   
    exists = mp.contains(movieIds, name)
   
    if exists:
       
        entry = mp.get(movieIds, name)
        movieId = me.getValue(entry)
        movieId["casting"] = elemento
    else:
        
        movieId = newMovieId(name)
        mp.put(movieIds, name, movieId)
        movieId["casting"] = elemento  
      

def addDirector(catalog, directorName, movieId):
    directors = catalog["directors"]
    
    exists = mp.contains(directors, directorName)
   
    if exists:
       
        entry = mp.get(directors, directorName)
        director = me.getValue(entry)
        lt.addLast(director["movies"], movieId)
    else:
        
        director = newDirector(directorName)
        mp.put(directors, directorName, director)
        lt.addLast(director["movies"], movieId)
    directorAvg = director["vote_average"]
    size = lt.size(director["movies"])
    movieDetails = linkIdToMovieDetail(catalog, movieId)
    movieAvg = movieDetails["vote_average"]
    if (directorAvg == 0.0):
        director['vote_average'] = float(movieAvg)
       
    else:
        
        director['vote_average'] = (directorAvg + float(movieAvg)) / 2


def addActor(catalog, actorName, movieId):
    actors = catalog["actors"]
    exists = mp.contains(actors, actorName)
   
    if exists:
       
        entry = mp.get(actors, actorName)
        actor = me.getValue(entry)
        lt.addLast(actor["movies"], movieId)
    else:
        
        actor = newActor(actorName)
        mp.put(actors, actorName, actor)
        lt.addLast(actor["movies"], movieId)

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

def addGenre(catalog, genreName, movie):
    genres = catalog["genres"]
  
    exists = mp.contains(genres, genreName)
   
    if exists:
       
        entry = mp.get(genres, genreName)
        genre = me.getValue(entry)
        lt.addLast(genre["movies"], movie)
    else:
        
        genre = newGenre(genreName)
        mp.put(genres, genreName, genre)
        lt.addLast(genre["movies"], movie)
    genreAvg = genre['vote_count']
    movieAvg = movie['vote_count']
    if (genreAvg == 0.0):
        genre['vote_count'] = float(movieAvg)
       
    else:
        
        genre['vote_count'] = (genreAvg + float(movieAvg)) / 2

def addCountry(catalog, countryName, movie):
    countries = catalog["productionCountries"]
  
    exists = mp.contains(countries, countryName)
   
    if exists:
       
        entry = mp.get(countries, countryName)
        country = me.getValue(entry)
        lt.addLast(country["movies"], movie)
    else:
        
        country = newGenre(countryName)
        mp.put(countries, countryName, country)
        lt.addLast(country["movies"], movie)

#Funciones
def getMoviesByProductionCompany(catalog, companyName):
    productionCompany = mp.get(catalog["productionCompanies"], companyName)
    if productionCompany:
        return me.getValue(productionCompany)
    return None

def getMoviesByDirector(catalog, directorName):
    director = mp.get(catalog["directors"], directorName)
    if director:
        return me.getValue(director)
    return None

def getMoviesByActor(catalog, actorName):
    actor = mp.get(catalog["actors"], actorName)
    if actor:
        return me.getValue(actor)
    return None

def getMoviesByGenre(catalog, genreName):
    genre = mp.get(catalog["genres"], genreName)
    if genre:
        return me.getValue(genre)
    return None

def getMoviesByCountry(catalog, countryName):
    country = mp.get(catalog["productionCountries"], countryName)
    if country:
        return me.getValue(country)
    return None

def linkIdToMovieCasting(catalog, movieId):
    entry = mp.get(catalog["moviesIds"], movieId)
    movie = me.getValue(entry)
    movieCasting = movie["casting"]
    if entry:
        return movieCasting
    return None

def linkIdToMovieDetail(catalog, movieId):
    entry = mp.get(catalog["moviesIds"], movieId)
    movie = me.getValue(entry)
    movieDetail = movie["detail"]
    if entry:
        return movieDetail
    return None
#Size
def detailsSize(lst):
    return lt.size(lst)

def castingsSize(lst):
    return lt.size(lst)

def companyMoviesSize(catalog, companyName):
    entry = mp.get(catalog["productionCompanies"], companyName)
    lst = me.getValue(entry)
    return lt.size(lst["movies"])

def DirectorSize(catalog, directorName):
    entry = mp.get(catalog["directors"], directorName)
    lst = me.getValue(entry)
    return lt.size(lst["movies"])

def actorSize(catalog, actorName):
    entry = mp.get(catalog["actors"], actorName)
    lst = me.getValue(entry)
    return lt.size(lst["movies"])

def genreMoviesSize(catalog, genreName):
    entry = mp.get(catalog["genres"], genreName)
    lst = me.getValue(entry)
    return lt.size(lst["movies"])
#Average
def averageByProductionCompany(catalog, companyName):
    entry = mp.get(catalog["productionCompanies"], companyName)
    lst = me.getValue(entry)
    return lst["vote_average"]

def averageByDirector(catalog, directorName):
    entry = mp.get(catalog["directors"], directorName)
    lst = me.getValue(entry)
    return lst["vote_average"]

def averageByActor(catalog, actorName):
    entry = mp.get(catalog["actors"], actorName)
    lst = me.getValue(entry)
    return lst["vote_average"]

def averageByGenre(catalog, genreName):
    entry = mp.get(catalog["genres"], genreName)
    lst = me.getValue(entry)
    return lst["vote_count"] 

#Comparaciones
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

def compareDirectors(keyname, director):
    directorEntry = me.getKey(director)
    if (keyname == directorEntry):
        return 0
    elif (keyname > directorEntry):
        return 1
    else:
        return -1

def compareActors(keyname, actor):
    actorEntry = me.getKey(actor)
    if (keyname == actorEntry):
        return 0
    elif (keyname > actorEntry):
        return 1
    else:
        return -1

def compareGenres(keyname, genre):
    genreEntry = me.getKey(genre)
    if (keyname == genreEntry):
        return 0
    elif (keyname > genreEntry):
        return 1
    else:
        return -1

def compareProductionCountries(keyname, productionCountry):
    countryEntry = me.getKey(productionCountry)
    if (keyname == countryEntry):
        return 0
    elif (keyname > countryEntry):
        return 1
    else:
        return -1

def compareMoviesId(keyname, movieId):
    movieIdEntry = me.getKey(movieId)
    if (keyname == movieIdEntry):
        return 0
    elif (keyname > movieIdEntry):
        return 1
    else:
        return -1