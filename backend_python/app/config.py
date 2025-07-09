from dotenv import load_dotenv
import os

load_dotenv()

# Debug connection string
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
print(f"DB_NAME: {os.getenv('DB_NAME')}")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT", "3306")}/{os.getenv("DB_NAME")}?charset=utf8mb4'

# Thêm JWT Secret Key
JWT_SECRET_KEY = 'your-super-secret-jwt-key-here-change-in-production'
SECRET_KEY = 'your-super-secret-flask-key-here-change-in-production'

# Cấu hình JWT
JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 giờ
JWT_REFRESH_TOKEN_EXPIRES = 2592000  # 30 ngày

print(f"Connection URI: {SQLALCHEMY_DATABASE_URI}")