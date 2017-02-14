# -*- coding: UTF-8 -*-
from redis import  Redis

class Config:

    rs = Redis(host='192.168.0.203', port=6379, db=6)  # password='1'
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RTxxxxx'
    SESSION_TYPE = u'redis'
    SESSION_REDIS = rs

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    # 'production': ProductionConfig,
    #  'heroku': HerokuConfig,
    #  'unix': UnixConfig,

    'default': DevelopmentConfig
}