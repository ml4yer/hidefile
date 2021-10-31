import os

command = "z"

while True:
    while command.upper() not in ["H", "S", "Q"]:
        command = input("Ne yapmak istiyorsun?(H:Gizle, S:Göster, Q:Çıkış)")

    if command.upper() == "Q":
        break

    filename = input("Dosya adı:")

    if command.upper() == "H":
        os.system(f"attrib +h {filename}")
    elif command.upper() == "S":
        os.system(f"attrib -h {filename}")
    command = "z"
