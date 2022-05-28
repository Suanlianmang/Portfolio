import environ

env = environ.Env()

environ.Env.read_env()
class Keys():
    DEBUG = env('DEBUG')
    SECRET_KEY = env('SECRET_KEY')
    DB_NAME = env('DB_NAME')
    DB_USER = env('DB_USER')
    DB_PASSWORD = env('DB_PASSWORD')
keys = Keys()
