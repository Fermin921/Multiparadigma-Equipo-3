from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField,DateField
from wtforms.validators import DataRequired

class NiñoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    genero = StringField('Género')
    tutor_principal = StringField('Tutor Principal', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class TutorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    direccion = StringField('Dirección')
    numero_telefono = StringField('Número de Teléfono', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class PersonalGuarderiaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    puesto = StringField('Puesto')
    fecha_contratacion = DateField('Fecha de Contratación', format='%Y-%m-%d', validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class AulaForm(FlaskForm):
    nombre_aula = StringField('Nombre de Aula', validators=[DataRequired()])
    capacidad_maxima = IntegerField('Capacidad Máxima')
    edades_admitidas = StringField('Edades Admitidas')
    maestro_a_cargo = StringField('Maestro a Cargo')
    enviar = SubmitField('Enviar')

class ComidaForm(FlaskForm):
    nombre_comida = StringField('Nombre de Comida', validators=[DataRequired()])
    ingredientes = StringField('Ingredientes')
    restricciones_alimenticias = StringField('Restricciones Alimenticias')
    fecha_introduccion = DateField('Fecha de Introducción', format='%Y-%m-%d', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
