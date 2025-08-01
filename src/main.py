from scrapper_request import Scraper
from telegram_bot import TelegramBot
from json_manage import MessageManage
import json

if __name__ == "__main__":

    ifrn = Scraper("https://processoseletivo.ifrn.edu.br/")

    bot = TelegramBot("8342730791:AAEVICmxzzoDnHK4OtjT00_ImkAIdQeHFKg", -1002736162258)

    test = MessageManage()

    if ifrn.url_request():
        selective_process_list = ifrn.list_selective_process()

        if selective_process_list:
            bot.send_message_selective_process(selective_process_list)
            test.verify_selective_process_list(selective_process_list)
        