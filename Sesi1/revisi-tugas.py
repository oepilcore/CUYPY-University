import random

def get_user_input():
    return int(input("Menurut anda dimana CUYPY berada? [ 1 / 2 / 3 / 4 ]: "))

def confirm_choice(pilihan_user):
    return input(f"apakah anda sudah yakin pilihan anda {pilihan_user}? [ y / n ]: ")

welcome_message = "Welcome to Cuypy Games!"
cuypy_position = random.randint(1, 4)

print("=" * 29)
print(f"== {welcome_message} ==")
print("=" * 29)

nama_user = input("masukkan nama anda: ")

print(f'''
Hi {nama_user}! Coba perhatikan goa di bawah ini
|_| |_| |_| |_|
''')

pilihan_user = get_user_input()
konfirmasi_user = confirm_choice(pilihan_user)

if konfirmasi_user == "n":
    pilihan_user = get_user_input()

print(f"pilihan anda adalah {pilihan_user}")

if pilihan_user == cuypy_position:
    print(f"SELAMAT {nama_user} ANDA BENAR! Posisi CUYPY berada di {cuypy_position} dan pilihan anda adalah goa nomor {pilihan_user} " )
else:
    print(f"MAAF {nama_user} ANDA SALAH! CUYPY bukan berada di sana, melainkan berad di {cuypy_position}")
