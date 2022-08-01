from flask import Flask, request
import operations

app = Flask(__name__)

OPS = {
    'add': operations.add,
    'sub': operations.sub,
    'mult': operations.mult,
    'div': operations.div
}


@app.route('/math/<operator>')
def handle(operator):

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(OPS[operator](a, b))


# completed further study before actual assignment... sigh
@app.route('/add')
def add():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(OPS['add'](a, b))


@app.route('/sub')
def sub():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(OPS['sub'](a, b))


@app.route('/mult')
def mult():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(OPS['mult'](a, b))


@app.route('/div')
def div():

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(OPS['div'](a, b))
