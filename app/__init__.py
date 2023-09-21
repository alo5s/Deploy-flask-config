from flask import Flask
# Impor la config
from config import Config, DevelopmentConfig
# Import la routes
from .routes import inicio_bp

app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
app.config.from_object(DevelopmentConfig)


app.register_blueprint(inicio_bp)