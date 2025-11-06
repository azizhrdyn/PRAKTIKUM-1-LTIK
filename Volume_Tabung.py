"=== KALKULASI VOLUME TABUNG ==="

def vtabung(radius, tinggi):
    volume = int((22/7) * (radius ** 2) * (tinggi))
    return volume

print("=== Kalkulasi Volume Tabung ===")
radius = int(input("Masukkan radius tabung (cm): "))
tinggi = int(input("Masukkan tinggi tabung (cm): "))
print(f"Volume tabung dengan radius {radius} cm dan tinggi {tinggi} cm adalah: {vtabung(radius, tinggi):.2f} cm³")
