from libs.libslist import *
base = sqlite3.connect('data.db')
cur = base.cursor()
base.execute('CREATE TABLE IF NOT EXISTS users(name VARCHAR(256),id VARCHAR(300))')
base.commit()