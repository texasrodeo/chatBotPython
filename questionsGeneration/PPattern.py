import pymorphy2 as py

class PPattern:
    def __init__(self):
        super().__init__()
        self.tags = []
        self.morph = py.MorphAnalyzer()

    def checkPhrase(self, text):
        def checkWordTags(tags, grams):
            for t in tags:
                if t not in grams:
                    return False
            return True

        def checkWord(tags, word):
            variants = self.morph.parse(word)
            for v in variants:
                if checkWordTags(self.tags[nextTag].split(','), v.tag.grammemes):
                    return word, v
            return None


        words = text.split()
        nextTag = 0
        result = []
        for w in words:
            res = checkWord(self.tags[nextTag].split(','), w)
            if res is not None:
                result.append(res)
                nextTag = nextTag + 1
                if nextTag >= len(self.tags):
                    return result
        return None

    def parse_single_word(self, word):
        return self.morph.parse(word)[0]
