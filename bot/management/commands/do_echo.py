import asyncio
import datetime
import logging
import sys

import schedule
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from asgiref.sync import sync_to_async
from django.core.management import BaseCommand

from bot.models import TaskManager
from core import settings

dp = Dispatcher()
bot = Bot(settings.BOT_TOKEN, parse_mode=ParseMode.HTML)



async def send_photo():

    tasks = await get_all_task()

    if tasks != []:
        for task in tasks:
            image = FSInputFile('media/' + str(task.image))
            await bot.send_photo(-1001949060344, image)
            image = FSInputFile('media/'+ str(task.image))
            await bot.send_document(-1001949060344, image)



        await save_all(tasks)


@sync_to_async
def save_all(tasks):
    for task in tasks:
        task.published = True
        task.save()

@sync_to_async
def get_all_task():
    date = datetime.date.today()

    task = TaskManager.objects.filter(published=False, task_date__year=date.year, task_date__month=date.month, task_date__day=date.day, task_time__lte=datetime.datetime.now().strftime("%H:%M"))

    return list(task)

async def main():
    await periodic_call()
    await dp.start_polling(bot)

async def periodic_call():
    while True:
        await send_photo()
        await asyncio.sleep(5)


class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())




