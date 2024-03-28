from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "ola!"


@app.route('/user/Usuário')
def index2():
    a = '<h1>óla, programador!</h1>'
    l = '<p><a href="/user/">clique aqui</a></p>'
    return a + l

@app.route('/user/')
def index3():
    return "Olá usuário"

@app.route('/user/nome_usuario')
def index4():
    return "ola, nome_usuario!"
if __name__=='__main__':
    app.run()

