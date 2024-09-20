def loginUsuario (perfil):
    if perfil.lower() == "admin":
        print("Bem vindo, administrador")
    else:
        print("Bem vindo, usuario")

perfil = str(input("Digite seu login:"))

loginUsuario (perfil)