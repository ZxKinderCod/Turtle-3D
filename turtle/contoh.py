import turtle as t

# Setup dasar
t.speed(3)  # speed 1-10, makin besar makin cepat
t.bgcolor("white")

# Fungsi untuk pindah tanpa gambar garis
def pindah(x, y):
    t.penup()      # angkat pena
    t.goto(x, y)   # pindah ke koordinat
    t.pendown()    # turunkan pena
    
# Buat segitiga 1 gunung
pindah(-200, 0)
t.goto(0, 150)     # ke puncak
t.goto(200, 0)     # ke kanan bawah
t.goto(-200, 0)    # balik ke awal
# Buat segitiga 2 gunung
pindah(-100, 0) 
t.goto(100, 120)     # ke puncak
t.goto(300, 0)     # ke kanan bawah
t.goto(-100, 0)    # balik ke awal
