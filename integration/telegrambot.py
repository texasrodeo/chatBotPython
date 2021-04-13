import telebot
from chat.chat import Chat

bot = telebot.TeleBot('1604983465:AAFEHC6ypJkCbZ3UQPojw8aaYOO3jXxnCeY')

chat = Chat()



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, chat.chatting(message.text))


bot.polling()