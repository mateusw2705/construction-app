from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Conexão com o banco de dados SQLite
def db_connection():
    conn = sqlite3.connect('construcao.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criação da tabela de projetos
def create_tables():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area REAL,
            custo REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materiais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            projeto_id INTEGER,
            nome TEXT NOT NULL,
            quantidade INTEGER,
            preco_unitario REAL,
            FOREIGN KEY(projeto_id) REFERENCES projetos(id)
        )
    """)
    conn.commit()
    conn.close()

# Endpoint para registrar um projeto
@app.route('/projetos', methods=['POST'])
def criar_projeto():
    data = request.get_json()
    nome = data['nome']
    area = data['area']
    custo = data['custo']

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO projetos (nome, area, custo)
        VALUES (?, ?, ?)
    """, (nome, area, custo))
    conn.commit()
    conn.close()

    return jsonify({"message": "Projeto criado com sucesso!"}), 201

# Endpoint para listar projetos
@app.route('/projetos', methods=['GET'])
def listar_projetos():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projetos")
    rows = cursor.fetchall()

    projetos = [dict(row) for row in rows]
    return jsonify(projetos)

# Endpoint para adicionar materiais a um projeto
@app.route('/projetos/<int:projeto_id>/materiais', methods=['POST'])
def adicionar_materiais(projeto_id):
    data = request.get_json()
    nome = data['nome']
    quantidade = data['quantidade']
    preco_unitario = data['preco_unitario']

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO materiais (projeto_id, nome, quantidade, preco_unitario)
        VALUES (?, ?, ?, ?)
    """, (projeto_id, nome, quantidade, preco_unitario))
    conn.commit()
    conn.close()

    return jsonify({"message": "Material adicionado com sucesso!"}), 201

# Endpoint para listar materiais de um projeto
@app.route('/projetos/<int:projeto_id>/materiais', methods=['GET'])
def listar_materiais(projeto_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM materiais WHERE projeto_id = ?", (projeto_id,))
    rows = cursor.fetchall()

    materiais = [dict(row) for row in rows]
    return jsonify(materiais)
# Endpoint para cálculo da área e custo
@app.route('/calculo', methods=['POST'])
def calculo():
    data = request.get_json()
    altura = data['altura']
    largura = data['largura']
    preco_por_metro = data['preco_por_metro']

    # Cálculo da área e custo
    area = altura * largura
    custo = area * preco_por_metro

    return jsonify({
        "area": area,
        "custo": custo
    })

if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
