from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PersonajeForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    descripcion = StringField('Descripcion',validators=[DataRequired()])
    franquicia = StringField('Franquicia',validators=[DataRequired()])
    habilidades = StringField('Habilidades',validators=[DataRequired()])
    fecha_creacion = StringField('Fecha de Creacion',validators=[DataRequired()])
    imagen = StringField('Ruta de Imagen',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class JuegoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fecha_lanzamiento = StringField('Fecha de Lanzamiento',validators=[DataRequired()])
    genero = StringField('Genero',validators=[DataRequired()])
    copias_vendidas = IntegerField('Copias Vendidas',validators=[DataRequired()])
    imagen = StringField('Ruta de Imagen',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class ConsolaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fecha_lanzamiento = StringField('Fecha de Lanzamiento',validators=[DataRequired()])
    generacion = StringField('Generacion',validators=[DataRequired()])
    consolas_vendidas = IntegerField('Consolas de Vendidas',validators=[DataRequired()])
    imagen = StringField('Ruta de Imagen',validators=[DataRequired()])
    enviar = SubmitField('Enviar')
