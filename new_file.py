from flask import Flask, render_template, jsonify, request, redirect

from peewee import *

app = Flask(__name__)

db = PostgresqlDatabase("flask_test")

class Todo(Model):
	task = CharField(null=False)
	completion = BooleanField(null=False, default=False)

	class Meta:
		database = db

db.create_tables([Todo])

@app.route("/")
def home():
	todos = Todo.select()
	return render_template("index.html", todos=todos)

@app.route("/todo/new")
def new():
	return render_template("form.html")

@app.route("/todo/create", methods=["POST"])
def create():
	task = request.form.get('task')
	todo = Todo(task=task)
	todo.save()
	return redirect("/")

app.run()



