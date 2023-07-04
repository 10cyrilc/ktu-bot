import hashlib
import requests
import telegram
from bs4 import BeautifulSoup
from helpers.db import add_hash, get_hash
from config import Config

bot = telegram.Bot(token=Config.BOT_ID)


link = "https://ktu.edu.in/eu/core/announcements.htm"


async def scrape():
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
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
        try:
            not_link = "ktu.edu.in" + not_a['href']
            not_link = remSpace("", not_link)
        except:
            not_link = ""

        hash_content = dates + "\n" + heading + "\n" + body
        share_content = "**"+dates+"**" + "\n\n" + heading + \
            "\n\n" + body + "\n\n" + not_link + "\n\n"

        await hasher(hash_content, share_content)


async def hasher(hash_string, share_string):
    result = hashlib.md5(hash_string.encode())
    final_hash = result.hexdigest()
    check_hash = get_hash(final_hash)
    if not check_hash:
        add_hash(final_hash)
        print(final_hash)
        await bot.send_message(chat_id=668069993, text=share_string)
    else:
        print("No Changes")


def remSpace(limiter, string):
    return limiter.join(string.split())
