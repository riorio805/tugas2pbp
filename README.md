# tugas2pbp

Link to page: [here](https://hsr-inventory.adaptable.app/main/)
<br><br>

## Checklist:
- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.
- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [ ] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).
    - Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    - Jelaskan mengapa kita menggunakan ***virtual environment***? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan ***virtual environment***?
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

## How to
#### Membuat sebuah proyek Django baru:
Buat git repository baru, lalu initialize ke sebuah folder lokal.<br>
Buat virtual environment python, aktifkan virtual environment dan install beberapa package yang diperlukan.<br>
Jalankan command "django-admin startproject inventory" (tetap didalam venv).<br>
Setup file inventory.settings agar semua host diperbolehkan akses website dan app "main" terdaftar sebagai aplikasi website.

#### Membuat aplikasi dengan nama `main` pada proyek tersebut:
Jalankan command "django-admin startapp main".<br>

#### Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`:
Menambahkan "path('main/', include('main.urls'))" di list urlpatterns di inventory.urls untuk mendefinisikan subdirektori main dengan file 'urls'nya sendiri.

#### Membuat model pada aplikasi `main` dengan nama `Item`:
Membuat class baru yang memiliki parent (django.db.)models.Model.
Menambahkan atribut menggunakan bawaan models. (contoh bil. bulat menggunakan "models.IntegerField()", string menggunakan models.TextField(), dst.)<br>
Atribut yang dipakai adalah "name", "amount", "description", "rarity", "effect". (self-explanatory)

#### Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML:
Buat fungsi "show_main" yang mengambil template main.html dan dibundle dengan context yang diberikan untuk mengembalikan response yang merupakan sebuah website.

#### Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`:
Di main.urls, buat list urlpatterns yang memuat 1 item, yang menghubungkan direktori "main/" dengan fungsi di main.views

#### Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet:
Hubungkan git repository ke adaptable.
Setup versi python dan command awal.
Wait deployment (😴😴😴)<br>
Done

#### Membuat sebuah `README.md` yang berisi tautan menuju aplikasi Adaptable yang sudah di-*deploy*:
You're reading this right now 👍👍👍👍 (keep going)

#### Bonus things *:)*
- Database implemented.
There's 21 items in the database and the server randomly chooses 5 items to show the user. (see main.views) <br>
- Redirect from '/' to '/main/'
##

## here's a picture maybe
Not yet

## Why use
Virtual environment digunakan karena 

Pembuatan aplikasi web tanpa menggunakan *virtual environment* masih tetap mungkin, tetapi ini tidak merupakan *best practices* karena dapat menimbulkan beberapa isu, seperti:
\- Konflik *dependencies* : 

## What is
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.