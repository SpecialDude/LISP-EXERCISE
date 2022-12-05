import shelve, os

shelveFile = shelve.open(os.path.join('.', 'Program Data'))
shelveFile['grace'] = 4
shelveFile.close()
