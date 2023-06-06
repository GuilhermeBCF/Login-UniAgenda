while True:
    print("1 - Login")
    print("2 - Cadastrar")
    print("3 - Esqueci minha senha")
    print("0 - Sair")
    print()
    quest = int(input("Digite a opção desejada: "))

    if quest == 0:
        break
    elif quest > 3:
        print("#### OPÇÃO INVÁLIDA ! ####")
        print()
    else:
        if quest == 2:
            print("--------CADASTRO--------")
            login = input("Informe seu usuário: ").lower()

            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if login in linha:
                        print("Usuário já cadastrado")
                        break
                else:
                    senha = input("Informe sua senha: ")
                    confirmacao = input("Confirme sua senha: ")

                    while confirmacao != senha:
                        print("#### SENHAS NÃO CONFEREM ####")
                        print()
                        senha = input("Informe sua senha: ")
                        confirmacao = input("Confirme sua senha: ")

                    usuario = (login, senha)

                    with open("usuarios.txt", "r") as arquivo:
                        usuarios = arquivo.readlines()

                    usuarios.append(f"{str(usuario)},\n")

                    with open("usuarios.txt", "w") as arquivo:
                        arquivo.writelines(usuarios)

                    user = login

        elif quest == 3:
            login = input("Informe seu usuário: ")

            encontrado = False
            usuarios = []

            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if login in linha:
                        encontrado = True
                        nova_senha = input("Informe uma nova senha: ")
                        conf_nova_senha = input("Confirme sua senha: ")

                        while conf_nova_senha != nova_senha:
                            print("#### SENHAS NÃO CONFEREM ####")
                            print()
                            nova_senha = input("Informe uma nova senha: ")
                            conf_nova_senha = input("Confirme sua senha: ")

                        usuario = linha.replace(linha.split(',')[1], f" '{nova_senha}')")
                        usuarios.append(usuario)
                    else:
                        usuarios.append(linha)

            if encontrado:
                with open("usuarios.txt", "w") as arquivo:
                    arquivo.writelines(usuarios)

                print("¨¨¨¨ Senha alterada com sucesso! ¨¨¨¨   ")

            else:
                print("Usuário não encontrado!")
                print()

        else:
            login = input("Informe seu usuário: ")
            senha = input("Informe sua senha: ")

            encontrado = False

            with open("usuarios.txt", "r") as arquivo:
                for linha in arquivo:
                    if login in linha and senha in linha:
                        encontrado = True
                        break

            if encontrado:
                print("Bem vindo ao APP")
                break
            else:
                print("Login ou senha incorretos!")
                print()