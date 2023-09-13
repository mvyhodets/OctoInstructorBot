from configs import *

BOT_TOKEN = os.environ['BOT_TOKEN']
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):

  # Инициируем веб-приложение
  app = await my_webapp.make_start_step()

  # Отправляем информацию о приложении
  await bot.send_message(
      message.chat.id,
      text="Авторизуйтесь через приложение",
      reply_markup=types.ReplyMarkup.inline_keyboard(
          [[types.InlineKeyboardButton(text="Открыть приложение", web_app=app)]]
      )
  )

  # Сохраняем текущее состояние
  await state.set_state("waiting_for_webapp_auth")

@dp.web_app_query()
async def auth_callback(query: types.WebAppQuery, state: FSMContext):

  # Обработка ответа от приложения
  user_data = await my_webapp.process_auth(query.data)

  if user_data:
    # авторизация прошла успешно
    await state.finish()
  else:
    pass


def main():
  dp.start_polling()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    logging.error("Bot stopped")
    dp.storage.close()