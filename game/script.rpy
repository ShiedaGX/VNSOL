# Naskah utama College Life.
# Karakter, variabel, dan pintu masuk cerita ada di file ini.
# Isi cerita per bab ada di file terpisah (bab1.rpy, dst).


## Karakter ####################################################################

# Nama protagonis bisa diganti pemain. Default-nya "Rael".
default player_name = "Rael"

define r = Character("[player_name]", color="#ffb27a")
define mila = Character("Tante Mila", color="#f7a8c4")
define luna = Character("Luna", color="#9ad1ff")
define ibu = Character("Ibu (pesan)", color="#c9b8ff")


## Variabel cerita #############################################################

# Poin kedekatan, dipengaruhi pilihan pemain.
default mila_aff = 0
default luna_aff = 0


## Awal permainan ##############################################################

label start:

    scene black with fade

    "Sebelum cerita dimulai..."

    menu:
        "Siapa yang akan kamu perankan?"

        "Rael (nama asli karakter)":
            $ player_name = "Rael"

        "Aku ingin memakai namaku sendiri":
            $ player_name = (renpy.input("Siapa namamu?", default="Rael", length=12, exclude="{}[]%") or "").strip() or "Rael"

    jump bab1
