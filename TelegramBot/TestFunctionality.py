#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:19:55 2018

@author: humza
"""

import telegram
bot = telegram.Bot(token = '583201853:AAHSj9c0Y5kxkwS_80hvjpnRgUMQCgO92Fc')
'''
updater = Updater(token='583201853:AAHSj9c0Y5kxkwS_80hvjpnRgUMQCgO92Fc')

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)


updater.start_polling()
Out[13]: <queue.Queue at 0x1820f69160>

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    

from telegram.ext import MessageHandler, Filters

echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)
    

caps_handler = CommandHandler('caps', caps, pass_args=True)

dispatcher.add_handler(caps_handler)
from telegram import InlineQueryResultArticle, InputTextMessageContent

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return 
    results = list()
    results.append(InlineQueryResultArticle(id=query.upper(),title='Caps', input_message_content=InputTextMessageContent(query.upper())))
    bot.answer_inline_query(update.inline_query.id, results)
    

from telegram.ext import InlineQueryHandler

inline_caps_handler=InlineQueryHandler(inline_caps)

dispatcher.add_handler(inline_caps_handler)
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    

unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(unknown_handler)

updater.stop()
'''
import os
import sys
from threading import Thread
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import logging 
from telegram import InlineQueryResultArticle, InputTextMessageContent, Sticker, InlineQueryResultCachedSticker
from uuid import uuid4


# Other code

def main():
    updater = Updater("583201853:AAHSj9c0Y5kxkwS_80hvjpnRgUMQCgO92Fc")
    dispatcher = updater.dispatcher

    # Add your other handlers here...



    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


    start_handler = CommandHandler('start', start)

    dispatcher.add_handler(start_handler)


    try:
        updater.start_polling()
    except:
        updater.stop()
        updater.start_polling()

    def echo(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    

    echo_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(echo_handler)

    def caps(bot, update, args):
        text_caps = ' '.join(args).upper()
        bot.send_message(chat_id=update.message.chat_id, text=text_caps)
    

    caps_handler = CommandHandler('caps', caps, pass_args=True)

    dispatcher.add_handler(caps_handler)
    
    def math(bot, update, args):
        text_math = ''.join(args)
        text_math= str(int(text_math) + 1)
        bot.send_message(chat_id=update.message.chat_id, text=text_math)
        
    math_handler = CommandHandler('math', math, pass_args= True)
    dispatcher.add_handler(math_handler)
    
    def help(bot, update, args):
        bot.send_message(chat_id=update.message.chat_id, text='Right now this bot is not functional, I am using it to test the concepts as I am learning them. \n The commmands are: \n /caps : displays messaged typed in all caps \n /math : adds 1 to the number')
    help_handler = CommandHandler('help', help, pass_args=True)
    dispatcher.add_handler(help_handler)
   

    def inline_caps(bot, update):
        query = update.inline_query.query
        if not query:
            return 
        results = list()
        results.append(InlineQueryResultArticle(id=query.upper(),title='Caps', input_message_content=InputTextMessageContent(query.upper())))
        bot.answer_inline_query(update.inline_query.id, results)
        
    def inline_lower(bot, update):
        query = update.inline_query.query
        if not query:
            return
        results = list()
        results.append(InlineQueryResultArticle(id= uuid4(), title = "lowercase", input_message_content=InputTextMessageContent(query.lower())))
        bot.answerInlineQuery(update.inline_query.id, results)
    


    inline_caps_handler=InlineQueryHandler(inline_caps)
    inline_lower_handler=InlineQueryHandler(inline_lower)

    dispatcher.add_handler(inline_caps_handler)
    dispatcher.add_handler(inline_lower_handler)
   
    
    

    def stop_and_restart():
        """Gracefully stop the Updater and replace the current process with a new one"""
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    # ...or here...

    dispatcher.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@Humdan')))
    
    def sticker(bot, update, args):
        text_sticker = ''.join(args)
        bot.send_sticker(update.message.chat_id, "CAADBAADMwADjkyzC3xhbwJiwFvjAg")
    sticker_handler= CommandHandler('sticker', sticker, pass_args=True)
    dispatcher.add_handler(sticker_handler)
    
    def inline_sticker(bot, update):
        query = update.inline_query.query
        if not query:
            return
        results = []
        results.append(InlineQueryResultCachedSticker('sticker', "CAADBAADMwADjkyzC3xhbwJiwFvjAg"))
        bot.answerInlineQuery(update.inline_query.id, results)
        
    dispatcher.add_handler(InlineQueryHandler(inline_sticker))
    

    # ...or here, depending on your preference :)
    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
    

    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()
    


if __name__ == '__main__':
    main()
    