#Essas 2 linhas debaixo são obrigatórias para importar o Flask e o app funcionar 
from flask import Flask
app = Flask(__name__)
#só para importar as rotas vindas de outro arquivo .py
from rotas import *
#Não sei o pq mas sem esse if o app não funciona direito
#se botar o app.run(debug=true) pode editar o site com o codigo rodando
if __name__ == "__main__":
    app.run(debug=True)
    