# -*- coding: utf-8 -*-

import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from config.settings import TELEGRAM_TOKEN

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    response_message = f"E ai {context.message.chat.first_name}!\n"
    response_message += "Eu sou um bot para deixá-lo informado sobre os impactos na econômia brasileira face a pandemia do Covid-19.\n"
    response_message += "Meus comandos são:"
    update.send_message(chat_id=context.message.chat_id, text=response_message)


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    # start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
