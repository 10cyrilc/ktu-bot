# KTU Bot

The KTU Bot is a Python-based bot that scrapes data from the Kerala Technological University (KTU) official website to provide you with the latest announcements. It retrieves information from the [KTU Announcements page](https://ktu.edu.in/eu/core/announcements.htm) and delivers updates to your channel or chat.

## Demo

Live Working Demo on [KTU Announcements](https://t.me/ktu_announcement)

## Features

- Scrapes the KTU Announcements page for the latest updates.
- Sends notifications to your Telegram chat.
- Easy setup and configuration using environment variables.

## Installation

1. Clone this GitHub repository to your local machine:

   ```shell
   git clone https://github.com/10cyrilc/ktu-bot.git
   ```

2. Change to the project directory:

   ```shell
   cd ktu-bot
   ```

3. Create a virtual environment to install the dependencies:

   ```shell
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For macOS/Linux:

     ```shell
     source venv/bin/activate
     ```

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Rename the `.env.example` file to `.env`.

7. Open the `.env` file and set the following variables:

   - `MONGO_URI`: The connection URI for your MongoDB database.
   - `SESSION_NAME`: A unique identifier for your bot session.
   - `BOT_ID`: The ID of your Telegram bot from [@Botfather](https://t.me/BotFather).
   - `CHAT_ID`: The identifier for the Telegram chat where you want to receive notifications.

8. Setup a cron job to run the bot script every 5 minutes:

   - Open your crontab file:

     ```shell
     crontab -e
     ```

   - Add the following line to the file:

     ```shell
     */5 * * * * /path/to/python3 /path/to/ktu-announcement-bot/main.py
     ```

     Replace `/path/to/python3` with the absolute path to your Python 3 executable, and replace `/path/to/ktu-announcement-bot/main.py` with the absolute path to the `main.py` script of the bot.

   - Save the crontab file.

## Usage

The KTU Bot will now run as a scheduled cron job, scraping the KTU Announcements page and sending notifications to your specified Telegram chat every 5 minutes.

## Contributing

Contributions to the KTU Bot are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. You can also submit pull requests with your proposed changes.

## License

The KTU Bot is licensed under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to the developers of the libraries and frameworks used in this project:

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Used for web scraping.
- [python-telegram-bot](https://python-telegram-bot.org/): Used for Telegram bot integration.
- [pymongo](https://pymongo.readthedocs.io/): Used for MongoDB integration.

## Authors

- [@10cyrilc](https://www.github.com/10cyrilc)

## Support Me

<a href="https://www.buymeacoffee.com/10cyrilc" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
