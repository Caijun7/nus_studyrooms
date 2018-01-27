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
	bot.sendMessage(chat_id=update.message.chat_id, text="Hello, this is a Telegram Bot that tells you if a particular study venue is occupied or not.\n\nThe list of commands are below:\n/start\n/venues")

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

def COM1(bot, update):
	replymessage = venue.getAvailability("SOC", "COM1")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def COM2(bot, update):
	replymessage = venue.getAvailability("SOC", "COM2")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))


def BIZ(bot, update):
	biz_building_keyboard = [['Biz1', 'Biz2']]
	biz_reply_markup = telegram.ReplyKeyboardMarkup(biz_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=biz_reply_markup)


def FASS(bot, update):
	fass_building_keyboard = [['AS1', 'AS2'], ['AS3', 'AS4'], ['AS5', 'AS6'], ['AS7', 'AS8']]
	fass_reply_markup = telegram.ReplyKeyboardMarkup(fass_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below.", reply_markup=fass_reply_markup)

def AS1(bot, update):
	print("ASDhere")

	replymessage = venue.getAvailability("FASS", "AS1")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))


def FOS(bot, update):
	fos_building_keyboard = [['S1', 'S1A'], ['S2', 'S3'], ['S4', 'S4A'], ['S5', 'S8'], ['S11', 'S12',], ['S13', 'S14'], ['S16', 'S17']]
	fos_reply_markup = telegram.ReplyKeyboardMarkup(fos_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below (scrollable).", reply_markup=fos_reply_markup)


def SDE(bot, update):
	replymessage = venue.getAvailability("SDE", "SDE")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))


def FOE(bot, update):
	foe_building_keyboard = [['E1', 'E1A'], ['E2', 'E2A'], ['E3', 'E3A'], ['E4', 'E4A'], ['E5', 'EA']]
	foe_reply_markup = telegram.ReplyKeyboardMarkup(foe_building_keyboard)
	bot.send_message(chat_id=update.message.chat_id, text="Select from the list of buildings below (scrollable).", reply_markup=foe_reply_markup)

def E1(bot, update):
	replymessage = venue.getAvailability("FOE", "E1")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E1A(bot, update):
	replymessage = venue.getAvailability("FOE", "E1A")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E2(bot, update):
	replymessage = venue.getAvailability("FOE", "E2")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E2A(bot, update):
	replymessage = venue.getAvailability("FOE", "E2A")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E3(bot, update):
	replymessage = venue.getAvailability("FOE", "E3")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E3A(bot, update):
	replymessage = venue.getAvailability("FOE", "E3A")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E4(bot, update):
	replymessage = venue.getAvailability("FOE", "E4")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E4A(bot, update):
	replymessage = venue.getAvailability("FOE", "E4A")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def E5(bot, update):
	replymessage = venue.getAvailability("FOE", "E5")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def EA(bot, update):
	replymessage = venue.getAvailability("FOE", "EA")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))


def UTSRC(bot, update):
	replymessage = venue.getAvailability("UTSRC", "UTSRC")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

def ERC(bot, update):
	replymessage = venue.getAvailability("ERC", "ERC")
	newreply = ""
	for x in replymessage:
		newreply = newreply + x + ": " + replymessage[x] + "\n"

	bot.send_message(chat_id=update.message.chat_id, text=str(newreply))

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

COM1_handler = RegexHandler('COM1', COM1)
COM2_handler = RegexHandler('COM2', COM2)
E1_handler = RegexHandler('E1', E1)
E1A_handler = RegexHandler('E1A', E1A)
E2_handler = RegexHandler('E2', E2)
E2A_handler = RegexHandler('E2A', E2A)
E3_handler = RegexHandler('E3', E3)
E3A_handler = RegexHandler('E3A', E3A)
E4_handler = RegexHandler('E4', E4)
E4A_handler = RegexHandler('E4A', E4A)
E5_handler = RegexHandler('E5', E5)
EA_handler = RegexHandler('EA', EA)
UTSRC_handler = RegexHandler('UTSRC', UTSRC)
ERC_handler = RegexHandler('ERC', ERC)

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

dispatcher.add_handler(COM1_handler)
dispatcher.add_handler(COM2_handler)
dispatcher.add_handler(E1_handler)
dispatcher.add_handler(E1A_handler)
dispatcher.add_handler(E2_handler)
dispatcher.add_handler(E2A_handler)
dispatcher.add_handler(E3_handler)
dispatcher.add_handler(E3A_handler)
dispatcher.add_handler(E4_handler)
dispatcher.add_handler(E4A_handler)
dispatcher.add_handler(E5_handler)
dispatcher.add_handler(EA_handler)
dispatcher.add_handler(UTSRC_handler)
dispatcher.add_handler(ERC_handler)

updater.start_polling()

