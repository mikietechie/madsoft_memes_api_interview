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
MINIO_PROTOCOL = env.get("MINIO_PROTOCOL")
MINIO_ENDPOINT = env.get("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = env.get("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = env.get("MINIO_SECRET_KEY")
MINIO_BUCKET = env.get("MINIO_BUCKET")
MINIO_SECURE = MINIO_PROTOCOL == "https"
MINIO_ADDRESS = f"{MINIO_PROTOCOL}://{MINIO_ENDPOINT}"
