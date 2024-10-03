"""
Membuat Daftar Penumpang

Tugasmu adalah membuat program yang akan mengonversi data penumpang dari input yang diberikan menjadi list of dictionaries. 
Setiap penumpang memiliki tiga atribut: nama, umur, dan asal planet. 
Program harus meminta input untuk setiap atribut penumpang dan menyimpannya dalam dictionary, lalu memasukkan dictionary tersebut ke dalam list.

Contoh
Input:
Jumlah penumpang: 2

Penumpang 1
Nama: Hanif
Umur: 23
Asal planet: Mars

Penumpang 2
Nama: Rani
Umur: 25
Asal planet: Jupiter

Output:
[
    {'nama': 'Hanif', 'umur': 23, 'asal planet': 'Mars'},
    {'nama': 'Rani', 'umur': 25, 'asal planet': 'Jupiter'}
]
"""
penumpang = []
jumlah_penumpang = int(input("Jumlah penumpang: "))

for i in range(jumlah_penumpang):
    nama = input(f"Penumpang {i+1}\nNama: ")
    umur = int(input("Umur: "))
    asal_planet = input("Asal planet: ")
    
    print()
    
    # lanjutkan code dibawah ini
    penumpang_dict = {
        'nama': nama,
        'umur': umur,
        'asal planet': asal_planet}
    penumpang.append(penumpang_dict)

    print(penumpang)

