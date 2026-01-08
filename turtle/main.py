import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Menggambar kubus (representasi 2D)
# Persegi depan
for _ in range(4):
    t.forward(100)  # Maju 100 piksel
    t.right(90)     # Belok kanan 90 derajat

# Pindah ke posisi untuk persegi belakang
t.penup()
t.goto(100, 50)  # Geser ke kanan atas untuk proyeksi isometrik kubus
t.pendown()

# Persegi belakang
for _ in range(4):
    t.forward(100)  # Maju 100 piksel
    t.right(90)     # Belok kanan 90 derajat

# Hubungkan sudut-sudut untuk efek 3D
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(80, 40)  # Diagonal kiri bawah (dipendekkan)

t.penup()
t.goto(100, 0)
t.pendown()
t.goto(180, 40)  # Diagonal kanan bawah (dipendekkan)

t.penup()
t.goto(0, 100)
t.pendown()
t.goto(100, 150)  # Diagonal kiri atas

t.penup()
t.goto(100, 100)
t.pendown()
t.goto(200, 150)  # Diagonal kanan atas

# Menutup jendela saat diklik
turtle.done()
