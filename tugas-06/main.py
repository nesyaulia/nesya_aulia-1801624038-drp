# IF STATEMENT

# AKTIVITAS SARAPAN 

# INPUT
aktivitas = "sarapan"
menu = "telur"

if aktivitas == "sarapan":

    if menu == "telur":
        perlu_masak = True

    elif menu == "ikan":
        perlu_masak = True

    elif menu == "nugget":
        perlu_masak = True

    else:
        perlu_masak = False

    # OUTPUT
    if perlu_masak:
        print("Bahan tersedia, silakan masak terlebih dahulu!")

    else:
        print("Bahan tidak tersedia, beli terlebih dahulu!")

# AKTIVITAS BERANGKAT KERJA

# INPUT
from datetime import datetime

waktu_sekarang = datetime.now()

jam_masuk = waktu_sekarang.replace(
    hour=8,
    minute=0,
    second=0,
    microsecond=0
)

terlambat = waktu_sekarang > jam_masuk

# OUTPUT
if terlambat:
    print("Kamu terlambat masuk kerja!")

else:
    print("Kamu belum terlambat, semangat!") 

    