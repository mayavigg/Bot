
from pyrogram import Client,filters
from pyrogram.handlers import MessageHandler
import asyncio






api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5686371046:AAFiCgN2kxUtp2kjsgw3ue5UR-QsjSDw6-E"


bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


role=[5559099357]

@bot.on_message(filters.text)
def start(bot,msg):
    if msg.from_user.id in role :
        None
    else : 
        bot.delete_messages(msg.chat.id,msg.id,True)
        print("msg deleted")    


        



print("Started")
bot.run()





       




     



        
        






