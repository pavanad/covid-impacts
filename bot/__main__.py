# -*- coding: utf-8 -*-

import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from .config.settings import TELEGRAM_TOKEN
from .services.queries import (
    get_city_data,
    get_economic_data,
    get_predict_data,
    get_state_data,
)

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    message = f"E ai {context.message.chat.first_name}!\n"
    message += "Eu sou um bot para deixá-lo informado sobre os impactos na econômia brasileira face a pandemia do Covid-19.\n"
    message += "Meus comandos são:\n /cidade /estado /previsao /economia"
    update.send_message(chat_id=context.message.chat_id, text=message)


def get_city(update, context, args):
    try:
        city = args[0]
        data = get_city_data(city)
        message = "Desculpe não localizei a cidade que vc digitou!"
        if len(data):
            message = f"Essa é a última informação que consegui sobre {city}:\n"
            message += f"Número de casos confirmados: {data[0][3]}\n"
            message += f"Número de mortes: {data[0][4]}\n"
            message += f"Latitude: {data[0][5]}\n"
            message += f"Longitude: {data[0][6]}\n"

        update.send_message(
            chat_id=context.message.chat_id, text=message,
        )
    except (IndexError, ValueError):
        update.send_message(
            chat_id=context.message.chat_id, text="Como usar:\n/cidade <nome da cidade>"
        )
    except Exception as error:
        logger.error(f"{error}")


def get_state(update, context, args):
    try:
        state = args[0]
        data = get_state_data(state)
        message = "Desculpe não localizei a estado que vc digitou!"
        if len(data):
            message = f"Essa é a última informação que consegui sobre {state}:\n"
            message += f"Número de casos confirmados: {data[0][2]}\n"
            message += f"Número de mortes: {data[0][3]}\n"
            message += f"Taxa de mortalidade: {round(data[0][7],2)}%\n"
            message += f"Número de recuperados: {data[0][6]}\n"
            message += f"Taxa de recuperados: {round(data[0][8],2)}%\n"
            message += f"Latitude: {data[0][4]}\n"
            message += f"Longitude: {data[0][5]}\n"

        update.send_message(
            chat_id=context.message.chat_id, text=message,
        )
    except (IndexError, ValueError):
        update.send_message(
            chat_id=context.message.chat_id,
            text="Como usar:\n/estado <sigla do estado>",
        )
    except Exception as error:
        logger.error(f"{error}")


def get_predict(update, context, args):
    try:
        messgage = ""
        predict_type = args[0]
        predict_list = ["confirmados", "mortes"]

        if predict_type not in predict_list:
            message = "Desculpe! Até o momento eu consigo fazer previsões apenas "
            message += "para os casos confirmados e mortes por covid-19."
        else:
            data = get_predict_data(predict_type)
            last_four_days = data[-4:]
            message = f"Meu modelo de previsão sempre considera 3 dias após o último número confirmado\n\n"
            message += f"Então vou te mostrar os últimos números reais em comparação a minha previsão:\n"
            message += (
                f"{predict_type.lower().title()} reais: {int(last_four_days[0][2])}\n"
            )
            message += (
                f"Previsão de {predict_type.lower()}: {int(last_four_days[0][1])}\n\n"
            )
            message += f"Agora vou mostrar minha previsão para os próximos 3 dias:\n"
            for i in range(1, 4):
                message += f"Previsão dia {i}: {int(last_four_days[i][1])}\n"

        update.send_message(
            chat_id=context.message.chat_id, text=message,
        )
    except (IndexError, ValueError):
        update.send_message(
            chat_id=context.message.chat_id,
            text="Como usar:\n/previsao <digite confirmados/mortes>",
        )
    except Exception as error:
        logger.error(f"{error}")


def get_economic(update, context):
    try:
        data = get_economic_data()
        message = "Desculpe não estou encontrando meus dados sobre econômia!"
        if len(data):
            message = "Ainda estou aprendendo sobre esse assunto, "
            message += "mas vou tentar mostrar os últimos dados que consegui:\n\n"

            inad = dsoc = ipca = inpc = 0
            for item in reversed(data):
                date_str = item[1].strftime("%m/%Y")
                if item[9] is not None and ipca == 0:
                    ipca = item[9]
                    message += (
                        f"IPCA - indicador para inflação em {date_str}: {ipca}%\n"
                    )
                if item[10] is not None and inpc == 0:
                    inpc = item[10]
                    message += (
                        f"INPC - indicador para salários em {date_str}: {inpc}%\n"
                    )
                if item[11] is not None and inad == 0:
                    inad = item[11]
                    message += f"Inadimplência em {date_str}: {inad}%\n"
                if item[12] is not None and dsoc == 0:
                    dsoc = item[12]
                    message += f"Desemprego a cada mil em {date_str}: {dsoc}\n"

            date_str = data[-1][1].strftime("%m/%Y")
            message += f"Cotação do dólar em {date_str}: R$ {round(data[-1][2], 2)}\n\n"
            message += f"Em breve vou mostrar outros indicadores e algumas previsões!"

        update.send_message(
            chat_id=context.message.chat_id, text=message,
        )
    except Exception as error:
        logger.error(f"{error}")


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("cidade", get_city, pass_args=True))
    dispatcher.add_handler(CommandHandler("estado", get_state, pass_args=True))
    dispatcher.add_handler(CommandHandler("previsao", get_predict, pass_args=True))
    dispatcher.add_handler(CommandHandler("economia", get_economic))

    # start the bot
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
