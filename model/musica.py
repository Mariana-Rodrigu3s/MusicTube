from database.conexao import conectar

def recuperar_musicas():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    musicas = cursor.fetchall()

    conexao.close()

    return musicas


def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem_url:str, genero:str) -> bool:
    """
    Essa função é para facilitar a aplicação as musicas para o usuário 
    """

    conexao, cursor = conectar()

    cursor.execute("""
                        INSERT INTO musica
                   (cantor, nome, duracao, url_imagem, nome_genero)
                   VALUES
                   (%s, %s, %s, %s, %s)
""",
[cantor, nome_musica, duracao, imagem_url, genero]
)
    
    conexao.commit()

    conexao.close()
