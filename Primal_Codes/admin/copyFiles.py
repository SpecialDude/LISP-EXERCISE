import os, shutil, writeDB

shutil.copy('main.py', '..\\tbDeployed')
shutil.copy('Program Data.bak', '..\\tbDeployed')
shutil.copy('Program Data.dat', '..\\tbDeployed')
shutil.copy('Program Data.dir', '..\\tbDeployed')
print('All files copied succesfully')