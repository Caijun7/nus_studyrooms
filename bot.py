import venue
import fetch
import booking_parser

import telegram
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, RegexHandler, CallbackQueryHandler

#Telegram bot token
TOKEN_USE = "486363762:AAFFmrpjRxKMuPTrQCFHluzuCOL5uemyELM"
bot = telegram.Bot(token=TOKEN_USE)

#Fetches new updates from telegram to pass to the Dispatcher Class
updater = Updater(token=TOKEN_USE)
#Sorts the updates fetched by the updater according to the handlers below
dispatcher = updater.dispatcher

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hello, this is a Telegram Bot that tells you if a particular study venue is occupied or not.\n\nThe list of commands are below:\n/start\n/venue")

#Faculties and Utown Building
def venues(bot, update):
	custom_keyboard = [['BIZ', 'SOC'], ['FASS', 'FOE'], ['FOS', 'SDE'], ['ERC', 'UTSRC'], ['Lecture Theatres']]
	#The ReplyKeyboardMarkup is used to create the custom keyboard
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of locations below (scrollable).\nTo go back to this keyboard again, simply type /venues", reply_markup=reply_markup)

def LectureTheatres(bot, update):
	lt_keyboard = [['LT1', 'LT2'], ['LT3', 'LT4'], ['LT5', 'LT6'], ['LT7', 'LT7A'], ['LT8', 'LT9'], ['LT10', 'LT11'], ['LT12', 'LT13'], ['LT14', 'LT15'], ['LT16', 'LT17'], ['LT18', 'LT19'], ['LT20', 'LT21'], ['LT22', 'LT23'], ['LT24', 'LT25'], ['LT26', 'LT27'], ['LT28', 'LT29'], ['LT30', 'LT31'], ['LT32', 'LT33'], ['LT34']]
	lt_reply_markup = telegram.ReplyKeyboardMarkup(lt_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of lecture theatres below (scrollable).", reply_markup=lt_reply_markup)

def SOC(bot, update):
	soc_building_keyboard = [['COM1', 'COM2'], ['i3']]
	soc_reply_markup = telegram.ReplyKeyboardMarkup(soc_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=soc_reply_markup)

def BIZ(bot, update):
	biz_building_keyboard = [['Biz1', 'Biz2']]
	biz_reply_markup = telegram.ReplyKeyboardMarkup(biz_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=biz_reply_markup)

def FASS(bot, update):
	fass_building_keyboard = [['AS1', 'AS2'], ['AS3', 'AS4'], ['AS5', 'AS6'], ['AS7', 'AS8']]
	fass_reply_markup = telegram.ReplyKeyboardMarkup(fass_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=fass_reply_markup)

def FOS(bot, update):
	fos_building_keyboard = [['S1', 'S1A'], ['S2', 'S3'], ['S4', 'S4A'], ['S5', 'S8'], ['S11', 'S12',], ['S13', 'S14'], ['S16', 'S17']]
	fos_reply_markup = telegram.ReplyKeyboardMarkup(fos_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below (scrollable).", reply_markup=fos_reply_markup)

#Need to edit SDE
def SDE(bot, update):
	#SDE does not really have multiple buildings. It is one big building by itself
	sde_building_keyboard = [['AS1', 'AS2'], ['AS3', 'AS4'], ['AS5', 'AS6'], ['AS7', 'AS8'], ['LT9', 'LT10',]]
	sde_reply_markup = telegram.ReplyKeyboardMarkup(sde_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=sde_reply_markup)

def FOE(bot, update):
	foe_building_keyboard = [['E1', 'E1A'], ['E2', 'E2A'], ['E3', 'E3A'], ['E4', 'E4A'], ['E5', 'EA']]
	foe_reply_markup = telegram.ReplyKeyboardMarkup(foe_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below (scrollable).", reply_markup=foe_reply_markup)

def AS1(bot, update):
	print("ASDhere")

	replymessage = venue.getAvailability("FASS", "AS1")
	#testing = ' ' + (replymessage)

	print(str(replymessage))
#	testing = ' '.join(replymessage)
	#print(testing)
	bot.send_message(chat_id=update.message.chat_id, text=str(replymessage))

#Handler class to handle Telegram commands
#Commands are telegram messages that start with /
start_handler = CommandHandler('start', start)
venues_handler = CommandHandler('venues', venues)

#Handler class to handle Telegram updates based on a regex
soc_handler = RegexHandler('SOC', SOC)
biz_handler = RegexHandler('BIZ', BIZ)
fass_handler = RegexHandler('FASS', FASS)
fos_handler = RegexHandler('FOS', FOS)
sde_handler = RegexHandler('SDE', SDE)
foe_handler = RegexHandler('FOE', FOE)
lt_handler = RegexHandler('Lecture Theatres', LectureTheatres)
AS1_handler = RegexHandler('AS1', AS1)

#bot.reply_to_message(chat_id=update.message.chat_id, text= venue.getAvailability("FASS", "AS1"))
#soc_vac_handler = RegexHandler('AS1', FASS.getAvailability(FASS, AS1))
#dispatcher.add_handler(soc_vac_handler)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(venues_handler)
dispatcher.add_handler(soc_handler)
dispatcher.add_handler(biz_handler)
dispatcher.add_handler(fass_handler)
dispatcher.add_handler(fos_handler)
dispatcher.add_handler(sde_handler)
dispatcher.add_handler(foe_handler)
dispatcher.add_handler(lt_handler)
dispatcher.add_handler(AS1_handler)
updater.start_polling()

