import turtle as t

def pindah(x, y):
    t.penup()      # angkat pena
    t.goto(x, y)   # pindah ke koordinat
    t.pendown()    # turunkan pena

# Setup dasar
t.speed(2)  # speed 1-10, makin besar makin cepat
t.bgcolor("white")
# Contoh 1: Buat (Jalan)
pindah(20, 0) 
t.goto(50, -290)  # kiri bawah
t.goto(-50,-290)   # kanan bawah
t.goto(-10, 0)      # kanan atas 
t.goto(20, 0)      # puncak

# contoh 1 : buat sawah
pindah (-280,0)
t.goto(-30,-20)
t.goto(-60,-240)
t.goto(-300,-220)
t.goto(-280,0)





t.hideturtle()
t.done()