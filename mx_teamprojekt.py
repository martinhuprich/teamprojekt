import urllib.request
import json
from random import shuffle

class Quiz():
    
    def __init__(self, name, url):
        self.name = name
        self.url = url
        
    
#    def get_info(self):
#        print(self.name)
#        print(self.url)


    def get_question_and_answers(self):
        
        #retrieving information from the website open trivia, getting one question with right and incorrect answers
        complete_information = json.load(urllib.request.urlopen(self.url))
        
        question = complete_information['results'][0]['question']
        
        correct_answer = complete_information['results'][0]['correct_answer']
        
        false_answers = complete_information['results'][0]['incorrect_answers']
        # building a list with all answers, correct and incorrect ones for processing
        answers = [complete_information['results'][0]['correct_answer']]
        
        for i in false_answers:
            answers.append(i)
        shuffle(answers)

        #print the question to the console
        print(question)
        
        #
        #print(answers)

        #if only true or false are the options the possible answers need to be adapted (-> true & false)
        if len(answers) == 2:
            print('1: ' + answers[0] + '\n' + '2: ' + answers[1])
        else:
            print('1: ' + answers[0] + '\n' + '2: ' + answers[1] + '\n' +'3: '+ answers[2] + '\n' +'4: ' + answers[3])
        
        #check whether there are 2 or 4 options and make sure the user is being provided with the adequate choice
        if len(answers) < 3:
            user_answer = input("Which answer do you choose? 1 or 2?")
        else:
            user_answer = input("Which answer do you choose? 1, 2, 3 or 4?")
        
        index = int(user_answer) - 1
        
        #check if the given answer of the user is correct, by accessing the answers list with index. index is calculated by subtracting 1 from the users´ answer
        if (answers[index]) == correct_answer:
            print("Hooray! You have won!")
        else:
            print("Uh Oh, that is not the right answer!")
        
    
    
   
        
        

Martin = Quiz("Martin", "https://opentdb.com/api.php?amount=1")
#Martin.get_info()
Martin.get_question_and_answers()