from script2 import ordi_premier2


def test_ordre_premier():
    test_cases = [
        (0, "0 n'est pas premier."),
        (1, "1 n'est pas premier."),
        (2, "2 est premier."),
        (7, "7 est premier."),
        (10, "10 n'est pas premier."),
        (1801, "1801 est premier."),
        (1802, "1802 n'est pas premier."),
        (1583, "1583 est premier."),
    ]

    for nombre, expected in test_cases:
        result = ordi_premier2(nombre)
        if result == expected:
            print(f"======= Test avec {nombre} OK")
        else:
            print(f"!!!!!!!! Test avec {nombre} NOK")


test_ordre_premier()
