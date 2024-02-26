DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///works.db'
SQLALCHEMY_BINDS = {'contacts_db': 'sqlite:///contacts.db'}
SQLALCHEMY_TRACK_MODIFICATIONS = True