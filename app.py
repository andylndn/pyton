from flask import Flask, request
import requests

app = Flask(__name__)

# Вставьте ваш Telegram Bot API Token сюда
TELEGRAM_API_URL = 'https://api.telegram.org/bot7679289773:AAELewdGiJT_pRAimlMhyjVTXeT_qceZIm4/sendMessage'
CHAT_ID = 'your_chat_id'  # Замените на ваш ID чата

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Artist's Website!"

@app.route('/submit_form', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    phone = request.form['phone']
    artwork = request.form['artwork']

    # Формируем сообщение для отправки в Telegram
    message = f"Получена заявка:\nИмя: {name}\nТелефон: {phone}\nИнтересующая картина: {artwork}"

    # Отправляем сообщение в Telegram
    response = requests.post(TELEGRAM_API_URL, data={
        'chat_id': CHAT_ID,
        'text': message
    })

    if response.status_code == 200:
        return "Спасибо за заявку! Мы свяжемся с вами.", 200
    else:
        return "Произошла ошибка. Попробуйте позже.", 500

if __name__ == '__main__':
    app.run(debug=True)
