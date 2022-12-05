import os, shelve

print(os.listdir())

shelveFile = shelve.open(os.path.join('.', 'mydata'))

print(shelveFile['grace'])