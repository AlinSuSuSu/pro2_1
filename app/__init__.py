from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import config
from flask_uploads import IMAGES,patch_request_class, UploadSet,configure_uploads
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
photos=UploadSet('photos',IMAGES)
#登录
login_manager = LoginManager()
login_manager.session_protection = "Strong"
login_manager.login_view = 'auth.login'

#工厂函数
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    configure_uploads(app, photos)
    patch_request_class(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .staff import staff as staff_blueprint
    app.register_blueprint(staff_blueprint,url_prefix='/staff')

    from .auth import auth  as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    from .house import house as house_blueprint
    app.register_blueprint(house_blueprint,url_prefix='/house')

    from .community import community as community_blueprint
    app.register_blueprint(community_blueprint, url_prefix='/community')

    from .finance import finance as finance_blueprint
    app.register_blueprint(finance_blueprint, url_prefix='/finance')

    from .file import file as file_blueprint
    app.register_blueprint(file_blueprint, url_prefix='/file')

    return app






