from database.conexao import conectar

def autenticar_usuario(usuario:str, senha:str):
    


    try:
        conexao, cursor = conectar()

        cursor.execute("""
                SELECT * FROM cadastro WHERE login = %s AND senha = %s

""")
        

    
