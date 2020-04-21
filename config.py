import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b"\xa96vgj\x92\xda\xcc+\x9e\x11%\xcd'\x16]"

    MONGODB_SETTINGS = { 'db' : 'Enrollment'}
