from dataProvider.questionsGeneration.answersParser import AnswersParser
from dataProvider.questionsGeneration.questionsConstruction import QuestionsConstructor
from dataProvider.questionsGeneration.writer.writer import IntentFileWriter

answersParser = AnswersParser()
questionsConstructor = QuestionsConstructor()
questions = questionsConstructor.generate_questions(answersParser.results)
intentFileWriter = IntentFileWriter(questions, answersParser.answers)

for question in questions:
    print(question.questionString)

intentFileWriter.save_file()
