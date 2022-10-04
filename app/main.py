from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("formulario.html")

@app.route("/cv1")
def curr():
    return render_template("curriculum.html")

@app.route("/cv", methods=["POST"])
def hello():
    name = request.form.get("name")
    fechaSN = request.form.get("fechaSN")
    ocupacion = request.form.get("ocupacion")
    contacto = request.form.get("contacto")
    nacionalidad = request.form.get("nacionalidad")
    nivelIngl = request.form.get("nivelIngl")
    lengProg = request.form.get("lengProg")
    aptitud = request.form.get("aptitud")
    habilidad = request.form.get("habilidad")
    perfil = request.form.get("perfil")

    return render_template("curriculum.html", name=name,fechaSN = fechaSN, ocupacion = ocupacion,
     contacto=contacto,nacionalidad = nacionalidad, nivelIngl = nivelIngl, lengProg = lengProg,
     aptitud = aptitud,habilidad = habilidad, perfil = perfil )

if __name__ == '__main__':
    app.run(debug=True,port=5000)