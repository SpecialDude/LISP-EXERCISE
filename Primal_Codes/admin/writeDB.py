import shelve, os, shutil, decipher

import ceaser


tamperCode = open('tamperCheck.py', 'r').read()
decipherCode = open('decipher.py', 'r').read()
questionsObject = open('plain_question.txt', 'r')
questions = questionsObject.readlines()
questionsObject.close()

questions = [ceaser.ceaser_cipher(i) for i in questions]

shelvefile = shelve.open('Program Data')
shelvefile['main'] = ceaser.ceaser_cipher(open('main.py', 'r').read())
shelvefile['cdatabase'] = tamperCode
shelvefile['decipher'] = decipherCode
shelvefile['grace'] = 3
shelvefile['questions'] = questions




#print(ceaser_decipher(shelvefile['main']) == open(mainCodePath, 'r').read())

def load_question():
    testfile = open('plain_question.txt', 'r')
    myTest = testfile.readlines()
    testQ = {}

    for i in range(len(myTest)):
        question = myTest[i].split('&&')[:-1]
        testQ[i+1] = question


    shelvefile = shelve.open('mydata')
    shelvefile['testQ'] = testQ

    shelvefile.close()


shelvefile.close()
print('Writing Completed')

