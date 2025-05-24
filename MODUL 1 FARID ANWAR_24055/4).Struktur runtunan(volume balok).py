# deklarasi variable
volume_balok = {
  "panjang": float(input("panjang :")),
  "lebar": float(input("lebar :")),
  "tinggi": float(input("tinggi :"))
}

#perhiitungan balok
volume = volume_balok["panjang"] * volume_balok["lebar"] * volume_balok["tinggi"]
 
#output
print("volume_balok", volume)