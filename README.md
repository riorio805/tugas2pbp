# tugas4pbp

Link to webpage:<br>
-> Not online yet, just clone the repository and run it locally.
Previous weeks page: [here](./archive/archive_list.md)<br>

(only works on the website)<br>
Link to main: [here](./main)<br>


Second last checklist items:<br>
[UserCreationForm](#genesis)
\- [Authentic & Authoric](#abyssgard)
\- [Eat cookies](#yummy)
\- [Bad cookies](#yucky)
\- [Implementasi](#How-to)<br>

<br>

## Checklist
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
- [x] Menghubungkan model `Item` dengan `User`.
- [x] Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- [ ] Menjawab beberapa pertanyaan berikut pada `README.md` pada *root folder* (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    - [ ] Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
    - [ ] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    - [ ] Apa itu *cookies* dalam konteks aplikasi web, dan bagaimana Django menggunakan *cookies* untuk mengelola data sesi pengguna?
    - [ ] Apakah penggunaan *cookies* aman secara *default* dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    - [ ] Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

**Bonus:**
- [x] Tambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
- [x] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.
Kedua fitur di atas wajib diimplementaskan (bukan sekedar tombol, melainkan harus dapat melakukan fungsi yang diinginkan) jika kamu ingin mendapatkan nilai bonus.

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

---
<a id="yucky"></a>
## yucky cookies [↑](#)

---
<a id="how-to"></a>
## How to [↑](#)

#### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Menggunakan UserCreationForm sebagai template form untuk mendaftar sebuah user. Proses login dapat menggunakan fungsi `authorisation` yang diberikan langsung dari Django, dengan input yang didapatkan dari sebuah Form. Login juga menentukan sebuah cookie yang menunjukkan login terakhir. Logout juga dapat menggunakan fungsi `logout`, dan hapus semua cookie yang tersimpan di browser.

#### Membuat **dua** akun pengguna dengan masing-masing **tiga** *dummy data* menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
<img src="./static/main/readme/2users3items.png" /><br>
Pada website, terdapat sebuah user "rio" yang merupakan admin, dan user "PakBepe" yang merupakan user biasa.

#### Menghubungkan model `Item` dengan `User`.
Membuat field baru di model Item yang merupakan sebuah ForeignKey, yang dapat dihubungkan dengan sebuah user menggunakan data dari request.

#### Menampilkan detail informasi pengguna yang sedang *logged in* seperti *username* dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
Ketika login, kita menambahkan cookies dengan key `last_login` dan value waktu sekarang. Saat fungsi `show_main` dijalankan, kita mengambil cookie `last_login` dan mengambil username dari `request.user`, lalu passing kedalam context, dimana data tersebut dapat ditampilkan menggunakan template HTML.

#### Tambahkan tombol dan fungsi untuk menambahkan `amount` suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
Membuat suatu fungsi baru di `main.views` yang mengambil id dari objek dan amount yang ingin ditambah, lalu menambahkan amount dari item dengan id yang diberikan (jika ada). Lalu menghubungkan sebuah url ke fungsi tersebut. Terakhir, membuat button di website main yang redirect ke url yang sudah dihubungkan.

#### Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.
Sama mekanisme dengan menambah amount, tetapi fungsi ini menghapus item tersebut.


---
github-markdown.css by <a href="https://github.com/sindresorhus/github-markdown-css">sindresorhus</a> and used under the MIT License<br>
website by sefriano edsel jieftara, class of pbp d