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
if pilihan_user == cuypy_position:
    print(f"Selamat {nama_user} pilihan anda benar! CUYPY berada di nomor {cuypy_position}")
else:
    print(f"Maaf {nama_user} Pilihan Anda Salah. CUYPY berada di nomor {cuypy_position}")