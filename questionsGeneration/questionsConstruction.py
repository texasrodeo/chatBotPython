from questionsGeneration.PatternAnswerTuple import PatternAnswerTuple
from questionsGeneration.Question import Question


# Вопросы генерирровать с вопросительными словами по падежу

class QuestionsConstructor:
    def __init__(self):
        pass

    def generate_questions(self, answers):
        questions = []
        for a in answers:
            questions.append(self.generate_question(a))
        return questions

    def get_question_word_by_case_anim(self, case, anim):
        question_word = []
        if case == 'nomn':
            question_word = ['Кто', 'Что']
        if case == 'gent':
            question_word = ['Кого', 'Чего']
        if case == 'datv':
            question_word = ['Кому', 'Чему']
        if case == 'ablt':
            question_word = ['Кем', 'Чем']
        if case == 'loct':
            question_word = ['О ком', 'О чем']
        if case == 'accs':
            question_word = ['Кого', 'Что']
        if anim == 'anim':
            return question_word[0]
        if anim == 'inan':
            return question_word[1]

    def generate_question(self, answerTuple: PatternAnswerTuple):
        count = 0
        answerString = answerTuple.answer.answerString
        for i in range(len(answerTuple.analyzeResult)):
            word = answerTuple.analyzeResult[i]

            if word[1].tag.POS != 'NOUN':
                if i != 0:
                    prev_word = answerTuple.analyzeResult[i-1]
                    question_word = self.get_question_word_by_case_anim(prev_word[1].tag.case, prev_word[1].tag.animacy)
                    question = question_word + answerString + '?'
                    return Question(question, answerTuple.answer.tag)
                else:
                    return
            else:
                count += 1
                answerString = answerString[len(word[0]):]



