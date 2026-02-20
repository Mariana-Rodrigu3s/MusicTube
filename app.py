from flask import Flask, redirect, render_template, request
import mysql.connector
from model.musica import adicionar_musica, recuperar_musicas
from model.genero import recuperar_genero
from 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pagina_principal():
    #conectando no banco de dados

    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "LunaWave"
    )

    cursor = conexao.cursor(dictionary=True)



    

    generos = recuperar_genero()
         
    musicas = recuperar_musicas()


    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/administracao")
def pagina_admin():
    musicas = recuperar_musicas()
    generos = recuperar_genero()
    return render_template("administracao.html", musicas = musicas, generos = generos)


@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():
    nome_musica = request.form.get("inpute")
    cantor =
    duracao =
    genero =

    if adicionar_musica(cantor, nome, musica):
        return redirect("/administracao")
    else:
        return "Erro ao adicionar música"


if __name__ == "__main__":
    app.run(debug=True)



   