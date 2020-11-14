import json
from questionsGeneration.answersParser import AnswersParser
from questionsGeneration.questionsConstruction import QuestionsConstructor
from questionsGeneration.writer.writer import IntentFileWriter

answersParser = AnswersParser()
questionsConstructor = QuestionsConstructor()
questions = questionsConstructor.generate_questions(answersParser.results)
intentFileWriter = IntentFileWriter(questions, answersParser.answers)

for question in questions:
    print(question.questionString)

intentFileWriter.save_file()
