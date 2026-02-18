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
def ordi_premier2(nombre):
    res=""
    nombre_identifie = nombre
    diviseur = 1
    f = 0
    diviseur2 = 1
    clone_nombre_identifie = nombre_identifie
    while True:
        diviseur2 = 1
        clone_nombre_identifie = nombre_identifie
        diviseur += 1
        if diviseur > nombre_identifie ** 0.5:
            break

        if nombre_identifie % diviseur == 0:
            f = 1
            while True:
                diviseur2 += 1
                while int(clone_nombre_identifie) % diviseur2 == 0:
                    if diviseur2 == clone_nombre_identifie:
                        break
                    print(diviseur2, end=" * ")
                    res = res + str(diviseur2) + " * "

                    clone_nombre_identifie = int(clone_nombre_identifie / diviseur2)
                if diviseur2 > nombre_identifie / diviseur ** 0.5:
                    print(int(clone_nombre_identifie), end=" = ")
                    res += str(clone_nombre_identifie) + " = " + str(nombre_identifie) + "; "
                    print(nombre_identifie)
                    break

            break
    print()
    if f == 0:
        res += str(nombre_identifie) + " est premier."
    else:
        res += str(nombre_identifie) + " n'est pas premier."
    return res

