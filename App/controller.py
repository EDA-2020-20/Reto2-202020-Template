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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""
def initCatalog():
    catalog = model.newCatalog()
    return catalog

def loadData(catalog, detailsFile, castingsFile):
    loadMoviesDetails(catalog, detailsFile)
    loadMoviesCasting(catalog, castingsFile)

def loadMoviesDetails(catalog, file):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row:
            model.addMovieDetails(catalog, elemento)
            name = elemento["id"]
            model.addMovieIdDetail(catalog, name, elemento)
            productionCompany = elemento["production_companies"]
            model.addMovieProductionCompany(catalog, productionCompany, elemento)
            genres = elemento["genres"]
            genreLst = genres.split("|")
            for genero in genreLst:
                model.addGenre(catalog, genero, elemento)
            country = elemento["production_countries"]
            model.addCountry(catalog, country, elemento)
            
def loadMoviesCasting(catalog, file):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            model.addMovieCasting(catalog, elemento)
            name = elemento["id"]
            model.addMovieIdCasting(catalog, name, elemento)
            director = elemento["director_name"]
            movieDirectorId = elemento["id"]
            model.addDirector(catalog, director, movieDirectorId)
            actor1 = elemento["actor1_name"]
            actor2 = elemento["actor2_name"]
            actor3 = elemento["actor3_name"]
            actor4 = elemento["actor4_name"]
            actor5 = elemento["actor5_name"]
            movieActorId = elemento["id"] 
            model.addActor(catalog, actor1, movieActorId)
            model.addActor(catalog, actor2, movieActorId)
            model.addActor(catalog, actor3, movieActorId)
            model.addActor(catalog, actor4, movieActorId)
            model.addActor(catalog, actor5, movieActorId)
        
def getMoviesByProductionCompany(catalog, companyName):
    moviesByCompany = model.getMoviesByProductionCompany(catalog, companyName)
    return moviesByCompany

def getMoviesByDirector(catalog, directorName):
    moviesByDirector = model.getMoviesByDirector(catalog, directorName)
    return moviesByDirector

def getMoviesByActor(catalog, actorName):
    moviesByActor = model.getMoviesByActor(catalog, actorName)
    return moviesByActor

def getMoviesByGenre(catalog, genreName):
    moviesByGenre = model.getMoviesByGenre(catalog, genreName)
    return moviesByGenre

def getMoviesByCountry(catalog, countryName):
    moviesByCountry = model.getMoviesByCountry(catalog, countryName)
    return moviesByCountry

def linkIdToMovieDetail(catalog, movieId):
    idToMovie = model.linkIdToMovieDetail(catalog, movieId)
    return idToMovie

def linkIdToMovieCasting(catalog, movieId):
    idToMovie = model.linkIdToMovieCasting(catalog, movieId)
    return idToMovie
#Size
def detailsSize(lst):
    return model.detailsSize(lst)

def castingsSize(lst):
    return model.castingsSize(lst)

def DirectorSize(catalog, directorName):
    return model.DirectorSize(catalog, directorName)

def actorSize(catalog, actorName):
    return model.actorSize(catalog, actorName)

def companyMoviesSize(catalog, companyName):
    return model.companyMoviesSize(catalog, companyName)

def genreMoviesSize(catalog, genreName):
    return model.genreMoviesSize(catalog, genreName)

#Average
def averageByProductionCompany(catalog, companyName):
    return model.averageByProductionCompany(catalog, companyName)

def averageByDirector(catalog, directorName):
    return model.averageByDirector(catalog, directorName)

def averageByGenre(catalog, genreName):
    return model.averageByGenre(catalog, genreName)

def averageByActor(catalog, actorName):
    return model.averageByActor(catalog, actorName)