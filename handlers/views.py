import logging

from aiogram.filters import Command
from aiogram.types import Message

from config.bot import router, bot
from handlers.core.bot_table import TableView

logger = logging.getLogger(__name__)


@router.message(Command('answers'))
async def table_view_command(message: Message):
    table_view = TableView()
    table = table_view.show_by_rows()

    await bot.send_message(chat_id=message.chat.id, text=f'<pre>{table.get_string()}</pre>')
