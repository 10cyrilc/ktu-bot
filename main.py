import asyncio
from helpers.scrapper import scrape
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    logger.warning("App is Running")
    loop.run_until_complete(scrape(logger))
