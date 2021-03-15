from flask import Flask, request

from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Person:
    name: str
    age: int = 16

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}'

@app.route('/hello', methods=["GET"])
def hello_get():
    name = request.args["name"]
    return f'Hello, {name}'

@app.route('/hello', methods=["POST"])
def hello_post():
    # name = request.json["name"]
    # person = Person(
    #     name=request.json.get("name"),
    #     age=request.json.get("age")
    # )
    person = Person.from_dict(request.json)
    print(person)
    # return f'Hello, {person.name}'
    return person.to_dict()
