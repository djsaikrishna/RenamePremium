import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5735158724:AAGdOHgLClMpob9Z44VmQvg_hMEgsIUBAGo")

API_ID = int(os.environ.get("API_ID", "15882573"))

API_HASH = os.environ.get("API_HASH", "dddd64edfc5326e4a35e448347b83e2d")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
