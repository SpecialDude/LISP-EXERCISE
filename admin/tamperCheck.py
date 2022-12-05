import shelve, os, sys, shutil

shelveFile = shelve.open('Program Data')
backupCode = shelveFile['eweeeey!']
grace = shelveFile['grace']

from decipher import *

try:
    os.remove('decipher.py')
    os.remove('cdatabase.py')
    os.remove('database.py')
    shutil.rmtree('__pycache__')
except:
    pass 

backupCode = decipher(backupCode)
mainCodeObj = open('main.py', 'r')
mainCode = mainCodeObj.read()
mainCodeObj.close()

state = False

if mainCode == backupCode:

    def load_question(subjects):
        testQ = {}
        for subject in subjects:
            questions = shelveFile[subject]
            questions = decipher(questions)
            subject = decipher(subject)

            questions = questions.rstrip().split('\n')
            questions = {i+1 : questions[i].split('&&')[:-1] for i in range(len(questions))}

            testQ[subject] = questions
        return testQ

    state = True

    subjects = shelveFile['subjects']
    testQuestions = load_question(subjects)
    
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
        try:
            datafiles = [file for file in os.listdir() if file.startswith('Program Data')]
            for file in datafiles:
                os.remove(file)
        except FileNotFoundError:
            pass    
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
        print('\nRun the \'main.py\' file to restart the program')
        
        
shelveFile.close()     

if not state:
    sys.exit()
