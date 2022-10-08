
from pyrogram import Client,filters
from pyrogram.handlers import MessageHandler
import asyncio





api_id = 17222725
api_hash = "d4c911d4a89f361a0254477927b250bf"
bot_token = "5764329195:AAH3gmmr36lkWVcvKHP9buypTYsemrohIcE"

bot = Client("my_account", api_id=api_id, api_hash=api_hash,bot_token=bot_token)




    
    
    
@bot.on_message(filters.text | filters.video  | filters.document | filters.photo)
async def start(bot,msg):
    if msg.chat.id == -1001808142344 : 
        await asyncio.sleep(1800)
        await bot.delete_messages(msg.chat.id,msg.id,True)
        print("msg deleted") 


        



print("Started")
bot.run()





       




     



        
        






