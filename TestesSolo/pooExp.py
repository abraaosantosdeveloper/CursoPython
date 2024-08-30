# Simple User Information with class and object

# class User:
#     def __init__(self, name, email, password):

#         self.name = name
#         self.email = email 
#         self.password = password
        

# username = input("Enter your name: ")

# user_email = input("Enter your email: ")

# user_password = input("Enter your password: ")

# user1 = User(username, user_email, user_password)

# print(f'''
#     Name: {user1.name}
#     Email: {user1.email}
#     Password: {user1.password}
    
#     ''')


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

nomeUsuario = input("Digite seu nome: ")

emailUsuario = input("Digite seu email: ")

senhaUsuario = input("Digite sua senha: ")

usuario1 = Usuario(nomeUsuario, emailUsuario, senhaUsuario)

print(f"""
    Nome: {usuario1.nome}
    Email: {usuario1.email}
    Senha: {usuario1.senha}
""")