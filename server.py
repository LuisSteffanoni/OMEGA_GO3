from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running in OMEGA_GO3!"

if __name__ == '__main__':
    app.run(debug=True)


