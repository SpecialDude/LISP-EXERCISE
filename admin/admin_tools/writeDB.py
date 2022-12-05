import shelve, os, shutil

import ceaser

with open('./admin/tamperCheck.py', 'r') as code:
    tamperCode = ceaser.ceaser_cipher(code.read())
tamperID = "ta-dah!"  

with open('./admin/entry.py', 'r') as code:
    entryCode = code.read() 

with open('./admin/main.py', 'r') as code:
    mainCode = ceaser.ceaser_cipher(code.read())
mainID = "eweeeey!"

with open('./admin/decipher.py', 'r') as code:
    decipherCode = code.read()
decipherID = "duhhh!"

with open('./admin/program_files/subjects.txt') as subject_file:
    subjects = subject_file.read().rstrip().split('\n')


all_subjects = {}
ciphered_subject_list = []
for subject in subjects:
    with open(f"./admin/program_files/{subject}_questions.txt") as question_file:
        questions = ceaser.ceaser_cipher(question_file.read())
    subject = ceaser.ceaser_cipher(subject)
    ciphered_subject_list.append(subject)
    all_subjects[subject] = questions



# Writing to the database

shelvefile = shelve.open('./admin/Program Data')
shelvefile[mainID] = mainCode           # Encrypted
shelvefile[tamperID] = tamperCode       # Encrypted
shelvefile[decipherID] = decipherCode   # Unencrypted
shelvefile['cdatabase'] = entryCode     # Unencrypted
shelvefile['grace'] = 3                 # Unencrypted
shelvefile['subjects'] = ciphered_subject_list  # Encrypted

for subject, question in all_subjects.items():
    shelvefile[subject] = question              # Encrypted

shelvefile.close()
print('Writing Completed')

import deploy
exit()




#questionsObject = open('plain_question.txt', 'r')
#questions = questionsObject.readlines()
#questionsObject.close()
#questions = [ceaser.ceaser_cipher(i) for i in questions]

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

