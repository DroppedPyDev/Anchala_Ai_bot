
import wget
import speedtest

from config import BOT_USERNAME as bname
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.filters import command, other_filters

@Client.on_message(command(["speedtest", f"speedtest@{bname}"]) & ~filters.edited)
async def run_speedtest(_, message: Message):
    m = await message.reply_text("⚡️ 𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙎𝙥𝙚𝙚𝙙 𝙊𝙣 𝙎𝙚𝙧𝙫𝙚𝙧𝙨..")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ 𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙...")
        test.download()
        m = await m.edit("⚡️ 𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙐𝙥𝙡𝙤𝙖𝙙 𝙎𝙥𝙚𝙚𝙙...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("🔄 Ｓｅｒｖｅｒ - 𝐒𝐩𝐞𝐞𝐝 𝐓𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬")
    path = wget.download(result["share"])

    output = f"""💡 **𝐒𝐩𝐞𝐞𝐝 𝐓𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭𝐬**
    
<u>**Ｂｏｔ:**</u>
**ISP:** {result['client']['isp']}
**𝐂𝐨𝐮𝐧𝐭𝐫𝐲:** {result['client']['country']}
  
<u>**Ｓｅｒｖｅｒ:**</u>
**𝐍𝐚𝐦𝐞:** {result['server']['name']}
**𝐂𝐨𝐮𝐧𝐭𝐫𝐲:** {result['server']['country']}, {result['server']['cc']}
**𝐒𝐩𝐨𝐧𝐬𝐨𝐫:** {result['server']['sponsor']}
**𝐋𝐚𝐭𝐞𝐧𝐜𝐲:** {result['server']['latency']}

⚡️ **Ｐｉｎｇ:** {result['ping']}"""
