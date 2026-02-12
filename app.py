from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/administracao")
def pagina_admin():
    return render_template("administracao.html")


if __name__ == "__main__":
    app.run(debug=True)