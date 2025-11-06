pwsistem = "Latihan"
kesempatan = 3

print("=== Sistem Login Admin ===")

for percobaan in range(kesempatan):
    
    print("Username: Daspro2023")
    password_input = input("Password: ")

    if password_input == pwsistem:
        print("\nLogin berhasil! Selamat datang di sistem.")
        break

    else:
        sisa = kesempatan - (percobaan + 1)
        if sisa > 0:
            print(f"Password salah! Kesempatan tersisa: {sisa}\n")
        else:
            print("\nAnda telah gagal 3 kali. Akses ditolak!")
