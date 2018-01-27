import telebot

bot = telebot.TeleBot("INSERT TOKEN")

# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.reply_to(message, "Hello, I am Konohamaru")
	pass

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)



bot.polling()