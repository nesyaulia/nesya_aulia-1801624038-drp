user = input("Siapa nama Anda? ")

print(f"\n1. PAPAN CATUR INPUT AKTIVITAS {user}")

for baris in range(8):
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬛", end=" ")
        else:
            print("⬜", end=" ")
    print()

print(f"\n2. DAFTAR AKTIVITAS {user}")

# List kosong
daftar_aktivitas = []

# Input jumlah aktivitas
jumlah_aktivitas = int(input("Berapa banyak aktivitas yang ingin Anda tambahkan? "))

for i in range(jumlah_aktivitas):

    print(f"\nAktivitas ke-{i+1}")

    nama_aktivitas = input("Nama aktivitas: ")
    durasi = input("Durasi aktivitas (jam): ")
    prioritas = input("Prioritas aktivitas (Tinggi/Sedang/Rendah): ")
    emoji = input("Emoji aktivitas favorit: ")

    aktivitas = {
        "nama": nama_aktivitas,
        "durasi": durasi,
        "prioritas": prioritas,
        "emoji": emoji
    }

    daftar_aktivitas.append(aktivitas)

print("\n" + "=" * 50)
print(f"🌸 DAFTAR AKTIVITAS {user} 🌸")
print("=" * 50)

total_durasi = 0

for i in range(len(daftar_aktivitas)):

    print(f"\nAKTIVITAS {i+1}")
    print(f"Nama Aktivitas : {daftar_aktivitas[i]['nama']}")
    print(f"Durasi         : {daftar_aktivitas[i]['durasi']} jam")
    print(f"Prioritas      : {daftar_aktivitas[i]['prioritas']}")
    print(f"Emoji Favorit  : {daftar_aktivitas[i]['emoji']}")

    total_durasi += int(daftar_aktivitas[i]['durasi'])

print("\n" + "=" * 50)
print("RINGKASAN AKTIVITAS")
print("=" * 50)

print(f"Total aktivitas : {len(daftar_aktivitas)}")
print(f"Total durasi    : {total_durasi} jam")