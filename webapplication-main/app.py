from flask import Flask, render_template, request, redirect 
from uuid import uuid4
import csv

app = Flask(__name__)

agenda = [ { 'id':uuid4(),'Tarefa':'Caminhar com o cachorro','Status':'Realizada','Horário':"18:40",'Tipo':'Lazer'}]

@app.route('/inicio')
def inicio():
    with open('Tarefas.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out,['id','Tarefa','Status','Horário','Tipo'])
        escritor.writeheader()
        escritor.writerows(agenda)

    with open('Tarefas.csv','rt') as file_in:
        leitor = csv.DictReader(file_in)
    return render_template('index.html',agenda = agenda )
    
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods = ['POST'])
def save():
    tarefa = request.form['Tarefa']
    horario = request.form['Horário']
    tipo = request.form['Tipo']
    agenda.append({'id':uuid4(),'Tarefa':tarefa,'Status':'Não realizada','Horário':horario,'Tipo':tipo})
    return redirect('\inicio')

@app.route('/edit/<id>')
def edit(id):
    for tarefa in agenda:
        if id == str(tarefa['id']):
            return render_template('update.html',tarefa = tarefa)

@app.route('/edit/tarefa/<id>', methods=['POST'])
def salvar_edicao(id):
    for tarefa in agenda:
        if (id == str(tarefa['id'])):
            i = agenda.index(tarefa)
            id_modificado = tarefa['id']
    n_tarefa = request.form['Tarefa']
    n_status = request.form['Status']
    n_horario = request.form['Horário']
    n_tipo = request.form['Tipo']
    agenda[i] = {'id':id_modificado,'Tarefa':n_tarefa,'Status':n_status,'Horário':n_horario,'Tipo':n_tipo}
    return redirect('/inicio')

@app.route('/delete/<id>')
def delete(id):
    for tarefa in agenda:
        if ( id == str(tarefa['id'])):
            i = agenda.index(tarefa)
            del agenda[i]
            return redirect('\inicio')


app.run(debug=True)