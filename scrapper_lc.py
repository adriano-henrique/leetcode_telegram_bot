from bs4 import BeautifulSoup
import requests
import json
import random
from functions import makeUrl, getText

class LCScrapper:
    easyQuestions = []
    mediumQuestions = []
    hardQuestions = []

    def __init__(self):
        r = requests.get(url = "https://leetcode.com/api/problems/algorithms/")
        dataJson = json.loads(r.text)
        questionsJson = dataJson['stat_status_pairs']

        for question in questionsJson:
            stat = question['stat']
            questionId = stat['question_id']
            questionName = stat['question__title']
            questionDifficulty = question['difficulty']['level']
            questionUrlId = stat['question__title_slug']
            isPaid = question['paid_only']
            if(not isPaid):
                questionsDict = {'id':questionId, 'name':questionName, 'difficulty': questionDifficulty, 'urlId': questionUrlId}
                if(questionDifficulty == 1):
                    self.easyQuestions.append(questionsDict)
                elif(questionDifficulty == 2):
                    self.mediumQuestions.append(questionsDict)
                else:
                    self.hardQuestions.append(questionsDict)

    def getEasyQuestion(self):
        index = random.randint(0,len(self.easyQuestions))
        s = getText(self.easyQuestions[index])
        return s

    def getMediumQuestion(self):
        index = random.randint(0,len(self.mediumQuestions))
        s = getText(self.mediumQuestions[index])
        return s

    def getHardQuestion(self):
        index = random.randint(0,len(self.hardQuestions))
        s = getText(self.hardQuestions[index])
        return s

    def getDesiredQuestions(self,numEasy,numMedium,numHard):
        counter = 0
        text = ""
        while(counter < numEasy):
            text += "Easy Question " + str(counter + 1) +" : \n" + self.getEasyQuestion() + "\n"
            counter += 1
        counter = 0
        text += "\n\n"
        while(counter < numMedium):
            text += "Medium Question " + str(counter + 1) +" : \n" + self.getMediumQuestion() + "\n"
            counter += 1
        counter = 0
        text += "\n\n"
        while(counter < numHard):
            text += "Hard Question " + str(counter + 1) +" : \n" + self.getHardQuestion() + "\n"
            counter += 1
        counter = 0
        print(text)
        return text



