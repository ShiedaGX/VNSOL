# Definisi gambar latar. Latar rumah, kamar, mobil, dan terminal masih berupa
# placeholder; sprite karakter dimuat otomatis dari folder game/images/.
#
# Untuk mengganti latar dengan gambar asli, taruh file di game/images/
# dengan nama yang sama, misalnya:
#   game/images/bg rumah.png
# lalu hapus baris renpy.image yang bersangkutan di bawah.


## Latar #######################################################################

# Latar kota memakai gambar yang sama dengan main menu.
image bg kota = "gui/main_menu.png"

init python:

    def placeholder_bg(label, color):
        return Fixed(
            Solid(color),
            Text(label, xalign=0.5, yalign=0.5, size=64, color="#ffffff55"),
        )

    renpy.image("bg terminal", placeholder_bg("Terminal Bus - Senja", "#2a2048"))
    renpy.image("bg mobil", placeholder_bg("Di Dalam Mobil", "#1f1a3d"))
    renpy.image("bg rumah", placeholder_bg("Rumah Tante Mila", "#3a2750"))
    renpy.image("bg kamar", placeholder_bg("Kamar Baru", "#2c2144"))


## Sprite karakter #############################################################

# Sprite Mila dan Luna dimuat otomatis dari folder game/images/ berdasarkan
# nama file, tidak perlu didefinisikan di sini:
#   mila normal / happy / surprised / tease
#   luna normal / tired / smirk / soft
# Untuk mengganti dengan ilustrasi sendiri, timpa file PNG dengan nama yang sama.
