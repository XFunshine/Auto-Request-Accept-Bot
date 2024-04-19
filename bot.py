import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "👋 𝗛𝗲𝗹𝗹𝗼 {mention}, Welcome to 𝗔𝗻𝗶𝗺𝗲𝗔𝗿𝗶𝘀𝗲 \n\n 🔰 𝗪𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗶𝗹𝗹 𝗴𝗲𝘁 𝗯𝘆 𝗝𝗼𝗶𝗻𝗶𝗻𝗴 𝗔𝗻𝗶𝗺𝗲𝗔𝗿𝗶𝘀𝗲? \n 1⃣ All your favourite anime in different audio like English Hindi Tamil etc \n 2⃣ Anime with a Complete Season or Ongoing Episode \n 3⃣ Watch Now and Download link of all the anime \n\n ✊ 𝗕𝗲𝗰𝗼𝗺𝗲 𝗮 𝗺𝗲𝗺𝗯𝗲𝗿 𝗼𝗳 𝗼𝘂𝗿 𝗔𝗻𝗶𝗺𝗲𝗔𝗿𝗶𝘀𝗲 𝗖𝗼𝗺𝗺𝘂𝗻𝗶𝘁𝘆? \n 1⃣ Request any anime which you want to watch. \n 2⃣ If the anime is available our Bot will provide you the link. \n 3⃣ Chat with Other Anime Lovers. \n 🔰 Anime online dekhe Hindi English Tamil etc languages me \n ♥️ Our Community Joining Link 👇\n https://t.me/AnimeArise \n https://t.me/AnimeArise \n https://t.me/AnimeArise \n\n 🔰 𝗦𝗲𝗻𝗱 /start 𝘁𝗼 𝗸𝗻𝗼𝘄 𝗺𝗼𝗿𝗲 𝗮𝗯𝗼𝘂𝘁 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁.")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
 #   button=[[
#      InlineKeyboardButton("𝚄𝙿𝙳𝙰𝚃𝙴𝚉", url="https://t.me/MWUpdatez"),
 #     InlineKeyboardButton("𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="https://t.me/OpusTechz")
  #    ],[
 #     InlineKeyboardButton("𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴", url=f"https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA")
  #    ]]
    await message.reply_text(text="👋 **нєу {mention} ๏ ɪ ᴀᴍ ᴀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴏᴛ, ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴀᴄᴄᴇᴘᴛ ᴜsᴇʀ ʀᴇǫᴜᴇsᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ**", reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))       

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱")
pr0fess0r_99.run()
