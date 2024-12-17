from flask import Flask, render_template
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = "jamell-website-secret-key"

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/page2')
def page2():
    return render_template('page2.html', active_page='page2')

@app.route('/page3')
def page3():
    return render_template('page3.html', active_page='page3')

@app.route('/page4')
def page4():
    return render_template('page4.html', active_page='page4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
