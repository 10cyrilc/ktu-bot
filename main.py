import asyncio
from helpers.scrapper import scrape


loop = asyncio.get_event_loop()
loop.run_until_complete(scrape())
