import dataProvider.questionsGeneration.reader.reader as reader
from dataProvider.questionsGeneration.PatternAnswerTuple import PatternAnswerTuple


class AnswersParser:
    def __init__(self):
        self.source = '''
            #Алгазинов Эдуард Константинович является деканом факультета
            # сущ сущ гл гл
            # что/кто  делает с чем-то
            #NOUN,nomn NOUN,nomn NOUN,nomn VERB
            #Кто VERB ...?

            #ФКН является лучший фаультетом ВГУ
            # сущ  гл
            # что/кто  делает с_чем-то
            #UNKN VERB
            #Что VERB ...?
            
        
            Вася ест кашу
            # сущ  гл
            # что/кто  делает с_чем-то
            NOUN,nomn VERB
            #Кто/что VERB ...?

            Президентом является Путин
            # сущ  гл
            # что/кто  делает с_чем-то
            NOUN,ablt VERB
            #Кем/чем VERB ...?

            
            '''

        self.patterns = reader.parse_source(self.source)
        self.results = []
        self.answers = reader.read_answers()
        for answer in self.answers:
            self.parseAnswer(answer, self.patterns)

    def parseAnswer(self, answer, patterns):
        for p in patterns:
            res = p.checkPhrase(answer.answerString)
            if res:
                self.results.append(PatternAnswerTuple(p, answer, res))


