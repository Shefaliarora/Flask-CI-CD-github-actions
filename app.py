from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "CI/CD Demo is working!"

HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
62d1412... updated app.py
