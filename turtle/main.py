import turtle as t

# Setup dasar
t.speed(7)  # speed 1-10, makin besar makin cepat
screen = t.Screen()
screen.bgcolor("#ffe0b2")

# Fungsi garis
def pindah(x, y):
    t.penup()      # angkat kursor
    t.goto(x, y)   # pindah ke koordinat
    t.pendown()    # turunkan kursor

# segitiga gunung
t.color("black", "darkgreen")  # garis hitam, isi hijau
t.begin_fill()
pindah(-200, 0)
t.goto(0, 150)     # ke puncak
t.goto(200, 0)     # ke kanan bawah
t.goto(-200, 0)    # balik ke awal
t.end_fill()

# Garis horizontal (garis di )
pindah(-300, 0)
t.goto(300, 0)

# Trapesium (jalan)
t.color("black", "#bfbfbf")  # garis hitam, isi abu-abu
t.begin_fill()
pindah(15, 0) 
t.goto(50, -290)  # kiri bawah
t.goto(-50,-290)   # kanan bawah
t.goto(-15, 0)      # kanan atas 
t.goto(20, 0)      # puncak
t.end_fill()

# Garis putus-putus (marka jalan)
pindah(0, -10)
t.setheading(-90)  # arah ke bawah (0=kanan, 90=atas, 180=kiri, 270=bawah)
for i in range(10):
    t.forward(20)   # gambar garis
    t.penup()
    t.forward(15)   # loncat tanpa gambar
    t.pendown()

# buat sawah
t.color("black", "#8fd18b")  # hijau sawah
t.begin_fill()
pindah (-280,-30)
t.goto(-30,-40)
t.goto(-60,-240)
t.goto(-310,-220)
t.goto(-280,-30)
t.end_fill()

# contoh 2 : buat garis horizontal sawah 
pindah(-285,-65)
t.goto(-36,-80)

pindah(-292,-110)
t.goto (-43,-130)

pindah (-300,-165)
t.goto (-50,-185)

#contoh 3 : buat garis vertikal sawah
pindah(-220,-32)
t.goto(-250,-227)

pindah (-155,-34)
t.goto (-180,-230)

pindah (-87,-39)
t.goto (-116,-238)

#isian sawah
def rumput(x, y, ukuran=20):

    pindah(x, y)
    t.setheading(130)
    t.forward(ukuran)

    pindah(x, y)
    t.setheading(50)
    t.forward(ukuran)
# posisi awal
start_x = -270
start_y = -50

jarak_x = 66
jarak_y = 58

for baris in range(4):
    for kolom in range(4):
        x = start_x + kolom * jarak_x
        y = start_y - baris * jarak_y
        rumput(x, y, 25)

#Buat rumah sederhana 
#kotak rumah
t.color("black", "#ffcc99")  # garis hitam, isi oranye muda
t.begin_fill()
pindah(60,-200)
t.goto(160,-200)
t.goto(160,-100)
t.goto(60,-100)
t.goto(60,-200)
t.end_fill()

# Atap rumah 
t.color("black", "#322825")  # garis hitam, isi coklat tua
t.begin_fill()
pindah(60,-106)
t.goto(107,-10)
t.goto(162,-100)
t.goto(280,-100)
t.goto(280,-10)
t.goto(105,-10)
t.goto(60,-106)
t.end_fill()

#tubuh rumah
t.color("black", "#ffcc99")  # garis hitam, isi oranye muda
t.begin_fill()
pindah(160,-100)
t.goto(160,-200)
t.goto(280,-200)
t.goto(280,-100)
t.goto(160,-100)
t.end_fill()

#Pintu rumah
t.color("black", "#B3E3E9")  # garis hitam, isi biru muda
t.begin_fill()
pindah(100,-200)
t.goto(140,-200)
t.goto(140,-150)
t.goto(100,-150)
t.goto(100,-200)
t.end_fill()

#jalan pintu rumah ke samping jalan
pindah(100,-200)
t.goto(44,-240)

pindah(140,-200)
t.goto(47,-280)

# jendela rumah
t.color("black", "#DE87BA")  # garis hitam, isi pink
t.begin_fill()
pindah(200,-150)
t.goto(240,-150)
t.goto(240,-110)
t.goto(200,-110)
t.goto(200,-150)
t.end_fill()

#tanda + di jendela
pindah(220,-150)
t.goto(220,-110)
pindah(200,-130)
t.goto(240,-130)

#garis genteng rumah miring
pindah(162,-100)
t.goto(280,-100)
t.goto(240,-10)

pindah(240,-100)
t.goto(190,-10)

pindah(200,-100)
t.goto(140,-10)

#garis genteng rumah horizontal
pindah(135,-55)
t.goto(280,-55)

pindah(149,-80)
t.goto(280,-80)

pindah(120,-30)
t.goto(280,-30)

#matahari
t.color("black", "yellow")  # garis hitam, isi kuning
t.begin_fill()
pindah(-200,200)
t.circle(40)
t.end_fill()





t.hideturtle()
t.done()