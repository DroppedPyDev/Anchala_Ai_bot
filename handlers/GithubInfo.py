'''
• Module to Get Github Information of a User.
• © Open Sourced Code ✅
• Not Scrapped from any Repository exist in Internet. If you Scrap or Copy these Module Don't remove the below Line !.
• /////https://t.me/reameab /////// Copyrighted. ! You can use it anywhere but not to be sold !!!

• Module Name = Githubinfo
• Created on = 27 March 2022 ~ 10:23:45 PM
• Command = '/git' 

'''

import aiohttp
from pyrogram import filters
from pyrogram import Client


@Client.on_message(filters.command('git'))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗼𝗳 𝗨𝘀𝗲𝗿 - {name} •
𝗚𝗶𝘁𝗵𝘂𝗯 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 :`{username}`
𝗨𝘀𝗲𝗿 𝗕𝗶𝗼 :`{bio}`
𝗚𝗶𝘁𝗵𝘂𝗯 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 : [{name}]({url})
𝗖𝗼𝗺𝗽𝗮𝗻𝘆 𝗡𝗮𝗺𝗲 : `{company}`
𝗨𝘀𝗲𝗿 𝗦𝗶𝗻𝗰𝗲 : `{created_at}`
𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝗶𝗲𝘀 : `{repositories}`
𝗕𝗹𝗼𝗴 𝗨𝗿𝗹 : `{blog}`
𝗨𝘀𝗲𝗿 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻 : `{location}`
𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀 : `{followers}`
𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 : `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
