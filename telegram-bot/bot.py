from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv('../.env')


def convert_longurl(longurl,username):
    try:
        payload = json.dumps({
            "name": username or "No Name",
            "longurl": longurl
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", os.environ.get("BASE_URL"), headers=headers, data=payload)

        response=response.json()
        return response["shorturl"]
    except BaseException as e:
        print(e)

def get_short_url(update, context):
    try:
        chat_id = update.message.chat_id
        username= update.message.chat.first_name
        url=update.message.text
        longurl=url.split(" ")[1]
        text=convert_longurl(longurl,username)
        context.bot.sendMessage(chat_id=chat_id,text="Shortened URL: "+text)
    except BaseException as e:
        print(e)

def driver_function():
    updater = Updater(token=os.environ.get("token"),use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('geturl',get_short_url))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    driver_function()