sisi = int(input("Masukkan sisi persegi:"))
pilih = input("pilih luas/keliling:")
pilihan = {"luas": sisi*sisi, "keliling": 4*sisi}
print(pilihan[pilih])