import json
import io
import xml.etree.ElementTree as ET
from dataProvider.questionsGeneration.PPattern import PPattern
from dataProvider.questionsGeneration.Answer import Answer


def read_answers_file():
    with open('../datasets/answers.json', 'r', encoding='utf-8') as f:
        intents = json.load(f)
    return intents['intents']


def read_answers():
    intents = read_answers_file()
    answers = []
    for intent in intents:
        for response in intent['responses']:
            answers.append(Answer(response, intent['tag']))
    return answers


def parse_source(src):
    def parseLine(s):
        nonlocal arr, last
        s = s.strip()
        if s == '':
            last = None
            return
        if s[0] == '#':
            return
        if last is None:
            last = PPattern()
            arr.append(last)
            last.example = s
        else:
            last.tags = s.split()

    arr = []
    last = None
    buf = io.StringIO(src)
    s = buf.readline()
    while s:
        parseLine(s)
        s = buf.readline()
    return arr


def get_source_patterns():
    tree = ET.parse('../datasets/patternConfig.xml')
    root = tree.getroot()
    return root[0].get('value')
