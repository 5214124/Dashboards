from flask import Flask, render_template, request
import html_grabber as soup 

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/get_url', methods=['POST'])
def url():
    if 'text_url' not in request.form:
        return "Invalid request: 'text_url' not found", 400

    req = request.form['text_url']

    if '@' in req:
        return render_template('dashboard-channel.html')
    else:
        return 'Placeholder'
    
if __name__ == '__main__':
    app.run(debug=True)