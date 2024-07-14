from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB = BASE_DIR / "db.sqlite3"


# $env:FLASK_DEBUG="True"


class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    TESTING = True
