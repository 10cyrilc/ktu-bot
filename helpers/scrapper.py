import hashlib
import time
import requests
import telegram
from bs4 import BeautifulSoup
from helpers.db import add_hash, get_hash
from config import Config

bot = telegram.Bot(token=Config.BOT_ID)

link = "https://ktu.edu.in/eu/core/announcements.htm"
wa_link = "https://api.whatsapp.com/send?text="


async def scrape(logger):
    logger.info("Getting Data...")
    page = requests.get(link)
    logger.info("Data Recieved....")
    soup = BeautifulSoup(page.content, "lxml")
    table = soup.find("table")
    trs = table.find_all("tr")
    for i in range(5):
        tr = trs[i]
        dates = tr.find(
            "label", class_="news-date").text.strip().replace("00:00:00 ", "")
        content = tr.find("li")
        heading = content.find("b").text.strip()
        body = content.text
        body = remSpace(" ", body)
        not_a = content.find("a")
        logger.info("Data Parsed....")

        try:
            not_link = "https://ktu.edu.in" + not_a['href']
            not_content = not_a.text
            not_link = remSpace("", not_link)
        except:
            not_link = ""
            not_content = ""

        hash_content = dates + "\n" + heading + "\n" + body

        body += f'\n\n<a href="{not_link}">{not_content}</a>'

        share_content = f"<b>{dates}</b>\n\n{heading}\n\n{body}"

        wa_content = f"{wa_link}{hash_content}"

        keyboard = [[telegram.InlineKeyboardButton(
            "Share to WhatsApp", url=wa_content)]]

        reply_markup = telegram.InlineKeyboardMarkup(keyboard)

        await hasher(logger, hash_content, share_content, reply_markup)

    logger.info("Completed")


async def hasher(logger, hash_string, share_string, reply_markup):
    result = hashlib.md5(hash_string.encode())
    final_hash = result.hexdigest()
    check_hash = get_hash(final_hash)
    if not check_hash:
        add_hash(final_hash)
        logger.warning(final_hash)
        await bot.send_message(chat_id=Config.CHAT_ID, text=share_string, reply_markup=reply_markup, parse_mode="HTML")
    else:
        logger.warning(f"{final_hash} - No Changes")


def remSpace(limiter, string):
    return limiter.join(string.split())
