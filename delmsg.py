
from pyrogram import Client,filters
from pyrogram.handlers import MessageHandler
import asyncio






api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5668405833:AAHzCkQQDdRZ15jMuZw4AraeueSbug1KBTM"


bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)



@bot.on_message(filters.text)
async def start(bot,msg):
    await asyncio.sleep(1)
    await bot.delete_messages(msg.chat.id,msg.id)


@bot.on_message(filters.bot)
def delbot(bot,msg):
    bot.delete_messages(msg.chat.id,msg.id)  

    
        



print("Started")
bot.run()





       




     



        
        






