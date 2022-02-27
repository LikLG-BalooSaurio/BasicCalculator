from os import system
from colorama import Fore

opcion = 0

print(Fore.GREEN + """

█▀ █ █▀▄▀█ █▀█ █░░ █▀▀
▄█ █ █░▀░█ █▀▀ █▄▄ ██▄
""")

print(Fore.LIGHTGREEN_EX + """
        █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
        █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄
""")

print(Fore.RED + """
                            ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                            ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                            ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█

| | | | | | | | | | | | | | | | | |
v v v v v v v v v v v v v v v v v v 
""")

n1 = int(input(Fore.CYAN + "Coloca el primer numero: "))

n2 = int(input(Fore.CYAN + "Coloca el segundo numero: "))

print(Fore.GREEN + """
            Que es lo que quieres hacer?
    1) Sumar
    2) Restar
    3) Multiplicar
    4) Dividir
    5) Salir
""")

opcion = int(input(Fore.CYAN + "    Opcion: "))
print("""

""")

if opcion == 1:
    print(Fore.LIGHTGREEN_EX + "El resultado es: ", Fore.RED, n1 + n2)
    print("""

    
    """)

elif opcion == 2:
    print(Fore.LIGHTGREEN_EX + "El resultado es: ", Fore.RED, n1 - n2)
    print("""

    
    """)

elif opcion == 3:
    print(Fore.LIGHTGREEN_EX + "El resultado es: ", Fore.RED, n1 * n2)
    print("""

    
    """)

elif opcion ==4:
    print(Fore.LIGHTGREEN_EX + "El resultado es: ", Fore.RED, n1 / n2)
    print("""

    
    """)

elif opcion == 5:
    print("""

    
    """)
    exit()