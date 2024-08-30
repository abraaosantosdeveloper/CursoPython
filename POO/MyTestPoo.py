class Usuario:
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __str__(self):
        return f"Nome: {self.nome}\nEmail: {self.email}\nSenha: {self.senha}"

def show_users(*objects):
    for user in objects:
        print(user)
    


nome_usuario = input("Digite seu nome completo: ")
email_usuario = input("Digite seu email: ")
senha_usuario = input("Digite sua senha: ")


user_1 = Usuario(nome_usuario, email_usuario, senha_usuario)
show_users(user_1)
