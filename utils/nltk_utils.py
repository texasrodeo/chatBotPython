import numpy as np
import nltk

nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def tokenize(sentence):
    """
    Разбивает предложение в массив токенов
    Токен может быть словом, числом, знаком пунктуации
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    Находит корень слова
    Например:
    words = ["дерево", "деревянный", "деревце"]
    words = [stem(w) for w in words]
    -> ["дерев", "дерев", "дерев"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    Проверяет вхождение слов из фразы в массив известных слов
    1 если входит, иначе 0
    Пример:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
