from flask import Flask, request
import requests

app = Flask(__name__)

# Ваш токен бота
BOT_TOKEN = '7679289773:AAELewdGiJT_pRAimlMhyjVTXeT_qceZIm4'
# Ваш Telegram ID
CHAT_ID = '263636925'

@app.route('/')
def home():
    return 'Bot and Form Handler are working!'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    artwork = request.form.get('artwork')

    message = f"🎨 New Inquiry:\n👤 Name: {name}\n📞 Phone: {phone}\n🖼 Artwork: {artwork}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

    return 'Form submitted!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
