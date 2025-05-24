# input
npm = input("Masukkan NPM: ")  
npm_depan = npm[:-2]               # untuk memisahkan 2 digit npm  akhir
dua_digit_terakhir = int(npm[-2:])  

# proses
i = 1
while i <= dua_digit_terakhir:
    npm_baru = npm_depan + f"{i:02d}"
    print(npm_baru)
    i += 1
print("Selesai. Program berhenti di NPM:", npm)
     