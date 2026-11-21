# Gambar placeholder agar game bisa langsung dijalankan.
#
# Untuk mengganti dengan gambar asli, taruh file di folder game/images/
# dengan nama yang sama, misalnya:
#   game/images/bg rumah.png
#   game/images/mila happy.png
# lalu hapus baris image yang bersangkutan di file ini.


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

init python:

    for ekspresi in ("normal", "happy", "surprised", "tease"):
        renpy.image(("mila", ekspresi), Placeholder("girl"))

    for ekspresi in ("normal", "tired", "smirk", "soft"):
        renpy.image(("luna", ekspresi), Placeholder("girl"))
