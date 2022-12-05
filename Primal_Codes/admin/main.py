#Exercises on Vectors
import shelve, os, time, random
from platform import system as ostype
from string import ascii_uppercase


class MyTest:
    def __init__(self):
        self.__load__()
        self.NUM_OF_QUESTION = len(self.testQ)
        self.optionTag = {i+1:ascii_uppercase[i] for i in range(5) }
        self.questionNumbers = {str(i):i for i in range(1, self.NUM_OF_QUESTION+1)}
        self.userData = shelve.open('User Data')
        

    def __load__(self):
        shelvefile = shelve.open('Program Data')
        database = open('cdatabase.py', 'w')
        database.write(shelvefile['cdatabase'])
        database.close()
        import cdatabase
        self.testQ = cdatabase.testQuestions
    def __clearScreen__(self):
        if ostype() == 'Linux' or ostype() == 'Darwin':
            os.system('clear')
        elif ostype() == 'Windows':
            os.system('cls')

    def display_instruction(self):
        print(f'\nINSTRUCTION: The test contains {self.NUM_OF_QUESTION} multiple choice questions')
        print('             Choose option A, B or C by entering A, B or C and press Enter')
        print('             You can enter a question number to go to that question')
        input('\nPress Enter to continue')
    
    def __validateUserInput__(self):
        while True:
            userIn = input(': ').upper()
            if userIn in self.option_inputs or userIn in self.questionNumbers:
                return userIn
            print('\nInvalid Input')
            print(f'Enter options ({", ".join(list(self.option_inputs.keys()))})\t\tOR')
            print(f'Enter a question number (1 - {self.NUM_OF_QUESTION})')
            print()
        
        
    def __takeTest__(self):
        print('Welcome to a test practice on Vector')
        self.display_instruction()
        self.__clearScreen__()
        for i in range(3,-1, -1):
            print(f'Test start in {i}')
            time.sleep(1)
            self.__clearScreen__()
        self.userAnswers = {}
        questionOrder = list(self.testQ.keys())
        random.shuffle(questionOrder)

        i = 0
        while i < self.NUM_OF_QUESTION + 1:
            answer = self.userAnswers.get(questionOrder[i])
            if answer == None:
                print(f'Question {i + 1}\n')
            else:
                print(f'Question {i + 1} (Answered: {answer})\n')
            print(self.testQ[questionOrder[i]][0])
            options = self.testQ[questionOrder[i]][1:]
            random.shuffle(options)
            print()
            for optionNumber in range(len(options)):
                print(f'    {self.optionTag[optionNumber+1]}.) {options[optionNumber]}')
            print()
            self.option_inputs = {ascii_uppercase[i]:i for i in range(len(options))}
            userIn = self.__validateUserInput__()
            if userIn in self.questionNumbers.keys():
                i = self.questionNumbers[userIn] - 1
                self.__clearScreen__()
                continue
            elif userIn in self.option_inputs:
                self.userAnswers[questionOrder[i]] = options[self.option_inputs[userIn]]
            self.__clearScreen__()
            i += 1
            
    def __toolOptions__(self):
        toolOptions = {'1':['Take Test'], '2':['Check Your Previous Test Results'], '3':['See your Project Choice'], '4':['Change your Username'], '5':['Quit Program']}
        print("\nTool Options\n")
        for i in toolOptions.keys():
            print(f"{i}. {toolOptions[i][0]}")
        while True:
            userIn = input(': ')
            if userIn in toolOptions.keys():
                break
            else:
                print('Invalid Input')

    def run(self):
        self.__clearScreen__()
        self.userName = self.userData.get('username')
        print('<<<<<<<<< LISP >>>>>>>>>')
        if self.userName == None:
            print('WELCOME!!!')
            print('Please Enter your Name (more like a username)')
            self.userName = input(': ')
            self.userData['username'] = self.userName
            print(f'\nThank you {self.userName}')
            print('Press Enter to Proceed to taking the test')
            input()
            self.__clearScreen__()
            self.__takeTest__()
        else:
            print(f'Welcome back {self.userName}!!')
            print('What would you like to do?')
            print()
            self.__toolOptions__()
        
        
        
        

k = MyTest()
k.run()
