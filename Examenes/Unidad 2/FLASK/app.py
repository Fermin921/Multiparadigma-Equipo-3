from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.niño.niño import appniño
from routes.tutor.tutor import apptutor
from routes.personalGuarderia.personalGuarderia import apppersonal
from routes.aula.aula import appaula
from routes.comida.comida import appcomida

#19100209
app = Flask(__name__)
app.register_blueprint(appniño)
app.register_blueprint(apptutor)
app.register_blueprint(apppersonal)
app.register_blueprint(appaula)
app.register_blueprint(appcomida)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate =Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename='logs.log')
