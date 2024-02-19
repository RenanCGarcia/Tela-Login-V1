import sqlite3


banco = sqlite3.connect("Tela Login v1/users.db")
root = banco.cursor()
root.execute("CREATE TABLE IF NOT EXISTS usuarios (id_user integer primary key autoincrement, nome text unique, senha text)")

def login(usuario, senha):
    root = banco.cursor()
    root.execute("SELECT id_user, nome, senha FROM usuarios WHERE nome = '"+usuario.get()+"'")
    id = root.fetchall()[0]
    
    if (id[1] == usuario.get()) and (id[2] == senha.get()):
        return True
    elif id[2] != senha.get():
        return False

def editar_banco(parametro):
    root.execute(parametro)
    banco.commit()

def editar_banco(parametro):
    root = banco.cursor()
    root.execute(parametro)
    banco.commit()

def cadastrar_usuarios(usuario, senha):
    root = banco.cursor()
    
    root.execute("INSERT INTO usuarios (nome, senha) VALUES ('"+usuario.get()+"', '"+senha.get()+"')")
    banco.commit()

def mudar_senha(usuario, senha_nova):
    root = banco.cursor()
    root.execute("UPDATE usuarios SET senha = '"+senha_nova+"' WHERE nome = '"+usuario+"'")
    banco.commit()

def remover_usuario(usuario):
    root = banco.cursor()
    root.execute("DELETE FROM usuarios WHERE nome = '"+usuario+"'")
    banco.commit()