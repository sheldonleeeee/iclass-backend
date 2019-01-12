from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix='/api')
    # 如果使用了这个参数，注册后蓝本中定义的 所有路由都会加上指定的前缀，即这个例子中的 /api
    return app
