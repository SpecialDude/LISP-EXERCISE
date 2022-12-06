# CBT Simulator
# Author:  ADETAYO


from platform import system as ostype
import os, shelve, random, time
from string import ascii_uppercase
from datetime import datetime


class MyTest:
    def __init__(self, subject:str, questions:dict, subject_info = None, duration:int = None):
        self.subject = subject
        self.testQ = questions
        self.duration = duration
        self.subject_info = subject_info

        self.NUM_OF_QUESTION = len(self.testQ)
        self.optionTag = {i+1:ascii_uppercase[i] for i in range(5) }

    def display_instruction(self):
        print(f'\nINSTRUCTION: The test contains {self.NUM_OF_QUESTION} multiple choice questions')
        print('             Choose option A, B or C by entering A, B or C and press Enter')
        print('             You can enter a question number to go to that question')
        print('             \'P\' or \'N\' to go to Previous or Next Question')
        print('             And \'S\' to submit')
        input('\nPress Enter to continue')
        U.cls()

    def __startTest__(self):
        self.userAnswers = {}
        questionOrder = list(self.testQ.keys())
        random.shuffle(questionOrder)

        i = 0
        while i < self.NUM_OF_QUESTION:
            answer = self.userAnswers.get(questionOrder[i])
            print(f'Question {i + 1}{(lambda x: "" if not x else (" (Answered: " + x + ")"))(answer)}\n')

            print(self.testQ[questionOrder[i]][0])
            options = self.testQ[questionOrder[i]][1:-1]

            random.shuffle(options)
            print()

            for optionNumber in range(len(options)):
                print(f'    {ascii_uppercase[optionNumber]}.) {options[optionNumber]}')
            print()

            self.option_inputs = {ascii_uppercase[j]:j for j in range(len(options))}

            userIn = self.__validateUserInput__(i)

            if isinstance(userIn, int):
                i = userIn - 1
            else:
                try:
                    self.userAnswers[questionOrder[i]] = options[self.option_inputs[userIn]]
                except:
                    if self.__confirmsubmit__():
                        break
                    i -= 1

            i += 1
            if i == self.NUM_OF_QUESTION:
                if not self.__confirmsubmit__():
                    i -= 1
            U.cls()

        point = 0
        testSummary = {}
        for i in range(self.NUM_OF_QUESTION):
            user_answer = self.userAnswers.get(i+1)
            if user_answer == self.testQ[i+1][-1]:
                point += 1
                comment = 'Right'
            else:
                comment = 'Wrong'
            testSummary[i+1] = (self.testQ[i+1][0], user_answer, comment)

        print('\nTest Ended and Recorded!!!')
        print(f'\nYour score: {point}/{self.NUM_OF_QUESTION}')
        self.testSummary = {'Subject':self.subject, 'Score':round((point/self.NUM_OF_QUESTION) * 100, 2), 'Summary':testSummary, 'Date':datetime.now()}

    def __confirmsubmit__(self):
        answered = self.NUM_OF_QUESTION - len(self.userAnswers)
        print('Submit Test?' + (lambda x: '' if x == 0 else f'(You have {x} unanswered questions)')(answered))
        U.display_options(['Yes', 'No'])
        return U.u_input(2) == 1


    def __validateUserInput__(self, i):
        idiot_proof = 0
        m = {'P' : lambda : i - 1, 'N': lambda : i + 1}
        while True:
            userIn = input(': ')
            idiot_proof += 1
            try:
                userIn = int(userIn)
                if userIn >= 1 and userIn <= self.NUM_OF_QUESTION:
                    return userIn - 1
            except:
                userIn = userIn.upper()
                if userIn in self.option_inputs:
                    return userIn
                elif  userIn == 'P':
                    if i == 0:
                        print('You are at the first Question')
                        continue
                    return i - 1
                elif userIn == 'N':
                    if i == self.NUM_OF_QUESTION - 1:
                        print('You are at the last Question')
                        print('Enter \'S\' to Submit')
                        continue
                    return i + 1
                elif userIn == 'S':
                    return userIn

            print('\nInvalid Input!!!')
            if idiot_proof > 2:
                print(f'Enter options ({", ".join(list(self.option_inputs.keys()))})\t\tOR')
                print(f'Enter a question number (1 - {self.NUM_OF_QUESTION})\t\tOR')
                print('Enter \'P\' or \'N\' to go to Previous or Next Question\tOR')
                print('Enter \'S\' to submit')
                print()
                idiot_proof = 0

    def run(self):
        U.cls()
        print(f'Welcome to a test practice on {self.subject}\n')
        if self.subject_info:
            print(self.subject_info + '\n')
            time.sleep(1)
        self.display_instruction()
        for i in range(3,-1, -1):
            print(f'Test start in {i}')
            time.sleep(1)
            U.cls()
        self.__startTest__()


