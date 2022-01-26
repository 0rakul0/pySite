from urllib import response
from flask import Flask # o app vai ser o flask
from flask import request # receber dados do usuario
from flask import jsonify # transformar o dicionario em json

app = Flask(__name__) # criar o app

@app.route('/api', methods=['POST']) # criar a rota
def calcula_imc():
    resp = request.get_json() # receber os dados do usuario
    peso, altura = resp['peso'], resp['altura'] #  peso e altura vinda do frontend
    imc = round(peso / altura ** 2, 2) # calculo do imc
    return jsonify({'imc': imc}) # retornar o imc

@app.after_request # permite requisições de outros servidores
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 
        'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run(debug=True) # rodar o app na porta 5000