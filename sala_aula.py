from flask import Flask, jsonify, request, render_template
from alunos_api import alunos_app
from professores_api import professores_app
from disciplinas_api import disciplinas_app
import requests as Req
import infra.alunos_db as alunos_db
import infra.professores_db as professores_db
import infra.disciplina_db as disciplinas_db

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)
app.register_blueprint(disciplinas_app)

@app.route('/')
def all():
    alunos = Req.get("http://localhost:5000/alunos").json()
    professores = Req.get("http://localhost:5000/professores").json()
    disciplinas = Req.get("http://localhost:5000/disciplinas").json()
    return render_template("index.html", alunos=alunos, professores=professores, disciplina=disciplinas)


alunos_db.init()
professores_db.init()
disciplinas_db.init()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
