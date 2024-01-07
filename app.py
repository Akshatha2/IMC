from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'AJ\'s web application!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

