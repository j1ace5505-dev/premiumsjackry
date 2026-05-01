import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
    
    # QRIS Payment
    QRIS_API_KEY = os.getenv('QRIS_API_KEY')
    QRIS_MERCHANT_ID = os.getenv('QRIS_MERCHANT_ID')
    QRIS_API_URL = os.getenv('QRIS_API_URL')
    QRIS_API_SECRET = os.getenv('QRIS_API_SECRET')
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///premium_sales.db')
    DATABASE_ECHO = os.getenv('DATABASE_ECHO', False)
    
    # Admin
    ADMIN_ID = int(os.getenv('ADMIN_ID', 0))
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
    
    # App
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    TIMEZONE = os.getenv('TIMEZONE', 'Asia/Jakarta')

settings = Settings()
