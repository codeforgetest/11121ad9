# a-discord-bot
# a discord bot dashboard website which has invite and support links and all bot features list
# This file was auto-generated by CodeForge AI

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "development_secret")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
