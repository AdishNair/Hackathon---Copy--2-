from flask import Flask, render_template, request, jsonify
import sys
import os

# Dynamically add path to src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from predict import predict_email, predict_url, predict_sender

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict/email', methods=['POST'])
def email_predict():
    text = request.form.get('email_text')
    result = predict_email(text)
    return jsonify({'result': result})

@app.route('/predict/url', methods=['POST'])
def url_predict():
    url = request.form.get('url')
    result = predict_url(url)
    return jsonify({'result': result})

@app.route('/predict/sender', methods=['POST'])
def sender_predict():
    sender = request.form.get('sender')
    result = predict_sender(sender)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
