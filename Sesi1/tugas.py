import random

welcome_message = "Welcome to Cuypy Games!"
cuypy_position = random.randint(1, 4)

print("=============================")
print(f"== {welcome_message} ==")
print("=============================")

nama_user = input("masukkan nama anda: ")

print(f'''
Hi {nama_user}! Coba perhatikan goa di bawah ini
|_| |_| |_| |_|
''')

pilihan_user = int(input("Menurut anda dimana CUYPY berada? [ 1 / 2 / 3 / 4 ]: "))
konfirmasi_user = input(f"apakah anda sudah yakin pilihan anda {pilihan_user}? [ y / n ]: ")

if konfirmasi_user == "y":
    print(f"pilihan anda adalah {pilihan_user}")
    if pilihan_user == cuypy_position:
        print(f"SELAMAT {nama_user} ANDA BENAR! Posisi CUYPY berada di {cuypy_position} dan pilihan anda adalah goa nomor {pilihan_user} " )
    else:
        print(f"MAAF {nama_user} ANDA SALAH! CUYPY bukan berada di sana, melainkan berad di {cuypy_position}")
else:
    pilihan_user = int(input("Menurut anda dimana CUYPY berada? [ 1 / 2 / 3 / 4 ]: "))
    print(f"pilihan anda adalah {pilihan_user}")
    if pilihan_user == cuypy_position:
        print(f"SELAMAT {nama_user} ANDA BENAR! Posisi CUYPY berada di {cuypy_position} dan pilihan anda adalah goa nomor {pilihan_user} " )
    else:
        print(f"MAAF {nama_user} ANDA SALAH! CUYPY bukan berada di sana, melainkan berad di {cuypy_position}")