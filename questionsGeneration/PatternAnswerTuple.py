from questionsGeneration.PPattern import PPattern
from questionsGeneration.Answer import Answer

class PatternAnswerTuple:
    def __init__(self, pattern: PPattern, answer:Answer, analyzeResult):
        self.pattern = pattern
        self.answer = answer
        self.analyzeResult = analyzeResult
