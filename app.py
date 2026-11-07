from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para simular os chamados de assistência técnica
chamados = [
    {"id": 1, "cliente": "Carlos Silva", "equipamento": "Notebook Dell", "defeito": "Não liga / Tela preta"},
    {"id": 2, "cliente": "Mariana Souza", "equipamento": "Desktop Gamer", "defeito": " Lentidão e travamentos"}
]

@app.route('/')
def index():
    return render_template('index.html', chamados=chamados)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    cliente = request.form.get('cliente')
    equipamento = request.form.get('equipamento')
    defeito = request.form.get('defeito')
    
    if cliente and equipamento and defeito:
        novo_id = len(chamados) + 1
        chamados.append({
            "id": novo_id,
            "cliente": cliente,
            "equipamento": equipamento,
            "defeito": defeito
        })
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)