import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Укажите ваш Telegram API и chat_id
TELEGRAM_API_URL = "https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage"
CHAT_ID = "YOUR_CHAT_ID"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def handle_form_submission():
    # Получаем данные из формы
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
