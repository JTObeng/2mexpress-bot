	from flask import Flask, request, jsonify 

import os 

import requests 

 

app = Flask(__name__) 

 

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN") 

WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN") 

PHONE_NUMBER_ID = os.environ.get("PHONE_NUMBER_ID") 

 

@app.route("/webhook", methods=["GET"]) 

def verify_webhook(): 

    mode = request.args.get("hub.mode") 

    token = request.args.get("hub.verify_token") 

    challenge = request.args.get("hub.challenge") 

    if mode == "subscribe" and token == VERIFY_TOKEN: 

        return challenge, 200 

    return "Verification failed", 403 

 

@app.route("/webhook", methods=["POST"]) 

def webhook(): 

    data = request.get_json() 

    print(data) 

    return jsonify({"status": "ok"}), 200 

 

@app.route("/", methods=["GET"]) 

def home(): 

    return "Bot is running", 200 

 

if __name__ == "__main__": 

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) 
