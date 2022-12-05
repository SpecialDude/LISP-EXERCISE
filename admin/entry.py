import shelve, os


with shelve.open("Program Data") as shelffile:
    cdatabase = shelffile["duhhh!"]
    database = shelffile["ta-dah!"]

with open("decipher.py", 'w') as dsFile:
    dsFile.write(cdatabase)

import decipher

with open("database.py", 'w') as dsFile:
    dsFile.write(decipher.decipher(database))

import database

testQuestions = database.testQuestions