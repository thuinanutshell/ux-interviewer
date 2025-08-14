import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-for-testing')
    TESTING = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret_key')
    JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET', 'refresh_secret_key')
    SWAGGER_URL = '/docs'
    SWAGGER_FILE = '/static/swagger.yaml'
    SENDER_EMAIL = os.getenv('SENDER_EMAIL')
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL', 'support@your-domain.com')
    OAUTHLIB_INSECURE_TRANSPORT = os.getenv('FLASK_ENV') == 'development'
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')