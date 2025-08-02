from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return redirect(url_for('register'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)