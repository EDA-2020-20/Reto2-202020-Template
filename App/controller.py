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
            productionCompanies = elemento["production_companies"]
            model.addMovieProductionCompany(catalog, productionCompanies, elemento)
                
def loadMoviesCasting(catalog, file):
    dialect = csv.excel()
    dialect.delimiter=";"
    with open(file, encoding="utf-8") as csvfile:
        row = csv.DictReader(csvfile, dialect=dialect)
        for elemento in row: 
            model.addMovieCasting(catalog, elemento)

def getMoviesByProductionCompany(catalog, companyName):
    moviesByCompany = model.getMoviesByProductionCompany(catalog, companyName)
    return moviesByCompany
    
def detailsSize(lst):
    return model.detailsSize(lst)

def castingsSize(lst):
    return model.castingsSize(lst)

def companyMoviesSize(catalog, companyName):
    return model.companyMoviesSize(catalog, companyName)

def averageByProductionCompany(catalog, companyName):
    return model.averageByProductionCompany(catalog, companyName)