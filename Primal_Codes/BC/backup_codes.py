import shelve, os

shelveFile = shelve.open('mydata')
backupCode = shelveFile['main']
grace = shelveFile['grace']

decipherFile = open('decipher.py', 'w')
decipherFile.write(shelveFile['decipher'])
decipherFile.close()

from decipher import *

backupCode = decipher(backupCode)
mainCodeObj = open('main.py', 'r')
mainCode = mainCodeObj.read()
mainCodeObj.close()

if mainCode == backupCode:
    pass
else:
    import time
    from platform import system as ostype
    grace -= 1
    def clear_screen():
        if ostype() == 'Linux' or ostype() == 'Darwin':
            os.system('clear')
        elif ostype() == 'Windows':
            os.system('cls')
    if grace <= 0:
        clear_screen()
        print('You have tampared with this program, program will now SELF-DESTRUCT')
        time.sleep(3)
        for i in range(5, -1, -1):
            clear_screen()
            print(f'SELF-DESTRUCT in {i}')
        mainFile = open('main.py', 'w')
        mainFile.write('Code Destroyed, Contact AWA for rectification!!!Code Destroyed, Contact AWA for rectification!!!\n'*100)
        mainFile.close()
        print('Program Destroyed, Contact Warith for repairs!!!')
    elif  grace > 0:
        clear_screen()
        shelveFile['grace'] = grace
        print('Code Tampered!!')
        time.sleep(2)
        print(f'Code will SELF-DESTRUCT if tampered with, {grace} more time(s)')
        time.sleep(2)
        print('Code will now be restored!!!')
        time.sleep(2)
        print('Restoring...')
        for i in range(5):
            print('.', end=' ')
            time.sleep(1.5)
        mainCodeObj = open('main.py', 'w')
        mainCodeObj.write(backupCode)
        mainCodeObj.close()
        print('\nRestoring Completed!!!')
        print('Run the "main.py" file to start again')

shelveFile.close()     
os.remove('decipher.py')
try:
    os.remove('cdatabase.py')
except FileNotFoundError:
    pass




#Exercises on Vectors
import shelve


class MyTest:
    def __init__(self):
        self.__load__()
        #self.NUM_OF_QUESTION = len(self.testQ)

    def __load__(self):
        shelvefile = shelve.open('Program Data')
        database = open('cdatabase.py', 'w')
        database.write(shelvefile['cdatabase'])
        database.close()
        import cdatabase.py
        #self.testQ = shelvefile['testQ']

    def check(self, status):
        if not status:
            raise Exception('Code Tampered With!!!')

    def display_instruction(self):
        print(f'\nINSTRUCTION: The test contains {self.NUM_OF_QUESTION} multiple choice questions')
        print('             Choose option A, B or C by entering A, B or C and press Enter')
        print('             You can enter a question number to go to that question')
    
    def run(self):
        print('<<<<<<<<< LISP >>>>>>>>>')
        print('Welcome to a test practice on Vector')
        self.display_instruction()
        input('\nPress Enter to start Test')
        

k = MyTest()
k.run()