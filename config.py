import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fitpulse-super-secret-key-2026')
    SITE_NAME = "FitPulse | Gen-Z Student Fitness & Nutrition"
    SITE_BASE_URL = os.environ.get('SITE_BASE_URL', 'http://localhost:5000')
    GOOGLE_SITE_VERIFICATION = os.environ.get( 'GOOGLE_SITE_VERIFICATION','JYJaASZZMoXFtEga0kkotXG5sjCcCHUos-au9TCeLiA')
    # Database Configuration:
    # 1. First preference: DATABASE_URL environment variable (PostgreSQL connection string)
    # 2. Render / Supabase / Neon fix: convert postgres:// to postgresql://
    # 3. Fallback: local SQLite file so it works out of the box without any setup needed!
    raw_db_url = os.environ.get('DATABASE_URL')
    if raw_db_url:
        if raw_db_url.startswith("postgres://"):
            raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = raw_db_url
    else:
        # Default local SQLite database file for zero-config running
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'fitness_blog.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
