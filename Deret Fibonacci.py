"=== KALKULASI DERET FIBONACCI ==="

def fibonacci(suku):
    deret = [0, 1]
    for x in range(2, suku):
        deret.append(deret[x - 1] + deret[x - 2])
    return deret

print("=== Kalkulasi Deret Fibonacci ===")
suku = int(input("Masukkan jumlah suku pada deret: "))
print(f"Deret fibonacci sebanyak {suku} suku: {fibonacci(suku)}")
