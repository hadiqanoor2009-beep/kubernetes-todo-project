from flask import Flask
from sqlalchemy import create_engine, text
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-service")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "todo")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(DATABASE_URL)

@app.route("/")
def home():
    return """
    <h1>My Kubernetes To-Do App</h1>
    <p>Hello! My Flask application is running.</p>
    """

@app.route("/health")
def health():
    return "OK"

@app.route("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return f"Database connection successful: {result.scalar()}"
    except Exception as e:
        return f"Database connection failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
