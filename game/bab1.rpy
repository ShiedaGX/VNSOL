# Bab 1: Alamat Baru
#
# Rael (19) baru masuk kuliah dan harus tinggal bersama tantenya, Mila (37),
# serta sepupunya, Luna (21).

label bab1:

    ## Judul bab ###############################################################

    scene black with fade
    show text "{size=+20}Bab 1{/size}\n{i}Alamat Baru{/i}" at truecenter with dissolve
    pause 2.5
    hide text with dissolve


    ## Adegan 1: Terminal bus ###################################################

    scene bg terminal with fade

    "Dua belas jam di dalam bus, dan akhirnya aku sampai."

    "Kota ini terlalu besar, terlalu ramai, dan terlalu terang untuk anak dari desa kecil yang listriknya masih sering padam."

    "Namaku [player_name]. Sembilan belas tahun. Mahasiswa baru Universitas Cakrawala, jurusan Desain Komunikasi Visual."

    "Dan mulai malam ini, aku akan tinggal di rumah seorang tante yang terakhir kali kulihat sepuluh tahun lalu."

    ibu "Sudah sampai? Tante Mila yang jemput, ya. Ucapkan terima kasih, dan jangan merepotkan."

    r "Iya, Bu. Baru turun dari bus."

    "Ingatanku tentang Tante Mila cuma satu: perempuan yang dulu suka mengepang rambutku."

    "Jadi aku mencari-cari seorang ibu berdaster di antara kerumunan."

    "Yang kutemukan malah seorang perempuan berkardigan krem, melambai sambil mengangkat kertas bertuliskan namaku dengan spidol besar."

    show mila happy at center with dissolve

    mila "Di sini! Di sini! Astaga, tinggi sekali kamu sekarang!"

    r "Eh... Kak Luna, ya? Maaf, aku belum pernah ketemu langsung..."

    show mila surprised

    mila "Luna? Hahaha!"

    show mila happy

    mila "Aduh, kamu bikin Tante senang sekali. Tapi bukan, ini Tante Mila. Tante kamu."

    r "..."

    r "Tante?!"

    menu:
        "Bagaimana reaksi [player_name]?"

        "\"Maaf, Tante! Habisnya Tante kelihatan muda sekali.\"":
            $ mila_aff += 1
            show mila tease
            mila "Pintar sekali merayu. Pasti menurun dari ayahmu."

        "\"Serius? Tante Mila yang dulu suka mengepang rambutku?\"":
            show mila normal
            mila "Yang itu. Waktu memang cepat sekali berlalu, ya."

        "(Terdiam, wajahku terasa panas)":
            show mila tease
            mila "Hei, tidak apa-apa. Muka kamu merah sekali, lho. Lucu."

    show mila happy

    mila "Ayo, mobil Tante di parkiran. Biar Tante bawakan tasmu."

    r "Eh, tidak usah, Tante. Aku saja."

    mila "Baiklah, anak baik. Tapi kalau jatuh, Tante pura-pura tidak kenal."

    hide mila with dissolve


    ## Adegan 2: Di dalam mobil #################################################

    scene bg mobil with fade

    "Lampu kota bergeser pelan di kaca jendela. Tante Mila menyetir dengan santai, sesekali bersenandung."

    show mila normal at center with dissolve

    mila "Jadi, aturan rumah. Pertama: sarapan bareng. Kedua: cuci piring gantian. Ketiga..."

    r "Ketiga?"

    mila "Jangan pernah, apa pun yang terjadi, menyentuh es krim di kulkas bagian bawah."

    r "Itu punya Tante?"

    show mila tease

    mila "Itu punya Luna. Dan Tante tidak mau jadi saksi mata kejadian berdarah."

    r "...Dicatat."

    show mila normal

    mila "Luna itu anak Tante. Umurnya dua puluh satu, semester lima di Komunikasi, kampusnya sama denganmu. Sambil kuliah dia kerja paruh waktu di kafe."

    mila "Om Dimas kerja di anjungan lepas pantai, pulangnya tiga bulan sekali. Jadi rumah kita biasanya ramai oleh dua perempuan saja. Sekarang bertambah satu."

    r "Tante punya Luna waktu masih muda sekali, ya?"

    show mila happy

    mila "Betul. Makanya orang-orang sering mengira kami kakak-adik. Tante sih tidak keberatan."

    "Aku tersenyum. Tapi ada yang mengganjal."

    "Di rumah, Ibu hampir tidak pernah menyebut nama adiknya sendiri. Kami juga tidak pernah mengunjungi Tante Mila. Rasanya aneh."

    hide mila with dissolve


    ## Adegan 3: Tiba di rumah #################################################

    scene bg rumah with fade

    "Rumah dua lantai yang tidak terlalu besar, dengan lampu teras kuning yang hangat dan pot-pot tanaman berjajar rapi."

    show mila happy at right with dissolve

    mila "Selamat datang di rumah barumu."

    "Aku baru melangkah masuk ketika sesosok bayangan menuruni tangga sambil menguap lebar."

    show luna tired at left with dissolve

    luna "Ma, berisik banget di bawah... jam segini orang mau tidur..."

    show luna normal

    luna "...Siapa ini?"

    mila "Rael, sepupumu. Anak Mbak Ratna. Ingat, kan?"

    "Perempuan di hadapanku memakai hoodie kebesaran, rambut sepundaknya berantakan, tapi matanya tajam menilai dari atas sampai bawah."

    show luna smirk

    luna "Oh. Yang dulu nangis gara-gara dikejar angsa itu?"

    r "Itu sepuluh tahun lalu!"

    menu:
        "Balas bagaimana?"

        "\"Dan Kak Luna dulu ngompol di tenda waktu kemah keluarga.\"":
            $ luna_aff += 2
            show luna normal
            luna "..."
            show luna smirk
            luna "Ma, dia berani. Anak ini bisa dipertahankan."
            mila "Luna, jangan seperti itu pada tamu."
            luna "Dia bukan tamu, dia penghuni. Beda urusan."

        "\"Angsanya besar sekali, Kak. Aku masih trauma.\"":
            $ luna_aff += 1
            show luna soft
            luna "Pfft. Oke, itu jujur. Aku suka orang jujur."

        "\"Iya... itu aku. Senang bertemu lagi, Kak Luna.\"":
            $ mila_aff += 1
            show luna normal
            luna "Formal banget. Santai saja, kita sepupu."
            mila "Nah, begini baru sopan."

    show luna smirk

    luna "Kamarmu di lantai atas, sebelah kamarku. Ayo, kutunjukkan."


    ## Adegan 4: Kamar baru #####################################################

    scene bg kamar with fade

    "Kamarnya kecil tapi bersih. Ada kasur, meja belajar, lemari, dan jendela yang menghadap ke arah kota."

    show luna normal at center with dissolve

    luna "Dindingnya tipis. Kalau kamu setel musik jam dua pagi, aku tahu."

    r "Aku tidak seburuk itu, Kak."

    luna "Semua orang bilang begitu sebelum jam dua pagi."

    luna "Eh, ospek besok, kan? Kampusnya sama. Aku berangkat jam setengah tujuh naik motor. Kalau mau bareng, jangan telat."

    menu:
        "Bagaimana jawabanmu?"

        "\"Mau, Kak. Makasih!\"":
            $ luna_aff += 1
            show luna soft
            luna "Oke. Satu hal: aku nggak nunggu orang yang lagi pakai sepatu."

        "\"Aku naik angkot saja, tidak mau merepotkan.\"":
            show luna smirk
            luna "Hm. Terserah. Tapi nanti kalau nyasar, jangan telepon aku."

        "\"Boleh, tapi Kakak nyetirnya pelan-pelan, ya.\"":
            $ luna_aff += 1
            show luna smirk
            luna "Nggak janji."

    show luna normal

    luna "Ya sudah. Selamat datang, sepupu."

    hide luna with dissolve

    "Pintu menutup pelan. Dari balik dinding, terdengar langkahnya menjauh, lalu sebuah pintu lain dibanting kecil."


    ## Adegan 5: Malam pertama ##################################################

    scene bg kota with fade

    "Dari jendela, kulihat menara jam kampus berdiri di antara cahaya kota. Jaraknya tidak jauh."

    "Besok hari pertama. Orang baru, tempat baru, hidup baru."

    "Aku membongkar tas, menggantung jaket, dan hampir melupakan satu hal."

    "Dari saku jaket, terselip selembar foto yang kuyakin tidak kuletakkan di sana."

    "Foto tua. Tiga perempuan muda tertawa di depan sebuah toko kecil. Satu adalah Ibu. Satu lagi, Tante Mila."

    "Yang ketiga, aku tidak mengenalnya."

    "Di balik foto, ada tulisan tangan Ibu:"

    ibu "Jangan tunjukkan ini pada Mila. Belum waktunya."

    r "..."

    r "Ibu, sebenarnya apa yang kamu sembunyikan?"

    "Di luar, menara jam berdentang sekali. Entah kenapa, rasanya seperti tanda bahwa cerita ini baru saja dimulai."

    scene black with fade
    show text "{i}Bersambung...{/i}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    return
