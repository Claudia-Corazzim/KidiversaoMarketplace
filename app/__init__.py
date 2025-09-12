from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()
login_manager.login_view = 'main.welcome'
login_manager.login_message = 'Você precisa fazer login para acessar esta página.'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app import routes, models
    app.register_blueprint(routes.bp, url_prefix='/')

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))
        
    # Adicionando filtro para formatar preços no formato brasileiro (com vírgula)
    @app.template_filter('format_price_br')
    def format_price_br(value):
        if value is None:
            return "0,00"
        try:
            # Converte para float e formata com vírgula e dois dígitos
            return f"{float(value):.2f}".replace('.', ',')
        except (ValueError, TypeError):
            return "0,00"

    return app

