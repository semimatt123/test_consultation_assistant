
def num_pre(choix_utilisateur):
    nombre_identifie=2
    nombre1=1
    liste_nombre_premier=list()
    f=0
    g=0
    different=0
    different_plus_grande=0
    while len(liste_nombre_premier)!=choix_utilisateur:
        b=0
        different+=1
        verificateur=1
        f=len(liste_nombre_premier)
        while f!=0:
            b+=1
            c=liste_nombre_premier[b-1]
            f-=1
            if c*c>nombre_identifie:
                f=0 # alors c'est un nombre premier
            if nombre_identifie/c==round(nombre_identifie/c):
                verificateur=0
                f=0 # alors c'est un nombre divisable par c
        if verificateur==1:
            if different > different_plus_grande:
                different_plus_grande=different
                nombre1=nombre_identifie
            print(f"{nombre_identifie} est un nombre premier, {different} est la différence actuelle de {nombre_identifie} et de {nombre_identifie-different}.")
            print(f"{different_plus_grande} a la différence la plus grande avec {nombre1} et {nombre1-different_plus_grande}")
            liste_nombre_premier.append(nombre_identifie)
            different = 0

        nombre_identifie+=1
    print(liste_nombre_premier)
    return liste_nombre_premier