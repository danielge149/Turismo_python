from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import url_for
from flask import render_template
from os import listdir
from forms import FormCalculadora
from forms import UploadForm
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/home')
def inicio():
    template_base = render_template("base.html")
    template_inicio = render_template("inicio.html")
    return template_base + template_inicio



@app.route('/')
def index():
    return redirect(url_for('inicio'))

# Ruta para '/hoteles'
@app.route('/hoteles')
def hoteles():
    return render_template('hoteles.html')

@app.route('/Restaurantes')
def restaurantes():
    return render_template('restaurantes.html')

# Manejar error 404 (Página no encontrada)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404), 404


@app.route('/hola/')
@app.route('/hola/<nombre>')
def hola(nombre=None):
    return render_template("template1.html", nombre=nombre)


# @app.route('/adicion/<num1>/<num2>')
# def adicion(num1, num2):
#     try:
#         resultado = int(num1) + int(num2)
#     except ValueError:
#         abort(404)
#         # abort(404, "Página NO ENCONTRADA")
#     return render_template("template2.html", num1=num1, num2=num2,
#                            resultado=resultado)


# @app.errorhandler(404)
# def page_not_found(error):
#     return (render_template("error.html", error="Página no encontrada..."),
#             404)
#     # return render_template("error.html", error=error.description), 404


# @app.route('/tabla/<numero>')
# def tabla(numero):
#     try:
#         numero = int(numero)
#     except ValueError:
#         abort(404)
#     return render_template("template3.html", num=numero)


# @app.route('/enlaces')
# def enlaces():
#     enlaces = [{"url": "http://www.google.es", "texto": "Google"},
#                {"url": "http://www.twitter.com", "texto": "Twitter"},
#                {"url": "http://www.facebook.com", "texto": "Facebook"}, ]
#     return render_template("template4.html", enlaces=enlaces)


# -------- Trabajando con Formularios ---------- #

# @app.route("/calculadora_post", methods=["GET", "POST"])
# def calculadora_post():
#     if request.method == "POST":
#         num1 = request.form.get("num1")
#         num2 = request.form.get("num2")
#         operador = request.form.get("operador")
#         try:
#             resultado = eval(num1 + operador + num2)
#         except Exception:
#             return render_template("error.html",
#                                    error="No puedo realizar la operación")
#         return render_template("resultado.html", num1=num1, num2=num2,
#                                operador=operador, resultado=resultado)
#     else:
#         return render_template("calculadora_post.html")


# @app.route("/calculadora_get", methods=["GET"])
# def calculadora_get():
#     if request.method == "GET" and len(request.args) > 0:
#         num1 = request.args.get("num1")
#         num2 = request.args.get("num2")
#         operador = request.args.get("operador")
#         try:
#             resultado = eval(num1 + operador + num2)
#         except Exception:
#             return render_template("error.html",
#                                    error="No puedo realizar la operación")
#         return render_template("resultado.html", num1=num1, num2=num2,
#                                operador=operador, resultado=resultado)
#     else:
#         return render_template("calculadora_get.html")


# @app.route("/calculadora/<operador>/<num1>/<num2>", methods=["GET"])
# def calculadora_var(operador, num1, num2):
#     try:
#         resultado = eval(num1 + operador + num2)
#     except Exception:
#         return render_template("error.html",
#                                error="No puedo realizar la operación")
#     return render_template("resultado.html", num1=num1, num2=num2,
#                            operador=operador, resultado=resultado)


# -------- Generando formularios con flask-wtf ---------- #

# @app.route("/calculadora_wtf", methods=["GET", "POST"])
# def calculadora_wtf():
#     form = FormCalculadora(request.form)
#     if form.validate_on_submit():
#         num1 = form.num1.data
#         num2 = form.num2.data
#         operador = form.operador.data
#         try:
#             resultado = eval(str(num1) + operador + str(num2))
#             print(resultado)
#         except Exception:
#             return render_template("error.html",
#                                    error="No puedo realizar la operación")
#         return render_template("resultado.html", num1=num1, num2=num2,
#                                operador=operador, resultado=resultado)
#     else:
#         return render_template("calculadora_wtf.jinja2", form=form)


# -------- Subida de Archivos ---------- #

# @app.route('/archivos')
# def archivos():
#     lista = []
#     for file in listdir(app.root_path+"/static/img"):
#         lista.append(file)
#     return render_template("archivos.html", lista=lista)


# @app.route('/subir_imagen', methods=['GET', 'POST'])
# def upload():
#     form = UploadForm()  # carga request.form y request.file
#     if form.validate_on_submit():
#         f = form.photo.data
#         filename = secure_filename(f.filename)
#         f.save(app.root_path + "/static/img/" + filename)
#         return redirect(url_for('archivos'))
#     return render_template('upload_image.html', form=form)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
