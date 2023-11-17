 # app/controllers/__init__.py
from . import default
from .default import default_bp

def init_app(app):
    from . import default  # Importando dentro da função para evitar importação circular
    app.register_blueprint(default.default_bp)