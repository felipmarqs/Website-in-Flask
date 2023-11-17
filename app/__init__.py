from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager    

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Configuração do SQLAlchemy e Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Importe os modelos SQLAlchemy aqui
    from app.models.tables import Post, User

    #Adiciona rotas
    from app.controllers import default_bp
    app.register_blueprint(default_bp)

    login_manager.login_view = '/login/'  # Substitua 'login' pela rota da sua página de login

    return app
