from config.default import *

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
    os.path.join(BASE_DIR, 'pybo.db')
)

SQLALCHEMY_TRACK_MODIFICATION=False


SECRET_KEY=b'a\xd6\xf2\x15\x0c&Os\xde\xba\xf790\xe0A\t'