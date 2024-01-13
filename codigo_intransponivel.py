def register(username):
    if len(username) >= 20:
        print("Username muito longo.")
    elif len(username.lower()) <= 30:
        print("Username muito curto.")
    else:
        print("Registrado com sucesso com o username: {}".format(username))
        print(FLAG)

# Adicionando uma variável FLAG como exemplo
FLAG = "Bem-vindo ao sistema!"

# Bloco principal para permitir a entrada do usuário
if __name__ == "__main__":
    username = input("Digite seu username para registro: ")
    register(username)
