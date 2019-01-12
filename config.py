# -*- coding:utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

from local_config import DBConfig


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_POSTS_PER_PAGE = os.environ.get('FLASKY_POSTS_PER_PAGE') or 20
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # whoosh索引数据库位置
    # WHOOSH_BASE = 'mysql://root:password@localhost/search.db'

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    whiski_db_uri = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(**DBConfig.local)
    SQLALCHEMY_DATABASE_URI = whiski_db_uri


config = DevelopmentConfig()
