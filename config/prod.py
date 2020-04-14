import os
import redis
DEBUG = False
SECRET_KEY=os.urandom(24)
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS=False


# SESSION_TYPE = 'redis'
# SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))
# SESSION_TYPE = os.environ.get('SESSION_TYPE')
# SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))
