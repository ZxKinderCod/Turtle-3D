import turtle as t

# Setup dasar
t.speed(2)  # speed 1-10, makin besar makin cepat
t.bgcolor("white")

# Fungsi untuk pindah tanpa gambar garis
def pindah(x, y):
    t.penup()      # angkat pena
    t.goto(x, y)   # pindah ke koordinat
    t.pendown()    # turunkan pena

# Contoh 1: Buat segitiga (gunung)
pindah(-200, 0)
t.goto(0, 150)     # ke puncak
t.goto(200, 0)     # ke kanan bawah
t.goto(-200, 0)    # balik ke awal

# Contoh 2: Garis horizontal (rumput)
pindah(-300, 0)
t.goto(300, 0)

# Contoh 3: Trapesium (jalan)
pindah(-50, 0)
t.goto(-20, -200)  # kiri bawah
t.goto(20, -200)   # kanan bawah
t.goto(50, 0)      # kanan atas

# Contoh 4: Garis putus-putus (marka jalan)
pindah(0, -10)
t.setheading(-90)  # arah ke bawah (0=kanan, 90=atas, 180=kiri, 270=bawah)
for i in range(5):
    t.forward(20)   # gambar garis
    t.penup()
    t.forward(15)   # loncat tanpa gambar
    t.pendown()

t.hideturtle()
t.done()