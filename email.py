# Obtener correo
email = input("Cual es tu correo electronico?: ").strip()

# Nombre de usuario
user_name = email[:email.index("@")]

# Dominio
domain_name = email[email.index("@")+1:]

# formato del mensaje ouyea
output = "Tu nombre de usuario es: '{}' y el dominio es: '{}'".format(user_name,domain_name)
print(output)