import telebot
import json

class TelegramBot:
    def __init__(self, api_token, id_channel):
        self.api_token = api_token
        self.bot = telebot.TeleBot(self.api_token)
        self.id_channel = id_channel

    def send_message_selective_process(self, selective_process_list):
        if selective_process_list:
            for i in selective_process_list:
                self.bot.send_message(self.id_channel, 
    "📢 Novo Processo Seletivo Disponível!\n\n"
    f"🎯 {i}\n\n"
    "🔗 Acesse o site do IFRN: https://processoseletivo.ifrn.edu.br"
)
