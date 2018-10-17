#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 12:44:25 2018

@author: humza
"""
# from Sticker_Info import sticker
from Hearts_Game import Game_Hearts, Bot, Table
import os
import sys
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging 
from telegram import InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4

GAME_CREATED = False
GAME_STARTED = False
NUM_PLAYERS = 0
POINTS_TO_END = 0
# TODO: Implement POINTS_TO_END


def main():
    updater = Updater("583201853:AAHSj9c0Y5kxkwS_80hvjpnRgUMQCgO92Fc")
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hey! I am a bot and currently my creator, @Humdan, is too lazy to make me do anything! Type in /help for commands")
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    
    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    restart_handler = CommandHandler('r', restart, filters=Filters.user(username='@Humdan'))
    dispatcher.add_handler(restart_handler)
    
    def help(bot, update):
        bot.send_message(chat_id=update.chate_id, text="/caps [text]: write the text in caps \n /create_hearts_game: create a new game of hearts \n /join_hearts_game: join an existing game of hearts \n /start_hearts_game: start an existing game of hearts")
    
    def caps(bot, update, args):
        text_caps = ' '.join(args).upper()
        bot.send_message(chat_id=update.message.chat_id, text=text_caps)

    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)
    
    def create_hearts_game(bot, update):
        global GAME_CREATED
        if not GAME_CREATED:
            bot.send_message(chat_id=update.message.chat_id, text= 'New Hearts game has been created! Press /join_hearts_game to join!')
            GAME_CREATED = True
        else:
            bot.send_message(chat_id=update.message.chat_id, text= "Game already in progress, if it hasn't started yet, please use /join_hearts_game")
        
    create_hearts_game_handler = CommandHandler('create_hearts_game', create_hearts_game)
    dispatcher.add_handler(create_hearts_game_handler)
        
    def join_hearts_game(bot, update):
        # bot.send_message(chat_id = bot.get_updates()[-1].message.chat_id, text='Joined the game!')
        update.message.reply_text('Joined the game!')
        global NUM_PLAYERS
        NUM_PLAYERS += 1
    
    join_hearts_game_handler = CommandHandler('join_hearts_game', join_hearts_game)
    dispatcher.add_handler(join_hearts_game_handler)
    
    def start_hearts_game(bot, update):
        if GAME_CREATED:
            bot.send_message(chat_id=update.message.chat_id, text = 'The game has started! Give me a second while I deal out the cards.')
            global GAME_STARTED
            GAME_STARTED = True
        else:
            bot.send_message(chat_id=update.message.chat_id, text= 'Create a game using /create_hearts_game before starting one!')
    
    start_hearts_game_handler = CommandHandler('start_hearts_game', start_hearts_game)
    dispatcher.add_handler(start_hearts_game_handler)
    
    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
    global GAME_CREATED, GAME_STARTED
    if GAME_STARTED:
        GAME_CREATED, GAME_STARTED = False, False
        game = Game_Hearts(NUM_PLAYERS, POINTS_TO_END=25)
        game.distribute_cards()
        game.play_game()
    
if __name__ == '__main__':
    main()