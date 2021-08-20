import sqlite3
from flask import Flask, request, session, g, redirect, \
    abort, render_template, flash

# configuração
DATABASE = "blog.db"
SECRET_KEY = "quimdim"

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_requisicao(exc):
    g.bd.close()

@app.route('/')
@app.route('/entradas')
def exibir_entradas():
    return render_template('exibir_entradas.html')

@app.route('/hello')
def pagina_incial():
    return 'Hello World!'