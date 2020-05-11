import os


class Config:
    SECRET_KEY = 'f8d35b418f70c0ab25119ec5313f05c7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db?check_same_thread=False'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
