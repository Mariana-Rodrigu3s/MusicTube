from database.conexao import conectar

def recuperar_musicas(ativos:bool=False):
    conexao, cursor = conectar()

    if ativos == False:
        cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica;")
    
    else:
        cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica WHERE ativo = 1;")
    musicas = cursor.fetchall()

    conexao.close()

    return musicas


def adicionar_musica(cantor:str, nome_musica:str, duracao:str, imagem_url:str, genero:str) -> bool:
    """
    Essa função é para facilitar a aplicação as musicas para o usuário 
    """
    try:
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

        return True
    
    except Exception as e:
        print(e)
        return False
    



def excluir_musica(codigo):

    try:

        conexao, cursor = conectar()

        cursor.execute( """
                    DELETE FROM musica WHERE codigo= %s
                
                    
    """,
    [codigo])



        conexao.commit()

        conexao.close()

        return True
    
    except:
        return False
    


def atualizar_status(ativo, codigo):

    try:

        conexao, cursor = conectar()

        cursor.execute("""

                    UPDATE musica 
                    SET ativo = %s
                    WHERE codigo = %s

""",
[ativo, codigo])
        
        return True
    
    except:
        return True

