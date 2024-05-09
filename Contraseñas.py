import random

def generar_contraseña (longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_-+=[]¨{}|:,.;?"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

longitud = int(input("Ingresa la longitud que quieras para la contraseña: "))
contraseña = generar_contraseña(longitud)
print("La contraseña generada es: ", contraseña)