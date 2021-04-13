import random
import json

import torch

from learning.netModel import NeuralNet
from utils.nltk_utils import bag_of_words, tokenize


class Chat:

    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open('../datasets/intents2.json', 'r', encoding='utf-8') as json_data:
            self.intents = json.load(json_data)

        FILE = "../data.pth"
        self.data = torch.load(FILE)

        self.input_size = self.data["input_size"]
        self.hidden_size = self.data["hidden_size"]
        self.output_size = self.data["output_size"]
        self.all_words = self.data['all_words']
        self.tags = self.data['tags']
        self.model_state = self.data["model_state"]

        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device)
        self.model.load_state_dict(self.model_state)
        self.model.eval()


    # bot_name = "Бот ФКН"
    # print("Обращайтесь к чат-боту ФКН! ('quit' чтобы выйти)")
    # while True:
    #     sentence = input("Вы: ")
    #     if sentence == "quit":
    #         break
    #
    #     sentence = tokenize(sentence)
    #     X = bag_of_words(sentence, all_words)
    #     X = X.reshape(1, X.shape[0])
    #     X = torch.from_numpy(X).to(device)
    #
    #     output = model(X)
    #     _, predicted = torch.max(output, dim=1)
    #
    #     tag = tags[predicted.item()]
    #
    #     probs = torch.softmax(output, dim=1)
    #     prob = probs[0][predicted.item()]
    #     if prob.item() > 0.75:
    #         for intent in intents['intents']:
    #             if tag == intent["tag"]:
    #                 print(f"{bot_name}: {random.choice(intent['responses'])}")
    #     else:
    #         print(f"{bot_name}: Я не понимаю...")

    def chatting(self, sentence):
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, self.all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(self.device)

        output = self.model(X)
        _, predicted = torch.max(output, dim=1)

        tag = self.tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.85:
            for intent in self.intents['intents']:
                if tag == intent["tag"]:
                    return random.choice(intent['responses'])
        else:
            return " Я не понимаю..."


# chat = Chat()
# bot_name = "Бот ФКН"
# print("Обращайтесь к чат-боту ФКН! ('quit' чтобы выйти)")
# while True:
#     sentence = input("Вы: ")
#     if sentence == "quit":
#         break
#     print(chat.chatting(sentence))