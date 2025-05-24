# Input waktu proses di 5 stasiun kerja
waktu_proses = []

print("Masukkan waktu proses untuk 5 stasiun kerja (dalam detik):")
for i in range(5):
    waktu = int(input(f"Stasiun {i+1}: "))
    waktu_proses.append(waktu)

# Hitung waktu siklus (cycle time)
waktu_siklus = max(waktu_proses)
print(f"\nWaktu siklus: {waktu_siklus} detik\n")

# Analisis setiap stasiun
for i in range(5):
    waktu = waktu_proses[i]
    if waktu == waktu_siklus:
        status = "Bottleneck"
    elif waktu > 35:
        status = "Perlu improvement"
    else:
        status = "Optimal"
    
    print(f"Stasiun {i+1} | Waktu: {waktu} detik → {status}")
