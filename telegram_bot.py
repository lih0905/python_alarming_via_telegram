import telegram

bot = telegram.Bot(token='970060618:AAFbYa2iflYVkwzmoDddsapDXTgJZ0xCKCE')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=874758964, text="테스트입니다")