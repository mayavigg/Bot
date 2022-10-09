import asyncio
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

api_id = 17222725
api_hash = "d4c911d4a89f361a0254477927b250bf"
bot_token = "5764329195:AAH3gmmr36lkWVcvKHP9buypTYsemrohIcE"

bot = Client("my_account", api_id=api_id, api_hash=api_hash,bot_token=bot_token)


@bot.on_message(filters.photo)
async def start(bot,msg):
    if msg.chat.id == -1001808142344 : 
        await bot.copy_message(-1001867103377,msg.chat.id,msg.id)
        await asyncio.sleep(300)
        await bot.delete_messages(msg.chat.id,msg.id,True)
        print("photo deleted")

@bot.on_message(filters.video | filters.document | filters.audio | filters.media_group)
async def start(bot,msg):
    if msg.chat.id == -1001808142344 :
        await bot.copy_message(-1001867103377,msg.chat.id,msg.id)
        await bot.copy_message(-1001412463977,msg.chat.id,msg.id)
        await bot.copy_message(-1001725493934,msg.chat.id,msg.id)
        print("media dumped")
        await asyncio.sleep(30)
        await bot.delete_messages(msg.chat.id,msg.id,True)
        print("media deleted")

    
    
    
@bot.on_message(filters.text )
async def start(bot,msg):
    if msg.chat.id == -1001808142344 : 
        await asyncio.sleep(1800)
        await bot.delete_messages(msg.chat.id,msg.id,True)
        print("msg deleted") 

print("bot started") 
bot.run()  
