from flask import Blueprint, request, redirect, render_template, url_for
from models import Juego
from forms import JuegoForm
from app import db

appjuego = Blueprint('appjuego', __name__, template_folder="templates/juego")

@appjuego.route('/indexJuego')
def inicio():
    juegos = Juego.query.all()
    return render_template('juego/indexJuego.html', juegos=juegos)

@appjuego.route('/agregarJuego', methods=["GET", "POST"])
def agregarJuego():
    juego = Juego()
    juegoForm = JuegoForm(obj=juego)
    if request.method == "POST":
        if juegoForm.validate_on_submit():
            juegoForm.populate_obj(juego)
            db.session.add(juego)
            db.session.commit()
            return redirect(url_for('appjuego.inicio'))
    return render_template('juego/agregarJuego.html', forma=juegoForm)

@appjuego.route("/editarJuego/<int:id>", methods=["GET", "POST"])
def editarJuego(id):
    juego = Juego.query.get_or_404(id)
    juegoForm = JuegoForm(obj=juego)
    if request.method == "POST":
        if juegoForm.validate_on_submit():
            juegoForm.populate_obj(juego)
            db.session.commit()
            return redirect(url_for('appjuego.inicio'))
    return render_template('juego/editarJuego.html', forma=juegoForm)

@appjuego.route('/eliminarJuego/<int:id>')
def eliminarJuego(id):
    juego = Juego.query.get_or_404(id)
    db.session.delete(juego)
    db.session.commit()
    return redirect(url_for('appjuego.inicio'))

@appjuego.route('/detalleJuego/<int:id>')
def detalleJuego(id):
    juego = Juego.query.get_or_404(id)
    return render_template('juego/detalleJuego.html', juego=juego)

