from config import token
from aiogram import types, Dispatcher, Bot, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from OpenAI_bot import chat_bot


__all__ = [
    "ALGA",
    "TelegramBot"
]


class TelegramBot:
    """_summary_
    """
    def __init__(self) -> None:
        self.token = token


    def creat_dispatch(self) -> None:

        bot = Bot(token=self.token)
        dp = Dispatcher(bot=bot)

        return dp

    
class Handler(TelegramBot):
    def __init__(self) -> None:
        super().__init__()


class Bottom(TelegramBot):
    def __init__(self) -> None:
        super().__init__()
        
    
def main():
    dp = TelegramBot().creat_dispatch()
    eng_lvl = None

    @dp.message_handler(commands=['start'])
    async def cmd_start(msg: types.Message):
        await msg.answer("""Hello! Welcome!\nSend me the book in pdf format >>>    """)

    @dp.message_handler()
    async def new_message(message: types.Message):
        input_text = str(message.text)

        if input_text:
            await message.answer(chat_bot(input_text))
    
    
    return dp


if __name__ == "__main__":
    dp = main() 
    executor.start_polling(dp)









    
