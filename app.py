from flask import Flask, redirect, render_template, request
import mysql.connector
from model.musica import adicionar_musica, atualizar_status, recuperar_musicas, excluir_musica
from model.genero import recuperar_genero

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
    nome_musica = request.form.get("musica")
    cantor = request.form.get("cantor")
    duracao = request.form.get("duracao")
    genero = request.form.get("nome_genero")
    imagem = request.form.get("imagem_url")

    if adicionar_musica(cantor, duracao, nome_musica, genero, imagem):
        return redirect("/administracao")
    else:
        return "Erro ao adicionar música"
    

@app.route("/musica/delete/<codigo>", methods=["GET"])
def deletar_musica(codigo):
    excluir_musica(codigo)
    return redirect("/administracao")

@app.route("/musica/atualizar/<codigo>/<ativo>")
def ativo_musica(codigo, ativo):
    atualizar_status(codigo, ativo)
    return redirect("/administracao")



if __name__ == "__main__":
    app.run(debug=True)



   