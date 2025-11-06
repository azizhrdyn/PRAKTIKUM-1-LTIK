"=== KALKULASI TOTAL DAN RATA-RATA ==="

def sumavg(*args):
    jumlah = sum(args)
    mean = jumlah / len(args)
    return jumlah, mean

print("=== Kalkulasi Total Dengan Return ===")
coef = input("Masukkan angka yang ingin dikalkulasi (pisahkan dengan spasi): ")
listcoef = [int(i) for i in coef.split()]
jumlah, mean = sumavg(*listcoef)
print(jumlah)
print(mean)
