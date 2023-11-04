from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.index.index import appindex
from routes.personaje.personaje import apppersonaje
from routes.juego.juego import appjuego
from routes.consola.consola import appconsola

app = Flask(__name__)
app.register_blueprint(appindex)
app.register_blueprint(apppersonaje)
app.register_blueprint(appjuego)
app.register_blueprint(appconsola)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate =Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename='logs.log')
