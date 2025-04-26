from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ваш токен бота
TELEGRAM_BOT_TOKEN = '7679289773:AAELewdGiJT_pRAimlMhyjVTXeT_qceZIm4'

def start(update: Update, context: CallbackContext) -> None:
    """Обработка команды /start"""
    # Приветственное сообщение, которое будет отправляться при команде /start
    update.message.reply_text(f"Hello {update.message.from_user.first_name}! Welcome to the Artist's Gallery. Type your inquiry.")

def handle_message(update: Update, context: CallbackContext) -> None:
    """Обработка текстовых сообщений"""
    update.message.reply_text("Thank you for reaching out! We will respond to your inquiry shortly.")

def main():
    """Запуск бота"""
    # Создаём обновитель, который будет подключаться к Telegram API
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # Получаем диспетчера для обработки сообщений
    dispatcher = updater.dispatcher

    # Добавляем обработчик для команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Добавляем обработчик для текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()
