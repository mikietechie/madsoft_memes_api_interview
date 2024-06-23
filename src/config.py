import os

from dotenv import load_dotenv

load_dotenv(override=True)
env = os.environ

# Server Conf
PROTOCOL = env.get("APP_PROTOCOL", "http")
HOST = env.get("APP_HOST", "0.0.0.0")
PORT = int(env.get("APP_PORT", 8000))
ADDRESS = f"{PROTOCOL}://{HOST}:{PORT}"
PROD = env.get("ENV") == "production"

# Database
DB_URI = env.get("DB_URI", "sqlite://db.sqlite3")

# AWS
AWS_REGION = env.get("AWS_REGION")
AWS_ACCESS_KEY_ID = env.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.get("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET = env.get("AWS_BUCKET")
AWS_KEY = env.get("AWS_KEY")
