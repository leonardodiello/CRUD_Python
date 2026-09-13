from flask import Flask, render_template, request, redirect, url_for
from conexao import conectar

app = Flask(__name__)


@app.route('/')
def index():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM vendas')
    vendas = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('index.html', vendas=vendas)


@app.route('/create', methods=['POST'])
def create():
    nome_produto = request.form['nome_produto']
    valor = request.form['valor']

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)',
        (nome_produto, valor)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    valor = request.form['valor']

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        'UPDATE vendas SET valor = %s WHERE id = %s',
        (valor, id)
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM vendas WHERE id = %s', (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)