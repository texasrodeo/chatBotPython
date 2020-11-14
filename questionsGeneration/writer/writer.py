import json
import codecs
from questionsGeneration.reader.reader import read_answers_file

class IntentFileWriter:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.data = {'intents': []}

    def create_data(self):
        intents = read_answers_file()
        for i in intents:
            tag = {}
            tag['tag'] = i['tag']
            tag['questions'] = []
            tag['responses'] = []
            self.data['intents'].append(tag)
        for q in self.questions:
            intent = self.get_needed_intent_by_tag(q)
            intent['questions'].append(q.questionString)
        for a in self.answers:
            intent = self.get_needed_intent_by_tag(a)
            intent['responses'].append(a.answerString)

    def get_needed_intent_by_tag(self, arg):
        for intent in self.data['intents']:
            if intent['tag'] == arg.tag:
                return intent

    def save_file(self):
        self.create_data()
        with open('../datasets/intents.json', 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
