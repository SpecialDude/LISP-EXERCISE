import shelve

shelveFile = shelve.open('Program Data')
decipherCode = shelveFile['decipher']

File = open('decipher.py', 'w')
File.write(decipherCode)
File.close()