
from pyrogram import Client,filters
from pyrogram.handlers import MessageHandler
import asyncio
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton)
from datetime import datetime, timedelta





api_id = 13503794
api_hash = "7c5edb66000bcb12d914019f87bffed4"
bot_token = "5736080957:AAFmsxObTNPVFfhLbGiD6xvo2tdG9M0gxsk"


bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

grpid=-1001661961660
grpmem=[]
grpv=[]

@bot.on_message(filters.command('start'))
def start(bot,msg):
    bot.send_message(msg.chat.id,"hello there !")


@bot.on_message(filters.command('check'))
async def getgrpmem(bot,msg):
      grpmem.clear()
      async for member in bot.get_chat_members(grpid):
            grpmem.append(member.user.id)
      print(grpmem)
      if msg.from_user.id in grpmem :
          await bot.send_message(msg.chat.id,"user found on group")
      else :
          await bot.send_message(msg.chat.id,"user not found ")


@bot.on_message(filters.group & filters.new_chat_members )
async def start(bot,msg):
    grpmem.clear()
    async for member in bot.get_chat_members(grpid):
        grpmem.append(member.user.id)
    if msg.from_user.id in grpmem :
          None
          print(grpmem) 
    else :
          await msg.reply_text(f"Hi @{msg.from_user.username}\nYou will be kicked in 15sec unless you join Backup group\n",reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("JOIN", url="https://t.me/+sNnEW79or2EzOWZh")]
        ]),reply_to_message_id=msg.id)
          await asyncio.sleep(15)
          await bot.delete_messages(-1001512328886,msg.id) 
          forban=msg.from_user.id
          if msg.from_user.id not in grpmem:
              await bot.ban_chat_member(-1001512328886,msg.from_user.id)
              await bot.unban_chat_member(-1001512328886,msg.from_user.id)
              await bot.send_message(msg.chat.id,f"@{msg.from_user.username} is kicked\n\nReason : Not joined in  Group ")


   
       


@bot.on_message(filters.group & filters.left_chat_member )
async def start(bot,msg):
    if msg.chat.id == grpid : 
        grpmem.remove(msg.from_user.id)
        await bot.ban_chat_member(-1001512328886,msg.from_user.id)
        await bot.send_message(msg.chat.id,f"@{msg.from_user.username} is kicked\n\nReason : Left from Backup group ")

    
   

    
        



print("Started")
bot.run()





       




     



        
        






