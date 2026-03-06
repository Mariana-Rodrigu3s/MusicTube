from database.conexao import conectar

def autenticar_usuario(usuario:str, senha:str) -> list:
    


        conexao, cursor = conectar()

        cursor.execute("""
                SELECT usuario, senha FROM cadastro WHERE usuario = %s AND senha = %s

        """, [usuario, senha])
        
        usuario = cursor.fetchone()

        conexao.commit()
        conexao.close()


        return usuario
        

    
