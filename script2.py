def fonction_appel_ia(nombre):
    if int(nombre)==int(nombre):
        return("true")
    else:
        return("false")

def ordi_premier(nombre):
    nombre_identifie = nombre
    nombre1 = 1
    while True:
        nombre1 += 1
        if nombre1 > nombre_identifie ** 0.5:
            return(f"{nombre_identifie} est premier")

        if nombre_identifie % nombre1 == 0:
            return(f"{nombre_identifie} n'est pas premier")