from flask import Blueprint,render_template

appindex =Blueprint('appindex',__name__,template_folder="templates")

@appindex.route('/')
@appindex.route('/index')
def index():
    return render_template('index.html')