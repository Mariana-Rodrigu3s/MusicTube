from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pagina_principal():
    #conectando no banco de dados

    conexao = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "musictube"
    )

    cursor = conexao.cursor(dictionary=True)



    

    cursor.execute("SELECT nome, icone, cor FROM genero;")

    generos = cursor.fetchall()

    conexao.close()

    musicas = recuperar_musicas()


    return render_template("principal.html", musicas = musicas, generos = generos)

@app.route("/administracao")
def pagina_admin():
    return render_template("administracao.html")




if __name__ == "__main__":
    app.run(debug=True)



   