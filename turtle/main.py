import turtle as t

# Setup dasar
t.speed(5)  # speed 1-10, makin besar makin cepat
t.bgcolor("white")

# Fungsi untuk pindah tanpa gambar garis
def pindah(x, y):
    t.penup()      # angkat pena
    t.goto(x, y)   # pindah ke koordinat
    t.pendown()    # turunkan pena

# Buat segitiga (gunung)
pindah(-200, 0)
t.goto(0, 150)     # ke puncak
t.goto(200, 0)     # ke kanan bawah
t.goto(-200, 0)    # balik ke awal

# Garis horizontal (garis di )
pindah(-300, 0)
t.goto(300, 0)

# Trapesium (jalan)
pindah(15, 0) 
t.goto(50, -290)  # kiri bawah
t.goto(-50,-290)   # kanan bawah
t.goto(-15, 0)      # kanan atas 
t.goto(20, 0)      # puncak

# Garis putus-putus (marka jalan)
pindah(0, -10)
t.setheading(-90)  # arah ke bawah (0=kanan, 90=atas, 180=kiri, 270=bawah)
for i in range(10):
    t.forward(20)   # gambar garis
    t.penup()
    t.forward(15)   # loncat tanpa gambar
    t.pendown()

# buat sawah
pindah (-280,-30)
t.goto(-30,-40)
t.goto(-60,-240)
t.goto(-310,-220)
t.goto(-280,-30)



t.hideturtle()
t.done()