import customtkinter
import sqlite3
import BancoDados
import tkinter
from functools import partial


# Tela de Cadastro
def tela_Cadastro():
    cadastro_tela = customtkinter.CTkToplevel()
    # ENTRADAS CADASTRO
    texto_cadastro = customtkinter.CTkLabel(master=cadastro_tela,text="CADASTRE UM NOVO USUÁRIO")
    texto_cadastro.pack(padx=0, pady=0)
    
    user_cadastro = customtkinter.CTkEntry(master=cadastro_tela, placeholder_text="Novo Usuário")
    user_cadastro.pack(padx=0, pady=10)
    
    password_cadastro = customtkinter.CTkEntry(master=cadastro_tela, placeholder_text="Nova Senha", show="*")
    password_cadastro.pack(padx=0, pady=10)
    
    def funcBtnCadastro():
        try:
            BancoDados.cadastrar_usuarios(user_cadastro, password_cadastro)
            tkinter.messagebox.showinfo(title="Aviso", message="Cadastro efetuado com sucesso!")
        except:
            tkinter.messagebox.showinfo(title="Aviso", message="Seu cadastro não foi efetuado, tente novamente.")
        cadastro_tela.destroy()

    botao_Cadastrar = customtkinter.CTkButton(master=cadastro_tela, text="CADASTRAR", command= funcBtnCadastro)
    botao_Cadastrar.pack(padx=0, pady=10)

    # Propriedades da Tela de Cadastro
    cadastro_tela.title("Tela de Cadastro")
    cadastro_tela.geometry("400x225")
    cadastro_tela.resizable(width=False, height=False)
    cadastro_tela.attributes("-topmost", True)


# Iniciando o banco de dados
banco = sqlite3.connect("Tela Login v1/users.db")
root = banco.cursor()
root.execute("CREATE TABLE IF NOT EXISTS usuarios (id_user integer primary key autoincrement, nome text unique, senha text)")

# Conteúdo da Janela
janela = customtkinter.CTk()

texto = customtkinter.CTkLabel(janela,text="FAÇA SEU LOGIN")
texto.pack(padx=0, pady=0)

# ENTRADAS LOGIN
user = customtkinter.CTkEntry(janela, placeholder_text="Usuário")
user.pack(padx=0, pady=10)
password = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
password.pack(padx=0, pady=10)

# Botões da Janela
def btnLogin(usuario, senha):
    try:
        if BancoDados.login(usuario, senha) == True:
            tkinter.messagebox.showinfo(title="Aviso", message="Login efetuado com sucesso!")
        elif BancoDados.login(usuario, senha) == False:
            tkinter.messagebox.showinfo(title="Aviso", message="Senha incorreta, tente novamente.")
        else:
            tkinter.messagebox.showinfo(title="Aviso", message="Seu login não foi efetuado, tente novamente.")
    except IndexError:
        tkinter.messagebox.showinfo(title="Aviso", message="Usuário incorreto, tente novamente.")
    except:
        tkinter.messagebox.showinfo(title="Aviso", message="Houve um erro com seu login, tente novamente.")

botao_Login = customtkinter.CTkButton(
    janela, text="LOGIN", 
    #command=partial(BancoDados.login, usuario=user, senha=password))
    command= partial(btnLogin, usuario=user, senha=password)).pack(padx=0, pady=10)

botao_tela_Cadastrar = customtkinter.CTkButton(janela, text="CADASTRAR",command=tela_Cadastro).pack(padx=0, pady=10)

# Propriedades da janela
janela.title("Sistema")
janela.geometry("400x225")
janela.resizable(width=False, height=False)
janela._set_appearance_mode("dark")
janela.mainloop()