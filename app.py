from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cronograma')
def cronograma():
    return render_template('cronograma.html')


@app.route('/modulos_ia')
def modulos_ia():
    return render_template('modulos_ia.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
