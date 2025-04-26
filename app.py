from flask import Flask, request, redirect, url_for
import requests

app = Flask(__name__)

# Replace with your bot's Telegram API token and chat ID
TELEGRAM_BOT_TOKEN = '7679289773:AAELewdGiJT_pRAimlMhyjVTXeT_qceZIm4'
CHAT_ID = 'your_chat_id'  # Your Telegram chat ID

@app.route('/')
def home():
    return "Welcome to the Artist's Gallery!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    artwork = request.form['artwork']
    
    # Prepare the message for Telegram
    message = f"New inquiry:\nName: {name}\nPhone: {phone}\nInterested Artwork: {artwork}"
    
    # Send the message to Telegram bot
    send_message_to_telegram(message)
    
    # Redirect back to home page after submission
    return redirect(url_for('home'))

def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Failed to send message to Telegram")
    else:
        print("Message sent to Telegram successfully")

if __name__ == '__main__':
    app.run(debug=True)
