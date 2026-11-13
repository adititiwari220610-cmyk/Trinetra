from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    msg = request.form['msg'].lower()

    
    score = 0
    
    if "otp" in msg:
        score += 40
    if "lottery" in msg:
        score += 30
    if "kyc" in msg:
        score += 30
    if "link" in msg:
        score += 20
    if "jeet" in msg:
        score += 25
    if "parcel" in msg:
        score += 20
    if "account band" in msg or "block" in msg:
        score += 30
    if "password" in msg:
        score += 35

    # Score 100 se zyada na ho
    if score > 100:
        score = 100

    # Ab score ke hisaab se result
    if score >= 70:
        result = f"🚨 {score}% SCAM! please don't open."
        color = "red"
    elif score >= 40:
        result = f"⚠️ {score}% Suspecting! Be careful."
        color = "orange"
    elif score > 0:
        result = f"😐 {score}% Little risky."
        color = "#b8860b"
    else:
        result = "✅ 0% - Safe , you can continue."
        color = "green"

    return render_template('index.html', result=result, color=color, score=score)

if __name__ == '__main__':
    app.run(debug=True)