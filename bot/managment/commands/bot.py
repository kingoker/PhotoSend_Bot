from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram import Update



# Объявление переменной бота
bot = TeleBot("6420728934:AAFO0dV1MRDhRJ_Inztqc-onQmh9TTj_wxI", threaded=False)

def do_echo(update: Update,)

# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()				# Загрузка обработчиков
        bot.infinity_polling()						# Бесконечный цикл бота