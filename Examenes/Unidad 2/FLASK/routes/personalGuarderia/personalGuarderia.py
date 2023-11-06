from flask import Blueprint, request, redirect, render_template, url_for
from models import PersonalGuarderia
from forms import PersonalGuarderiaForm
from app import db

apppersonal = Blueprint('apppersonal', __name__, template_folder="templates/personalGuarderia")

@apppersonal.route('/')
@apppersonal.route('/index')
@apppersonal.route('/indexPersonalGuarderia')
def inicio():
    personal_guarderia = PersonalGuarderia.query.all()
    return render_template('personalGuarderia/indexPersonalGuarderia.html', personal_guarderia=personal_guarderia)

@apppersonal.route('/agregarPersonalGuarderia', methods=["GET", "POST"])
def agregarPersonalGuarderia():
    personal_guarderia = PersonalGuarderia()
    personal_guarderiaForm = PersonalGuarderiaForm(obj=personal_guarderia)
    if request.method == "POST":
        if personal_guarderiaForm.validate_on_submit():
            personal_guarderiaForm.populate_obj(personal_guarderia)
            db.session.add(personal_guarderia)
            db.session.commit()
            return redirect(url_for('apppersonal.inicio'))
    return render_template('personalGuarderia/agregarPersonalGuarderia.html', forma=personal_guarderiaForm)

@apppersonal.route("/editarPersonalGuarderia/<int:id>", methods=["GET", "POST"])
def editarPersonalGuarderia(id):
    personal_guarderia = PersonalGuarderia.query.get_or_404(id)
    personal_guarderiaForm = PersonalGuarderiaForm(obj=personal_guarderia)
    if request.method == "POST":
        if personal_guarderiaForm.validate_on_submit():
            personal_guarderiaForm.populate_obj(personal_guarderia)
            db.session.commit()
            return redirect(url_for('apppersonal.inicio'))
    return render_template('personalGuarderia/editarPersonalGuarderia.html', forma=personal_guarderiaForm)

@apppersonal.route('/eliminarPersonalGuarderia/<int:id>')
def eliminarPersonalGuarderia(id):
    personal_guarderia = PersonalGuarderia.query.get_or_404(id)
    db.session.delete(personal_guarderia)
    db.session.commit()
    return redirect(url_for('apppersonal.inicio'))

@apppersonal.route('/detallePersonalGuarderia/<int:id>')
def detallePersonalGuarderia(id):
    personal_guarderia = PersonalGuarderia.query.get_or_404(id)
    return render_template('personalGuarderia/detallePersonalGuarderia.html', personal_guarderia=personal_guarderia)
