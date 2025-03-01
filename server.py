from flask import Flask, render_template
import html_grabber as soup 

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/get_url', methods=['POST'])
def url():
    return render_template('dashboard-channel.html')