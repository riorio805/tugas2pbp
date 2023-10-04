# tugas0.8pbp

Link to webpage:<br>
-> Not online yet, just clone the repository and run it locally.<br>
Previous weeks page: [here](./archive/archive_list.md)<br>

(only works on the website)<br>
Link to main: [here](./main)<br>


Checklist items:<br>
[UserCreationForm](#genesis)
\- [Authentic & Authoriz](#abyssgard)
\- [Eat cookies](#yummy)
\- [Bad cookies](#yucky)
\- [Implementasi](#how-to)<br>

More checklist items:<br>
[Element selector](#quantum)
\- [HTML5 Tag](#roblox-moderation)
\- [Margin & Padding](#empty-spaces)
\- [CSS framework](#chrome-wrap)
\- [Implementasi 2](#how-to-the-sequel)<br>


<br>

## Checklist
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
- [x] Menghubungkan model `Item` dengan `User`.
- [x] Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- [ ] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [x] Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
    - [x] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    - [ ] Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
    - [ ] Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

**Bonus:**
- [x] Tambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
- [x] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.
Kedua fitur di atas wajib diimplementaskan (bukan sekedar tombol, melainkan harus dapat melakukan fungsi yang diinginkan) jika kamu ingin mendapatkan nilai bonus.

## Checklist the sequel
- [x] Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
    - [x] Kustomisasi halaman *login*, *register*, dan tambah inventori semenarik mungkin.
    - [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan *apporach* lain seperti menggunakan **Card**. 
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [x] Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya. 
    - [x] Jelaskan HTML5 Tag yang kamu ketahui.
    - [x] Jelaskan perbedaan antara *margin* dan *padding*.
    - [x] Jelaskan perbedaan antara *framework* CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

**Bonus:**
- [x] Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari *item* pada inventori anda **menggunakan CSS**. 

---
<a id="genesis"></a>
## genesis [↑](#)
UserCreationForm adalah sebuah form yang disediakan oleh Django untuk membuat suatu user baru. Kita menggunakan `UserCreationForm` sebagai *interface* untuk menambahkan suatu User dengan mudah dan tanpa kerumitan. Penggunaan UserCreationForm juga dapat meningkatkan keamanan dari website kita, karena secara otomatis password akan di-*hash*, sehingga susah dijebol oleh seorang *middleman*.

Kekurangan dari form tersebut adalah limitasi dari *fields* yang dapat digunakan, sehingga jika ingin membuat website registrasi yang memiliki fields yang aneh-aneh, diperlukan form baru yang inherit dari UserCreationForm, atau dibuat dari awal yang inherit dari ModelForm.

---
<a id="abyssgard"></a>
## abyssgard [↑](#)
Autentikasi merupakan sebuah proses yang bertujuan memverifikasi identitas dari sebuah pengguna benar-benar merupakan pengguna tersebut. Biasanya autentikasi dilakukan dengan menggunakan username dan password yang diketahui oleh pengguna. Otorisasi merupakan proses yang bertujuan verifikasi apakah pengguna tersebut dapat melakukan sebuah aksi pada server. Otorisasi dilakukan secara internal, dengan verifikasi terjadi langsung di servernya. Otorisasi dilakukan agar pengguna tidak melakukan hal yang tidak boleh dilakukan. Autentikasi dan Otorisasi penting dilaksanakan karena merupakan 2 hal yang harus dilakukan agar server kita menjadi aman.

---
<a id="yummy"></a>
## yummy cookies [↑](#)
Cookies merupakan sebuah 

---
<a id="yucky"></a>
## yucky cookies [↑](#)
Penggunaan cookies secara default tidak aman.

---
<a id="how-to"></a>
## How to [↑](#)

#### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Menggunakan UserCreationForm sebagai template form untuk mendaftar sebuah user. Proses login dapat menggunakan fungsi `authorisation` yang diberikan langsung dari Django, dengan input yang didapatkan dari sebuah Form. Login juga menentukan sebuah cookie yang menunjukkan login terakhir. Logout juga dapat menggunakan fungsi `logout`, dan hapus semua cookie yang tersimpan di browser.

#### Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
<img src="./static/main/readme/2users3items.png"/><br>
Pada website, terdapat sebuah user "rio" yang merupakan admin, dan user "PakBepe" yang merupakan user biasa.

#### Menghubungkan model `Item` dengan `User`.
Membuat field baru di model Item yang merupakan sebuah ForeignKey, yang dapat dihubungkan dengan sebuah user menggunakan data dari request.

#### Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
Ketika login, kita menambahkan cookies dengan key `last_login` dan value waktu sekarang. Saat fungsi `show_main` dijalankan, kita mengambil cookie `last_login` dan mengambil username dari `request.user`, lalu passing kedalam context, dimana data tersebut dapat ditampilkan menggunakan template HTML.

#### Tambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
Membuat suatu fungsi baru di `main.views` yang mengambil id dari objek dan amount yang ingin ditambah, lalu menambahkan amount dari item dengan id yang diberikan (jika ada). Lalu menghubungkan sebuah url ke fungsi tersebut. Terakhir, membuat button di website main yang redirect ke url yang sudah dihubungkan.


---
---
<a id="quantum"></a>
## monoquantum [↑](#)
Jelaskan manfaat dari setiap *element selector* dan kapan waktu yang tepat untuk menggunakannya.
Terdapat beberapa tipe *element selector* yang dapat digunakan di CSS:
1. Type selector<br>
Syntax: `elemen { styles }`<br>
Selector ini digunakan sebagai selector general, sebaiknya digunakan jika elemen hanya memiliki 1 *use case*, atau ingin membuat variabel baru yang dapat diturunkan.
2. Class selector<br>
Syntax: `elemen { styles }`<br>
Selector ini digunakan sebagai selector spesifik, digunakan untuk memilih suatu class.
3. ID selector<br>
Syntax: `elemen { styles }`<br>
Selector ini digunakan sebagai selector paling spesifik (hanya 1), digunakan jika terdapat banyak blok yang memiliki class yang sama tetapi ID berbeda.
4. Descendant selector<br>
Syntax: `ancestor descendant { styles }`<br>
Selector ini digunakan sebagai selector struktur, dan digunakan ketika hanya memilih suatu tag dalam dari sebuah tag.
5. Child selector<br>
Syntax: `parent > child { styles }`<br>
Selector ini digunakan sebagai selector relasi, dengan memilih child yang hanya 1 langkah dari sebuah parent. Selector ini digunakan untuk memilih elemen yang memiliki kedalaman yang lebih spesifik.
6. Adjacent sibling selector<br>
Syntax: `elemen1 + elemen2 { styles }`<br>
Selector ini digunakan sebagai selector urutan, dengan memilih elemen2 yang berada pas didepan elemen1. Ini digunakan ketika memiliki banyak blok konten didalam satu blok besar.
7. General sibling selector<br>
Syntax: `elemen1 ~ elemen2 { styles }`<br>
Selector ini digunakan sebagai selector urutan juga, tetapi dengan memilih semua elemen2 yang berada didepan elemen1.

Element selector ini dapat dikombinasikan dan digabungkan (menggunakan `,`) untuk menentukan styles dari elemen dengan spesifisitas yang diingin oleh developer.

---
<a id="roblox-moderation"></a>
## roblox be like: #### [↑](#)
Tag yang baru di HTML5 yang saya ketahui:

#### Semantic structure tags:<br>
`<article>, <aside>, <footer>, <header>, <nav>, <section>` <br>
Keenam HTML tag ini berfungsi sebagai penanda struktur konten yang ditampilkan pada browser, agar pembaca file HTML dapat dengan mudah melihat strukturnya.

#### Display tags:<br>
`<details>` => Tag ini berfungsi untuk menampilkan informasi yang awalnya disembunyikan hingga user menekan sebuah tombol<br>
`<mark>` => Tag ini berfungsi untuk meng-*highlight* suatu teks.

#### Input tags: <br>
`<datalist>` => Tag ini ditempatkan setelah tag `<input>` dan berfungsi untuk menampilkan beberapa input yang sudah ditentukan sebagai rekomendasi terhadap input.

#### Media tags: <br>
`<audio>` => Tag ini digunakan untuk memasukkan sebuah file berupa audio ke web browser. File audio dapat langsung dimainkan saat webpage di-load.<br>
`<video>` => Sama seperti tag `<audio>`, tetapi ini digunakan untuk memasukkan file yang berupa video<br>
`<embed>` => Tag ini digunakan untuk memasukkan file yang datang dari website eksternal.<br>
`<canvas>` => Tag ini digunakan untuk menggambarkan grafik dari sebuah media audiovisual secara *real-time* dengan menggunakan JavaScript. Contoh penggunaan tag ini adalah untuk menampilkan sebuah permainan.

---
<a id="empty-spaces"></a>
## unliminal [↑](#)
Margin adalah pemisah antara sebuah blok konten dengan block lainnya, dan padding adalah pemisah isi blok konten dengan pembatas(border) dari blok tersebut.

---
<a id="chrome-wrap"></a>
## Chrome color wrapping paper [↑](#)
Framework Bootstrap memberikan halaman web yang sangat responsif yang cocok untuk pembuatan web untuk *mobile* dan *desktop* sekaligus. Namun, Bootstrap tidak memiliki banyak kebebasan mengenai bagaimana struktur situs web dirancang. Berbeda dengan Tailwind, Bootstrap merupakan sebuah UI Kit, yang berarti sekumpulan komponen UI yang sudah dibuat dan dapat dengan mudah diimplementasikan. Bootstrap sebaiknya digunakan ketika kita belum menguasai CSS, dan hanya ingin mengembangkan website yang bersih dan rapi dengan waktu yang cepat.

Sedangkan, framework Tailwind memberikan banyak kebebasan bagi *developer* untuk menentukan struktur dari websitenya. Ini dikarenakan Tailwind hanya memberikan widget yang dapat diambil dan dibuat menjadi komponen oleh *developer*-nya. Tailwind sebaiknya digunakan ketika kita sudah memiliki ilmu banyak mengenai CSS, dan ingin mengekspresikan kreativitas dalam web design.

---
<a id="how-to-the-sequel"></a>
## How to (sequel edition) [↑](#)

#### Kustomisasi halaman *login*, *register*, dan tambah inventori semenarik mungkin.
#### Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan *apporach* lain seperti menggunakan **Card**. 
Saya menggunakan 2 file external CSS, yaitu framework Bootstrap, dan stylesheet github-markdown, keduanya dimodifikasi. File ini digunakan untuk mengeluarkan suatu pesona yang mirip dengan website dari Github Pages yang menggunakan Markdown. Didalam file HTMLnya, dibuat styles lagi agar mencapai hasil yang memuaskan. Saya juga menggunakan gambar untuk 

#### Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari *item* pada inventori anda **menggunakan CSS**. 
Sebelum daftar item dipassing ke template, kita mengambil id dari item terakhir. Di file HTML, digunakan template tags untuk mengecek id dari item terakhir, lalu mengubah item tersebut agar display teks dengan warna beda (dalam website saya, warnanya adalah animasi warna pelangi)