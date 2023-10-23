from telegram import Update
from telegram.ext import CallbackContext, CallbackContext, Updater, CommandHandler, CommandHandler
import requests 
from bs4 import BeautifulSoup 

def start(update: Update, context: CallbackContext) -> None:
    search = update.message.text.split()[1]
    URL = f"https://kun.uz/news/search?q={search}"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html.parser')
    news = soup.find_all("div", class_="col-md-4")
    for key, item in enumerate(news):
        if key == 10:
            break
        update.message.reply_text(f"{key+1}. https://kun.uz{item.find('a', class_='news__title')['href']}", disable_web_page_preview=True)
        
def main() -> None:
    """Start the bot."""
    updater = Updater("6527372080:AAEcF_9xlU6FG_R2e4Imyd2cPT0QkqL0x3o")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()

