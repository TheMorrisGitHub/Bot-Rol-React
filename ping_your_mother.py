from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello. I ping you sweetie"

def run():
  app.run(host='0.0.0.0',port=8080)

def ping_your_mother():
    t = Thread(target=run)
    t.start()