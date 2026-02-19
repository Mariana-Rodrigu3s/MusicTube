from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas
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
        database = "MusicTube"
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




if __name__ == "__main__":
    app.run(debug=True)



   