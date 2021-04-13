import requests
from bs4 import BeautifulSoup
import pandas as pd
from sklearn.model_selection import train_test_split

_url = "http://sfaq.ru/p"
_prefix = "ask_question"


def get_page_url(pageNumber):
    return _url + str(pageNumber) + '/'


resultQuestions = []
resultAnswers = []

for i in range(1, 51):
    r = requests.get(get_page_url(i))
    soup = BeautifulSoup(r.text)

    questions = soup.find_all('h2')
    for question in questions:
        resultQuestions.append(question.text)

    answers = soup.find_all('p')
    answers = answers[7:-4]
    for i in range(len(answers)):
        if i % 2 == 0:
            resultAnswers.append(answers[i].text.replace('\r\n\r', '').replace('\n', ''))


def get_record(question, answer):
    res = pd.DataFrame()
    res = res.append(pd.DataFrame([[question, answer, _prefix]], columns=['target_text', 'input_text', 'prefix']), ignore_index=True)
    return res


result = pd.DataFrame()
length = len(resultQuestions)

for i in range(length):
    result = result.append(get_record(resultQuestions[i], resultAnswers[i]), ignore_index=True)

train_df, eval_df = train_test_split(result, test_size=0.05)


train_df.to_csv("../T5QuestionGenerator/data/train_df_3.tsv", "\t")
eval_df.to_csv("../T5QuestionGenerator/data/eval_df_3.tsv", "\t")
