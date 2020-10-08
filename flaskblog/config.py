import os

class Config:
    SECRET_KEY = '0c4b45ccd5a50c08739cfe54a0cf2d14'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

    # # app.config['DEBUG'] = True
    # # app.config['TESTING'] = False
    # app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    # app.config['MAIL_PORT'] = 587
    # # app.config['MAIL_USE_SSL'] = False
    # app.config['MAIL_USE_TLS'] = True
    # # app.config['MAIL_DEBUG'] = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    # # app.config['MAIL_DEFAULT_SENDER'] = None
    # # app.config['MAIL_MAX_EMAIL'] = None
    # # app.config['MAIL_SUPPRESS_SEND'] = False
    # # app.config['MAIL_ASCII_ATTACHMENTS'] = False