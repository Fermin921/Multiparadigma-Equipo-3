from flask import Blueprint, request, redirect, render_template, url_for
from models import Consola
from forms import ConsolaForm
from app import db

appconsola = Blueprint('appconsola', __name__, template_folder="templates/consola")

@appconsola.route('/indexConsola')
def inicio():
    consolas = Consola.query.all()
    return render_template('consola/indexConsola.html', consolas=consolas)

@appconsola.route('/agregarConsola', methods=["GET", "POST"])
def agregarConsola():
    consola = Consola()
    consolaForm = ConsolaForm(obj=consola)
    if request.method == "POST":
        if consolaForm.validate_on_submit():
            consolaForm.populate_obj(consola)
            db.session.add(consola)
            db.session.commit()
            return redirect(url_for('appconsola.inicio'))
    return render_template('consola/agregarConsola.html', forma=consolaForm)

@appconsola.route("/editarConsola/<int:id>", methods=["GET", "POST"])
def editarConsola(id):
    consola = Consola.query.get_or_404(id)
    consolaForm = ConsolaForm(obj=consola)
    if request.method == "POST":
        if consolaForm.validate_on_submit():
            consolaForm.populate_obj(consola)
            db.session.commit()
            return redirect(url_for('appconsola.inicio'))
    return render_template('consola/editarConsola.html', forma=consolaForm)

@appconsola.route('/eliminarConsola/<int:id>')
def eliminarConsola(id):
    consola = Consola.query.get_or_404(id)
    db.session.delete(consola)
    db.session.commit()
    return redirect(url_for('appconsola.inicio'))

@appconsola.route('/detalleConsola/<int:id>')
def detalleConsola(id):
    consola = Consola.query.get_or_404(id)
    return render_template('consola/detalleConsola.html', consola=consola)
