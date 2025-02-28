from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    message = os.getenv("APP_MESSAGE", "Hello, Docker!")
    return f"<h1>{message}</h1>"

@app.route('/db')
def test_db():
    """Test connection to PostgreSQL"""
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        return "<h1>Database Connected Successfully! 🎉</h1>"
    except Exception as e:
        return f"<h1>Database Connection Failed! ❌</h1><p>{e}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
