from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def pagina_principal():
    #conectando no banco de dados

    conexao = mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "root",
        database = "musictube"
    )

    cursor = conexao.cursor(dictionary=True)



    cursor.execute("SELECT docigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    musicas = cursor.fetchall()

    conexao.close()


    return render_template("principal.html", musicas = musicas)

@app.route("/administracao")
def pagina_admin():
    return render_template("administracao.html")




if __name__ == "__main__":
    app.run(debug=True)



   