class Utility:

    @staticmethod
    def display_options(list_of_options, header=None):
        pad = ""
        if header:
            print(header)
            pad = "\t"

        for i in range(len(list_of_options)):
            print(f"{pad}{i + 1}. {list_of_options[i]}")

    @staticmethod
    def u_input(max, prompt=': '):
        while True:
            userin = input(prompt)

            try:
                userin = int(userin)
                if userin < 1 or userin > max:
                    print('Invalid input: ')
                    continue
                break
            except:
                print('Pls input a number from the listed above')
        return userin

    @staticmethod
    def cls():
        if ostype() == 'Linux' or ostype() == 'Darwin':
            os.system('clear')
        elif ostype() == 'Windows':
            os.system('cls')


def load():
    shelvefile = shelve.open('Program Data')
    database = open('cdatabase.py', 'w')
    database.write(shelvefile['cdatabase'])
    database.close()
    import cdatabase
    return cdatabase.testQuestions

def selectSubject(testQuestions :dict, default=False):
    if default:
        for subject in testQuestions:
            return subject, testQuestions[subject]
    U.cls()
    print("Select a Subject from list below.")
    subjects = list(testQuestions.keys())
    U.display_options(subjects)
    userin = U.u_input(len(subjects))
    return subjects[userin-1], testQuestions[subjects[userin-1]]

def previousScores():
    U.cls()
    with shelve.open('User Data') as userdata:
        test_records = userdata.get('TestRecords')
    if not test_records:
        print("You have no test record,\nGoto the main menu to take a test")
    else:
        for i in range(len(test_records)):
            print(f'{i + 1}. Subject: {test_records[i]["Subject"]}')
            print(f'\tTest taken on {test_records[i]["Date"]}')
            print(f'\tScore: {test_records[i]["Score"]}%\n')

    input('\nPress Enter to continue to the main menu')

def updateName():
    global userName
    oldusername = userName
    U.cls()
    username = input("\nEnter a new Username: ")
    if username == oldusername:
        print("You want to mess with me right hun?\n")
        time.sleep(2)
        return
    with shelve.open('User Data') as userdata:
        userdata['username'] = username
    userName = username
    print(f"Username Changed {oldusername} --> {username}")
    input('\nPress Enter to continue to the main menu')

def takeTest(*params):
    subject, questions = selectSubject(*params[:2])
    test = MyTest(subject, questions)
    test.run()
    test_summary = test.testSummary
    with shelve.open('User Data') as userdata:
        test_records = userdata.get('TestRecords')
        if not test_records:
            test_records = []
        test_records.append(test_summary)
        userdata['TestRecords'] = test_records
    input('Press Enter to continue to the main menu')

def main():
    U.cls()
    test_questions = load()

    with shelve.open('User Data') as userdata:
        global userName
        userName = userdata.get('username')

    if userName == None:
        print('WELCOME!, new individual\nThis is a CBT Simulator Program')
        print('\nPlease Enter your Name (more like a username)')
        userName = input(': ')

        with shelve.open('User Data') as userdata:
            userdata['username'] = userName

        print(f'\nThank you {userName}')
        print('Press Enter to Proceed to taking a test')
        takeTest(test_questions, runTest(input()))

    else:
        print(f'Welcome back {userName}!!')
        print('What would you like to do?\n')
        print('Press Enter to continue to the main menu')
        input()

    args = {1:(test_questions, False), 2:(), 3:(), 4:()}
    while True:
        U.cls()

        print('<<<<<<<<< Welcome to CBT Simulator >>>>>>>>>\n\n')
        print(f'                        Earthling: {userName}\n')
        options = ['Take Test', 'Check Your Previous Tests Score', 'Change your Username', 'Exit']
        U.display_options(options, 'Menu Options')
        userChoice = U.u_input(len(options))
        menuOptions[userChoice](*(args[userChoice]))

def exit():
    print("\nThanks for your time, I respect you man or ma'am (whatever), bye!!!")
    raise SystemExit

if __name__ == "__main__":
    U = Utility
    menuOptions = {1:takeTest, 2:previousScores, 3: updateName, 4:exit}
    runTest = lambda x : x.lower() != "select"

    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBossman Calm down nah, no dey terminate me anyhow!")
        time.sleep(2)
        print("Buhbye sha!")
    except Exception as e:
        print("Something went wrong!\nYou fit help understand what happened ( I'm not an AI code (-_-) )")
        time.sleep(2)
        if isinstance(e, KeyError):
            print("Wait, Do you have the database file(s) sha?")
            raise SystemExit
        print("This is error raised\nHappy Debugging my friend, You caused it!!!")
        time.sleep(2)
        raise
